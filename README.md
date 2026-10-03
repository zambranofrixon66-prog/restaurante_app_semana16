```markdown
# Restaurante App - Semana 16

**Estudiante:** Frixon Jeancarlos Zambrano Ortiz  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 16  

## Propósito

En la Semana 16 se continuó con la evolución de la aplicación `restaurante_app`, manteniendo la arquitectura y las funcionalidades desarrolladas en semanas anteriores e incorporando la gestión completa de usuarios mediante manejo de eventos en `Tkinter`.

El objetivo principal fue permitir al usuario con rol Administrador registrar, consultar, actualizar y eliminar usuarios, utilizando controles como `Treeview`, `Combobox`, botones y eventos de teclado. Además, se mantuvo la persistencia de los datos en archivos `JSON` y la separación de responsabilidades entre modelos, servicios e interfaz gráfica.

## Estructura del Proyecto

```text
restaurante_app/
├── assets/
│   └── logo.png
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Descripción de la Estructura

* `assets/`: almacena los recursos gráficos de la aplicación, como el logotipo.
* `datos/`: contiene los archivos `JSON` utilizados para la persistencia de productos, usuarios y ventas.
* `modelos/`: contiene las clases `Producto`, `Usuario` y `Venta`.
* `servicios/`: concentra la lógica del negocio, validaciones y operaciones sobre los datos.
* `ui/`: contiene las vistas de autenticación y la interfaz principal.
* `main.py`: funciona como punto de entrada de la aplicación.
* `README.md`: documenta la evolución del proyecto correspondiente a la Semana 16.

## Funcionalidades Conservadas de Semanas Anteriores

El sistema mantiene las funciones desarrolladas previamente:

* Autenticación de usuarios.
* Gestión de productos.
* Registro de ventas.
* Descuento automático de stock.
* Persistencia de productos, usuarios y ventas en archivos `JSON`.
* Navegación mediante menú lateral.
* Uso de recursos visuales almacenados en `assets/`.

## Gestión de Usuarios - Semana 16

En esta semana se incorporó una sección completa para la administración de usuarios.

El módulo permite:

* Registrar nuevos usuarios.
* Consultar los usuarios existentes.
* Actualizar el nombre, contraseña y rol de un usuario.
* Eliminar usuarios.
* Evitar que el usuario que tiene una sesión activa elimine su propia cuenta.
* Mantener los cambios guardados en `datos/usuarios.json`.

Los roles utilizados en el sistema son:

* `Administrador`
* `Empleado`
* `Cliente`

El formulario de gestión se muestra al usuario con rol `Administrador`, mientras que los demás perfiles mantienen acceso limitado de acuerdo con la estructura del sistema.

## Manejo de Eventos en Tkinter

La gestión de usuarios incorpora diferentes mecanismos de interacción basados en eventos:

### `<<TreeviewSelect>>`

Al seleccionar un usuario en la tabla, se ejecuta un callback que obtiene el usuario seleccionado y carga automáticamente sus datos en el formulario.

### `<<ComboboxSelected>>`

Permite detectar el cambio de rol realizado mediante el `Combobox` y mostrar información relacionada con el rol seleccionado.

### `<Return>`

La tecla Enter funciona como atajo para ejecutar la acción principal del formulario, permitiendo registrar o confirmar una modificación según el estado actual.

### `<Escape>`

La tecla Escape limpia los campos del formulario y elimina la selección realizada en el `Treeview`.

### `command=`

Los botones Registrar, Actualizar, Eliminar y Limpiar utilizan `command=` para enlazar las acciones de la interfaz con sus callbacks correspondientes.

## Interfaz de Gestión de Usuarios

La sección de usuarios contiene:

* Campo Usuario.
* Campo Nombre.
* Campo Contraseña.
* Selector de Rol mediante `ttk.Combobox`.
* Botón Registrar.
* Botón Actualizar.
* Botón Eliminar.
* Botón Limpiar.
* Tabla `ttk.Treeview` para mostrar los usuarios registrados.
* Barra de desplazamiento vertical.

Por seguridad, la contraseña no se muestra dentro del `Treeview`.

## Separación de Responsabilidades

Se mantiene la arquitectura modular del proyecto:

* La capa de interfaz gráfica captura las acciones del usuario, administra los eventos y actualiza los componentes visuales.
* `RestauranteServicio` se encarga de las validaciones y operaciones relacionadas con usuarios, productos y ventas.
* Los modelos representan los datos del sistema.
* Los archivos `JSON` permiten mantener la información entre diferentes ejecuciones de la aplicación.

De esta manera, la lógica de negocio no se encuentra directamente dentro de los eventos visuales, facilitando el mantenimiento del sistema.

## Persistencia de Usuarios

Los usuarios se almacenan en:

```text
datos/usuarios.json
```

Cada usuario contiene la siguiente información:

```json
{
    "username": "admin",
    "password": "123",
    "nombre": "Administrador General",
    "rol": "Administrador"
}
```

Cuando se registra, actualiza o elimina un usuario, el archivo se actualiza para conservar los cambios.

## Tecnologías Utilizadas

* `Python`
* `Tkinter`
* `ttk`
* `Treeview`
* `Combobox`
* `JSON`
* Programación Orientada a Objetos
* Git
* GitHub

## Ejecución

Para ejecutar el sistema desde la carpeta principal del proyecto:

```bash
python main.py
```

## Conclusión

Durante la Semana 16 se amplió la funcionalidad de `restaurante_app` mediante la implementación de la gestión de usuarios basada en eventos. La incorporación de operaciones de registro, consulta, actualización y eliminación permitió fortalecer el módulo administrativo del sistema.

El uso de eventos como `<<TreeviewSelect>>`, `<<ComboboxSelected>>`, `<Return>` y `<Escape>` mejoró la interacción con la interfaz, mientras que la separación entre la vista y `RestauranteServicio` permitió conservar una arquitectura organizada y reutilizable. Además, la persistencia en `usuarios.json` garantiza que los cambios realizados se mantengan entre sesiones.
```