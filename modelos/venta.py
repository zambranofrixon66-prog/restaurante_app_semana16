class Venta:
    def __init__(self, id_venta, id_usuario, nombre_usuario, id_producto, nombre_producto, precio, fecha):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = float(precio)
        self.fecha = fecha

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "precio": self.precio,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_venta=data.get("id_venta", ""),
            id_usuario=data.get("id_usuario", ""),
            nombre_usuario=data.get("nombre_usuario", ""),
            id_producto=data.get("id_producto", ""),
            nombre_producto=data.get("nombre_producto", ""),
            precio=data.get("precio", 0.0),
            fecha=data.get("fecha", "")
        )