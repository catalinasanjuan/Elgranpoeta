from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from functools import wraps
import business_logic
from data_access import DataAccess
from config import db_config
import hashlib
import os

# Crear una instancia de DataAccess
data_access = DataAccess(db_config)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave-temporal-dev')

# Decorador para requerir login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/inventario', methods=['GET', 'POST'])
@login_required
def inventario():
    categorias = business_logic.obtener_categorias()
    titulo = request.args.get('titulo')
    descripcion = request.args.get('descripcion')
    codigo = request.args.get('codigo')
    tipo_producto = request.args.get('tipo_producto')

    productos = business_logic.obtener_productos()
    print("Productos en ruta:", productos)  # Debug print

    if titulo:
        productos = [p for p in productos if titulo.lower() in p['nombre_producto'].lower()]
    if descripcion:
        productos = [p for p in productos if descripcion.lower() in p['descripcion'].lower()]
    if codigo:
        try:
            codigo = int(codigo)
            productos = [p for p in productos if p['codigo'] == codigo]
        except ValueError:
            pass
    if tipo_producto:
        productos = [p for p in productos if tipo_producto.lower() in p['nombre_categoria'].lower()]

    return render_template('inventario.html', productos=productos, categorias=categorias)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = business_logic.obtener_usuario_por_nombre(username)
        if user:
            salt = user['salt']
            hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
            
            if hashed_password == user['hashed_password']:
                session['user_id'] = user['ID_Usuario']
                return redirect(url_for('index'))
            else:
                flash('Contraseña incorrecta.')
        else:
            flash('Usuario no encontrado.')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Otras rutas protegidas con el decorador @login_required

@app.route('/reportes')
@login_required
def reportes():
    reporte_inventario = business_logic.obtener_reporte_inventario()
    reporte_valoracion_bodegas = business_logic.obtener_reporte_valoracion_bodegas()
    reporte_stock = business_logic.obtener_reporte_stock()
    print("Reporte de Inventario en ruta:", reporte_inventario)  # Debug print
    print("Reporte de Valoración de Bodegas en ruta:", reporte_valoracion_bodegas)  # Debug print
    print("Reporte de Stock en ruta:", reporte_stock)  # Debug print
    return render_template('reportes.html', reporte_inventario=reporte_inventario,
                           reporte_valoracion_bodegas=reporte_valoracion_bodegas,
                           reporte_stock=reporte_stock)

@app.route('/rastreo')
@login_required
def rastreo():
    productos = business_logic.obtener_productos()
    bodegas = business_logic.obtener_bodegas()
    return render_template('rastreo.html', productos=productos, bodegas=bodegas)

@app.route('/ajustes')
@login_required
def ajustes():
    return render_template('ajustes.html')

@app.route('/bodegas', methods=['GET', 'POST'])
@login_required
def bodegas():
    if request.method == 'POST':
        data = request.json
        business_logic.agregar_bodega(data)
        return jsonify({'message': 'Bodega agregada exitosamente'}), 200

    bodegas = business_logic.obtener_bodegas()
    return render_template('bodegas.html', bodegas=bodegas)

@app.route('/bodegas/<nombre_bodega>', methods=['GET'])
@login_required
def obtener_bodega(nombre_bodega):
    bodega = business_logic.obtener_bodega_por_nombre(nombre_bodega)
    if bodega:
        return jsonify({
            'nombre_bodega': bodega['Nombre_Bodega'],
            'capacidad': bodega['Capacidad'],
            'calle': bodega['Calle'],
            'numero': bodega['Numero'],
            'ciudad': bodega['Ciudad'],
            'region': bodega['Region']
        })
    else:
        return jsonify({'error': 'Bodega no encontrada'}), 404

@app.route('/bodegas/editar/<nombre_bodega>', methods=['GET', 'POST'])
@login_required
def editar_bodega(nombre_bodega):
    if request.method == 'POST':
        data = request.form
        business_logic.modificar_bodega(nombre_bodega, data)
        return redirect(url_for('bodegas'))
    
    bodega = business_logic.obtener_bodega_por_nombre(nombre_bodega)
    if bodega:
        return render_template('editar_bodega.html', bodega=bodega)
    else:
        return "Bodega no encontrada", 404

@app.route('/productos/agregar', methods=['POST'])
@login_required
def agregar_producto():
    data = request.json
    resultado = business_logic.agregar_producto(data)
    if resultado:
        return jsonify({'message': 'Producto agregado exitosamente'}), 200
    else:
        return jsonify({'error': 'Error al agregar el producto'}), 400

@app.route('/productos/editar/<int:codigo>', methods=['GET', 'POST'])
@login_required
def editar_producto(codigo):
    print(request.method)
    if request.method == 'POST':
        data = request.form
        print("Datos recibidos para editar:", data)  # Mensaje de depuración
        resultado = business_logic.modificar_producto(codigo, data)
        if resultado:
            print("Producto editado exitosamente.")  # Mensaje de depuración
        else:
            print("Error al editar el producto.")  # Mensaje de depuración
        return redirect(url_for('inventario'))
    
    producto = business_logic.obtener_producto_por_codigo(codigo)
    if producto:
        return render_template('editar_producto.html', producto=producto)
    else:
        return "Producto no encontrado", 404



@app.route('/productos/descontinuar/<int:codigo>', methods=['DELETE'])
@login_required
def descontinuar_producto(codigo):
    resultado = business_logic.descontinuar_producto(codigo)
    if resultado:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 400

if __name__ == '__main__':
    app.run(debug=True)
