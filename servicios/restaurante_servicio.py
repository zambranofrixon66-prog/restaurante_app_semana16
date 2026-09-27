import os
import json
from datetime import datetime
from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.ruta_datos = "datos"
        self.archivo_usuarios = os.path.join(self.ruta_datos, "usuarios.json")
        self.archivo_productos = os.path.join(self.ruta_datos, "productos.json")
        self.archivo_ventas = os.path.join(self.ruta_datos, "ventas.json")

        self.usuarios = []
        self.productos = []
        self.ventas = []

        self.cargar_datos()

    def cargar_datos(self):
        os.makedirs(self.ruta_datos, exist_ok=True)
        self._cargar_usuarios()
        self._cargar_productos()
        self._cargar_ventas()

    def _cargar_usuarios(self):
        if os.path.exists(self.archivo_usuarios):
            try:
                with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    self.usuarios = [Usuario.from_dict(u) for u in datos]
            except Exception:
                self.usuarios = []
        else:
            self.usuarios = []

    def _cargar_productos(self):
        if os.path.exists(self.archivo_productos):
            try:
                with open(self.archivo_productos, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    self.productos = [Producto.from_dict(p) for p in datos]
            except Exception:
                self.productos = []
        else:
            self.productos = []

    def _cargar_ventas(self):
        if os.path.exists(self.archivo_ventas):
            try:
                with open(self.archivo_ventas, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    self.ventas = [Venta.from_dict(v) for v in datos]
            except Exception:
                self.ventas = []
        else:
            self.ventas = []

    def guardar_productos(self):
        try:
            with open(self.archivo_productos, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    def guardar_ventas(self):
        try:
            with open(self.archivo_ventas, "w", encoding="utf-8") as f:
                json.dump([v.to_dict() for v in self.ventas], f, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    def autenticar(self, username, password):
        for u in self.usuarios:
            if getattr(u, 'username', '') == username and getattr(u, 'password', '') == password:
                return u
        return None

    def obtener_usuarios(self):
        return self.usuarios

    def buscar_usuario_por_id(self, id_usuario):
        for u in self.usuarios:
            uid = getattr(u, 'id_usuario', getattr(u, 'id', getattr(u, 'username', '')))
            if str(uid) == str(id_usuario):
                return u
        return None

    def obtener_productos(self):
        return self.productos

    def buscar_producto_por_id(self, id_producto):
        for p in self.productos:
            if str(p.id_producto) == str(id_producto):
                return p
        return None

    def crear_producto(self, producto):
        if self.buscar_producto_por_id(producto.id_producto):
            return False, "Ya existe un producto con ese código."
        self.productos.append(producto)
        self.guardar_productos()
        return True, "Producto registrado exitosamente."

    def actualizar_producto(self, producto):
        p_existente = self.buscar_producto_por_id(producto.id_producto)
        if not p_existente:
            return False, "Producto no encontrado para actualizar."
        p_existente.nombre = producto.nombre
        p_existente.categoria = producto.categoria
        p_existente.precio = producto.precio
        p_existente.stock = producto.stock
        self.guardar_productos()
        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, id_producto):
        p_existente = self.buscar_producto_por_id(id_producto)
        if not p_existente:
            return False, "Producto no encontrado."
        self.productos.remove(p_existente)
        self.guardar_productos()
        return True, "Producto eliminado correctamente."

    def obtener_ventas(self):
        return self.ventas

    def registrar_venta(self, id_usuario, id_producto):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            return False, "El usuario seleccionado no existe."

        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, "El producto seleccionado no existe."

        if producto.stock <= 0:
            return False, f"Sin stock disponible para '{producto.nombre}'."

        producto.stock -= 1

        nuevo_id = f"V-{len(self.ventas) + 1:04d}"
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nombre_u = getattr(usuario, 'nombre', str(usuario))
        uid = getattr(usuario, 'id_usuario', getattr(usuario, 'id', getattr(usuario, 'username', '')))

        nueva_venta = Venta(
            id_venta=nuevo_id,
            id_usuario=uid,
            nombre_usuario=nombre_u,
            id_producto=producto.id_producto,
            nombre_producto=producto.nombre,
            precio=producto.precio,
            fecha=fecha_actual
        )

        self.ventas.append(nueva_venta)
        self.guardar_ventas()
        self.guardar_productos()

        return True, nueva_venta