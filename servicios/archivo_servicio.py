import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta: str) -> list:
        if not os.path.exists(ruta):
            try:
                os.makedirs(os.path.dirname(ruta), exist_ok=True)
                with open(ruta, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)
            except Exception:
                pass
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def guardar_json(ruta: str, datos: list) -> bool:
        try:
            directorio = os.path.dirname(ruta)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False

    # Métodos alias por compatibilidad con versiones previas
    @classmethod
    def guardar_datos(cls, ruta: str, datos: list) -> bool:
        return cls.guardar_json(ruta, datos)

    @classmethod
    def leer_datos(cls, ruta: str) -> list:
        return cls.leer_json(ruta)