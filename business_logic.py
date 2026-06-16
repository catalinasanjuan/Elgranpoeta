# business_logic.py
from data_access import DataAccess
from models import Bodega, Producto

data_access = DataAccess()


def obtener_usuario_por_nombre(nombre_usuario):
    return data_access.obtener_usuario_por_nombre(nombre_usuario)


def obtener_productos():
    productos = data_access.obtener_productos()
    return productos

def obtener_categorias():
    categorias = data_access.obtener_categorias()
    return categorias

def descontinuar_producto(codigo):
    try:
        resultado = data_access.descontinuar_producto(codigo)
        return resultado
    except Exception as e:
        print(f"Error al descontinuar producto: {e}")
        return False

def obtener_bodega_por_nombre(nombre):
    try:
        return data_access.obtener_bodega_por_nombre(nombre)
    except Exception as e:
        print(f"Error al obtener la bodega: {e}")
        return None

def obtener_bodegas():
    bodegas = data_access.obtener_bodegas()
    return bodegas

def agregar_bodega(data):
    try:
        data_access.agregar_bodega(data['nombre'], data['capacidad'], data['calle'], data['numero'], data['ciudad'], data['region'])
        return True
    except Exception as e:
        print(f"Error al agregar bodega: {e}")
        return False

def modificar_bodega(nombre, data):
    try:
        bodega = data_access.obtener_bodega_por_nombre(nombre)
        if bodega:
            data_access.modificar_bodega(nombre, data['nombre'], data['capacidad'], data['calle'], data['numero'], data['ciudad'], data['region'])
            return True
        return False
    except Exception as e:
        print(f"Error al modificar bodega: {e}")
        return False


def agregar_producto(data):
    try:
        data_access.agregar_producto(data['nombre'], data['cantidad'], data['ubicacion'], data['precio'], data['descripcion'])
        return True
    except Exception as e:
        print(f"Error al agregar producto: {e}")
        return False

def obtener_reporte_inventario():
    reporte_inventario = data_access.obtener_reporte_inventario()
    return reporte_inventario

def obtener_reporte_valoracion_bodegas():
    reporte_valoracion_bodegas = data_access.obtener_reporte_valoracion_bodegas()
    return reporte_valoracion_bodegas

def obtener_reporte_stock():
    reporte_stock = data_access.obtener_reporte_stock()
    return reporte_stock


# listoko
def modificar_producto(codigo, data):
    print(data)
    conn = None
    cursor = None
    data_access.modificar_producto(codigo, data['nombre_producto'], data['descripcion'], data['precio'], data['cantidad_stock'], data['nombre_categoria'], data['ubicacion'])
    return True


def obtener_producto_por_codigo(codigo):
    try:
        producto = data_access.obtener_producto_por_codigo(codigo)
        return producto
    except Exception as e:
        print(f"Error al obtener producto: {e}")
        return None