class Producto:
    def __init__(self, id_producto: str, nombre: str, categoria: str, precio: float, stock: int):
        self.id_producto = str(id_producto).strip()
        self.nombre = str(nombre).strip()
        self.categoria = str(categoria).strip()
        self.precio = float(precio)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Lee id_producto o id si viene del formato anterior
        id_val = data.get("id_producto") if "id_producto" in data else data.get("id", "")
        return cls(
            id_producto=str(id_val),
            nombre=data.get("nombre", ""),
            categoria=data.get("categoria", ""),
            precio=data.get("precio", 0.0),
            stock=data.get("stock", 0)
        )