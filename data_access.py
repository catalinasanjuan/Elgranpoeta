import mysql.connector

class DataAccess:
    def __init__(self, db_config):
        self.db_config = db_config
        self.db = mysql.connector.connect(**db_config)
        self.cursor = self.db.cursor(dictionary=True)

    def obtener_usuario_por_nombre(self, nombre_usuario):
        query = "SELECT * FROM usuario WHERE Nombre_Usuario = %s"
        self.cursor.execute(query, (nombre_usuario,))
        return self.cursor.fetchone()

    def obtener_productos(self):
        query = """
        SELECT p.ID_Producto as codigo, p.Nombre_Producto as nombre_producto, 
            p.Descripcion as descripcion, p.Precio as precio, 
            s.Cantidad as cantidad_stock, c.Nombre_Categoria as nombre_categoria, 
            b.Nombre_Bodega as ubicacion
        FROM producto p
        JOIN stock s ON p.ID_Producto = s.Producto_FK
        JOIN categoria c ON p.Categoria_FK = c.ID_Categoria
        JOIN bodega b ON s.Bodega_FK = b.ID_Bodega
        """
        self.cursor.execute(query)
        productos = self.cursor.fetchall()
        return productos

    def obtener_categorias(self):
        query = "SELECT * FROM categoria"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def obtener_bodegas(self):
        query = """
        SELECT b.Nombre_Bodega as nombre_bodega, b.Capacidad, d.Calle, d.Numero, d.Ciudad, d.Region 
        FROM bodega b
        JOIN direccion d ON b.Direccion_FK = d.ID_Direccion
        """
        self.cursor.execute(query)
        bodegas = self.cursor.fetchall()
        return bodegas

    def obtener_bodega_por_nombre(self, nombre):
        query = """
        SELECT b.Nombre_Bodega, b.Capacidad, d.Calle, d.Numero, d.Ciudad, d.Region 
        FROM bodega b
        JOIN direccion d ON b.Direccion_FK = d.ID_Direccion
        WHERE b.Nombre_Bodega = %s
        """
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (nombre,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None


    def agregar_bodega(self, nombre, capacidad, calle, numero, ciudad, region):
        direccion_query = """
        INSERT INTO direccion (Calle, Numero, Ciudad, Region)
        VALUES (%s, %s, %s, %s)
        """
        bodega_query = """
        INSERT INTO bodega (Nombre_Bodega, Direccion_FK, Capacidad)
        VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(direccion_query, (calle, numero, ciudad, region))
            direccion_id = self.cursor.lastrowid
            self.cursor.execute(bodega_query, (nombre, direccion_id, capacidad))
            self.db.commit()
        except mysql.connector.Error as err:
            print(f"Error al agregar bodega: {err}")
            self.db.rollback()

    def modificar_bodega(self, nombre, nuevo_nombre, capacidad, calle, numero, ciudad, region):
        query = """
        UPDATE direccion d
        JOIN bodega b ON b.Direccion_FK = d.ID_Direccion
        SET d.Calle = %s, d.Numero = %s, d.Ciudad = %s, d.Region = %s, b.Nombre_Bodega = %s, b.Capacidad = %s
        WHERE b.Nombre_Bodega = %s
        """
        self.cursor.execute(query, (calle, numero, ciudad, region, nuevo_nombre, capacidad, nombre))
        self.db.commit()


    def agregar_producto(self, nombre, cantidad, ubicacion, precio, descripcion):
        try:
            producto_query = """
            INSERT INTO producto (Nombre_Producto, Descripcion, Precio, Categoria_FK, Estado_FK)
            VALUES (%s, %s, %s, 1, 1)
            """
            self.cursor.execute(producto_query, (nombre, descripcion, precio))
            producto_id = self.cursor.lastrowid

            stock_query = """
            INSERT INTO stock (Producto_FK, Bodega_FK, Cantidad)
            VALUES (%s, (SELECT ID_Bodega FROM bodega WHERE Nombre_Bodega = %s), %s)
            """
            self.cursor.execute(stock_query, (producto_id, ubicacion, cantidad))
            self.db.commit()
        except mysql.connector.Error as err:
            print(f"Error al agregar producto: {err}")
            self.db.rollback()


    def obtener_reporte_inventario(self):
        query = """
        SELECT p.Nombre_Producto, s.Cantidad, c.Nombre_Categoria
        FROM stock s
        JOIN producto p ON s.Producto_FK = p.ID_Producto
        JOIN categoria c ON p.Categoria_FK = c.ID_Categoria
        """
        self.cursor.execute(query)
        reporte_inventario = self.cursor.fetchall()
        return reporte_inventario

    def obtener_reporte_valoracion_bodegas(self):
        query = """
        SELECT b.Nombre_Bodega, v.Puntuacion, v.Comentario
        FROM valoracion v
        JOIN bodega b ON v.Bodega_FK = b.ID_Bodega
        """
        self.cursor.execute(query)
        reporte_valoracion_bodegas = self.cursor.fetchall()
        return reporte_valoracion_bodegas

    def obtener_reporte_stock(self):
        query = """
        SELECT p.Nombre_Producto, s.Cantidad, e.Descripcion_Estado
        FROM stock s
        JOIN producto p ON s.Producto_FK = p.ID_Producto
        JOIN estadoproducto e ON p.Estado_FK = e.ID_Estado
        """
        self.cursor.execute(query)
        reporte_stock = self.cursor.fetchall()
        return reporte_stock

    def descontinuar_producto(self, codigo):
        try:
            delete_product_query = "DELETE FROM producto WHERE ID_Producto = %s"
            self.cursor.execute(delete_product_query, (codigo,))
            self.db.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"Error al descontinuar producto: {err}")
            return False



    # LISTOP
    def modificar_producto(self, codigo, nombre, descripcion, precio, cantidad_stock, categoria, ubicacion):
        query = """
        UPDATE producto
        SET Nombre_Producto = %s, Descripcion = %s, Precio = %s, Cantidad_Stock = %s, Categoria_FK = %s, Ubicacion = %s
        WHERE ID_Producto = %s
        """
        self.cursor.execute(query, (nombre, descripcion, precio, cantidad_stock, categoria, ubicacion, codigo))
        self.db.commit()




    def obtener_producto_por_codigo(self, codigo):
            query = """
            SELECT p.ID_Producto as codigo, p.Nombre_Producto as nombre_producto, 
                p.Descripcion as descripcion, p.Precio as precio, 
                c.Nombre_Categoria as nombre_categoria, 
                e.Descripcion_Estado as estado
            FROM producto p
            JOIN categoria c ON p.Categoria_FK = c.ID_Categoria
            JOIN estadoproducto e ON p.Estado_FK = e.ID_Estado
            WHERE p.ID_Producto = %s
            """
            try:
                self.cursor.execute(query, (codigo,))
                producto = self.cursor.fetchone()
                return producto
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
