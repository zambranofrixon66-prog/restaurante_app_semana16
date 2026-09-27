```markdown
# Restaurante App - Semana 15

**Estudiante:** Frixon Jeancarlos Zambrano Ortiz  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 15  

## Propósito

En esta semana se realizó la evolución de la aplicación `restaurante_app` mediante la implementación del **Módulo de Ventas** y el **Manejo de Eventos** en la interfaz gráfica utilizando `Tkinter` y `ttk`.

El objetivo principal fue incorporar la gestión de transacciones comerciales al sistema, permitiendo registrar ventas vinculando usuarios y productos existentes, con afectación automática del inventario (stock) y persistencia independiente en archivos `JSON`. Se mantuvo de forma estricta la separación de responsabilidades en capas y el enlace desacoplado de eventos visuales.

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

* `assets/`: almacena recursos gráficos como logotipos o elementos visuales de la aplicación.
* `datos/`: almacena los archivos `JSON` (`productos.json`, `usuarios.json` y `ventas.json`) garantizando la persistencia desacoplada de la información.
* `modelos/`: define las clases entidad del sistema (`Producto`, `Usuario` y la nueva entidad `Venta`), junto con sus métodos de serialización y deserialización de diccionarios.
* `servicios/`: contiene la lógica del negocio (`RestauranteServicio`) y la gestión de archivos (`ArchivoServicio`), coordinando validaciones, reglas de venta y descuento de inventario.
* `ui/`: contiene las vistas del sistema (`LoginView` para autenticación y `MainView` para la gestión modular con pestañas).
* `main.py`: punto de entrada que inicia la aplicación y gestiona el flujo de vistas.
* `README.md`: documentación completa del proyecto correspondiente a la Semana 15.

## Mejoras Incorporadas en la Interfaz (Semana 15)

La interfaz principal (`MainView`) incorporó una nueva pestaña y elementos de control interactivo:

1. **Nueva Pestaña en `ttk.Notebook` (Registro de Ventas):** Área dedicada exclusivamente al proceso de transacciones comerciales y consulta de historial.
2. **Selectores Dinámicos con `ttk.Combobox`:** Listas desplegables configuradas en modo solo lectura (`readonly`) que muestran los clientes activos y los productos con sus existencias disponibles.
3. **Manejo de Eventos (`command=` sin invocación inmediata):** Enlace del botón "Registrar Venta" mediante referencia limpia a función (`command=self.callback_registrar_venta`), asegurando que la acción se ejecute únicamente cuando el usuario presiona el control.
4. **Tabla de Historial con `ttk.Treeview`:** Visualización tabular estructurada en columnas (ID Venta, Cliente, Producto, Precio y Fecha) acompañada de su barra de desplazamiento vertical (`Scrollbar`).
5. **Actualización Reactiva de Controles:** Al confirmar una transacción exitosa, la interfaz refresca simultáneamente la tabla histórica de ventas, el catálogo de productos y los valores de los selectores desplegables.

## Operaciones Implementadas sobre Ventas

El proceso de venta se ejecuta desde la vista y delega toda la lógica a `RestauranteServicio`:

* **Selección de Participantes:** Captura del identificador del cliente y del producto seleccionado en las listas desplegables.
* **Validación de Existencia y Stock:** El servicio comprueba que ambos elementos existan y que el producto disponga de al menos una unidad en inventario antes de procesar la orden.
* **Generación de Registro:** Se crea la instancia de la clase `Venta` asignándole un código identificador único y la marca de fecha/hora del sistema.
* **Descuento de Stock:** Se disminuye automáticamente en una unidad la cantidad disponible del producto adquirido.
* **Persistencia Inmediata:** La transacción se guarda en `datos/ventas.json` y los cambios de stock se actualizan en `datos/productos.json`.

## Separación de Responsabilidades y Persistencia

Se preservó estrictamente la arquitectura modular del sistema:

* La capa **UI** (`MainView`) captura las selecciones, maneja cuadros de diálogo informativos/de error y solicita la actualización de los componentes visuales.
* La capa de **Servicios** (`RestauranteServicio`) ejecuta las validaciones de negocio, calcula identificadores y coordina la persistencia sin acoplarse a elementos gráficos.
* La persistencia en `ventas.json` y `productos.json` se realiza de manera independiente mediante `ArchivoServicio`, garantizando la integridad de las transacciones entre sesiones.

## Tecnologías Utilizadas

* `Python`
* `Tkinter` / `ttk` (`Notebook`, `LabelFrame`, `Treeview`, `Combobox`, `Scrollbar`, `Button`, `Entry`, `Label`)
* `JSON` (Persistencia de datos)
* `Programación Orientada a Objetos` (POO)
* `Git` y `GitHub`

## Conclusión

Con las implementaciones de la Semana 15, `restaurante_app` completó el ciclo operativo del negocio integrando el módulo de ventas y el control riguroso de eventos. La conexión fluida entre la captura de acciones del usuario, la validación de inventario y la persistencia de transacciones reafirma una estructura de software mantenible, robusta y alineada a las buenas prácticas de diseño orientado a objetos.