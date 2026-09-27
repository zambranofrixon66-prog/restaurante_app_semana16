class Usuario:
    def __init__(self, username, password, nombre, rol="Personal"):
        self.username = str(username).strip()
        self.password = str(password).strip()
        self.nombre = str(nombre).strip()
        self.rol = str(rol).strip()

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data: dict):
        return Usuario(
            username=data.get("username", ""),
            password=data.get("password", ""),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "Personal")
        )