class Bodega:
    def __init__(self, nombre_bodega, capacidad, calle, numero, ciudad, region):
        self.nombre_bodega = nombre_bodega
        self.capacidad = capacidad
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.region = region

class Producto:
    def __init__(self, nombre_producto, descripcion, precio, categoria, estado):
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.estado = estado
