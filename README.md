<<<<<<< HEAD
# AgroCBA
=======
# AgroCBA - Sistema de Gestión de Productos Agropecuarios

## Descripción
Aplicación monolítica desarrollada en Python que permite gestionar productos de una unidad productiva agropecuaria. 
El sistema implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con validaciones robustas de datos.
Incluye control de versiones con Git para el seguimiento de cambios durante el desarrollo.

## Institución
Centro de Biotecnología Agropecuaria (CBA) - SENA Mosquera
Programa: Tecnólogo en Análisis y Desarrollo de Software (ADSO)
Ficha: 3409610

## Propósito Formativo
Integrar fundamentos de programación en Python con buenas prácticas iniciales de control de versiones:
cambios pequeños, commits significativos, consulta de historial y trabajo básico con ramas.

## Funcionalidades Principales

### 1. Registrar Producto (Opción 1)
Permite registrar un nuevo producto con los siguientes datos:
- **Código**: Identificador único (texto, no puede estar vacío ni duplicado)
- **Nombre**: Descripción del producto (texto, no puede estar vacío)
- **Categoría**: Clasificación del producto (texto, no puede estar vacío)
- **Cantidad**: Unidades disponibles (número entero >= 0)
- **Precio**: Costo unitario (número > 0)

### 2. Consultar Productos (Opción 2)
Muestra todos los productos registrados en el sistema o informa si no hay registros.

### 3. Buscar Producto (Opción 3)
Busca un producto específico por su código y muestra todos sus datos.

### 4. Actualizar Producto (Opción 4)
Permite modificar nombre, categoría, cantidad y/o precio de un producto existente.
El código se conserva como identificador.

### 5. Eliminar Producto (Opción 5)
Elimina un producto del registro.
Solicita confirmación antes de ejecutar la acción.

### 6. Calcular Valor Total del Inventario (Opción 6)
Calcula la suma de (cantidad × precio) para todos los productos registrados.

### 7. Salir (Opción 7)
Finaliza el programa de forma controlada.

## Validaciones Obligatorias

✓ El código no puede quedar vacío y no debe repetirse.
✓ El nombre y la categoría no pueden quedar vacíos.
✓ La cantidad debe ser un número entero mayor o igual a cero.
✓ El precio debe ser numérico y mayor que cero.
✓ Una opción inválida del menú no debe cerrar el programa.
✓ Las búsquedas, actualizaciones y eliminaciones informan cuando el producto no existe.

## Tecnologías Utilizadas
- **Python 3.x**: Lenguaje de programación
- **Git**: Sistema de control de versiones
- **Estructuras de datos**: Listas y diccionarios

## Requisitos del Sistema
- Python 3.6 o superior instalado
- Git instalado (para control de versiones)
- Terminal o consola de comandos

## Instrucciones de Ejecución

### 1. Clonar o descargar el proyecto
```bash
cd agrocba
```

### 2. Ejecutar la aplicación
```bash
python main.py
```

### 3. Usar el menú
- Ingresa el número de la opción deseada (1-7)
- Sigue las indicaciones en pantalla
- Ingresa los datos solicitados

## Estructura del Proyecto
AgroCBA/
├── main.py # Código fuente principal con todas las funcionalidades
├── README.md # Documentación del proyecto (este archivo)
├── .gitignore # Archivo para excluir archivos temporales de Git
└── .git/ # Repositorio Git (creado automáticamente con git init)


### Ejemplo de Uso

```text
=====================================
        SISTEMA AGROCBA
=====================================

1. Registrar producto
2. Consultar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Mostrar valor total del inventario
7. Salir

=====================================

Opcion: 1

=== REGISTRAR PRODUCTO ===

Codigo: P001
Nombre: Fertilizante
Categoria: Insumos
Cantidad: 15
Precio: 35000
```
Producto registrado correctamente.

## Historial Git

El proyecto utiliza Git para registrar cada cambio realizado:

### Ver el historial de commits
```bash
git log --oneline
```

### Ver cambios específicos entre versiones
```bash
git diff <commit_anterior> <commit_nuevo>
```

### Ver la rama actual
```bash
git branch
```

## Commits Realizados

1. Inicio del proyecto AgroCBA
2. Implementa registro de productos
3. Implementa consulta de productos
4. Implementa busqueda de productos
5. Implementa actualizacion de productos
6. Implementa eliminacion de productos
7. Agrega calculo del valor total del inventario
8. Mejora validaciones de productos
9. Agrega README con documentacion completa

## Rama de Mejoras

Se creó una rama independiente `mejora-validaciones` para implementar validaciones robustas antes de integrar cambios a la rama principal `main`.

## Pruebas Realizadas

- ✓ Registrar producto con datos válidos
- ✓ Rechazar código duplicado
- ✓ Rechazar cantidad negativa
- ✓ Rechazar precio cero o negativo
- ✓ Buscar producto inexistente
- ✓ Actualizar producto existente
- ✓ Cancelar eliminación de producto
- ✓ Calcular inventario correctamente
- ✓ Manejar opciones inválidas del menú

## Notas de Desarrollo

- La aplicación utiliza una estructura monolítica donde toda la lógica se concentra en un único archivo `main.py`.
- Los datos se almacenan en memoria usando una lista de diccionarios.
- Los cambios no se persisten al cerrar la aplicación (se pierden si no se guarda en archivo).

## Autor

**JUAN SEBASTIAN GARCIA** - SENA ADSO Ficha 3409610

Centro de Biotecnología Agropecuaria (CBA)

Mosquera, Colombia

---

# AgroCBA

>>>>>>> 51d0eb4 (Agrega README completo)
