productos = []
c
def mostrar_menu():
    print("=====================================")
    print("      SISTEMA AGROCBA")
    print("=====================================")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar valor total del inventario")
    print("7. Total de unidades existentes")
    print("8. Producto de mayor precio")
    print("9. Producto con mayor cantidad")
    print("10. Consultar por categoria")
    print("11. Ordenar productos alfabeticamente")
    print("12. Productos con bajo inventario")
    print("13. Guardar datos en JSON")
    print("14. Salir")
    print("=====================================")

# Permite registrar productos con validaciones
def registrar_producto():
    print("\n=== REGISTRAR PRODUCTO ===")
    
    # Validar codigo no vacio
    codigo = input("Codigo: ").strip()
    if codigo == "":
        print("Error: codigo no puede estar vacio.\n")
        return
    
    # Validar codigo no duplicado
    for p in productos:
        if p["codigo"] == codigo:
            print("Error: codigo ya existe.\n")
            return
    
    # Validar nombre no vacio
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Error: nombre no puede ser vacio.\n")
        return
    
    # Validar categoria no vacia
    categoria = input("Categoria: ").strip()
    if categoria == "":
        print("Error: categoria no puede ser vacia.\n")
        return
    
    # Validar cantidad >= 0
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            print("Error: cantidad no puede ser negativa.\n")
            return
    except ValueError:
        print("Error: cantidad debe ser numero entero.\n")
        return
    
    # Validar precio > 0
    try:
        precio = float(input("Precio: "))
        if precio <= 0:
            print("Error: precio debe ser mayor que cero.\n")
            return
    except ValueError:
        print("Error: precio debe ser numero.\n")
        return
    
    producto = {"codigo": codigo, "nombre": nombre, "categoria": categoria, "cantidad": cantidad, "precio": precio}
    productos.append(producto)
    print("Producto registrado correctamente.\n")

# Muestra todos los productos registrados
def consultar_productos():
    print("\n=== CONSULTAR PRODUCTOS ===")
    if len(productos) == 0:
        print("No hay productos.\n")
    else:
        for i, p in enumerate(productos):
            print(f"{i+1}. Codigo: {p['codigo']}")
            print(f"   Nombre: {p['nombre']}")
            print(f"   Categoria: {p['categoria']}")
            print(f"   Cantidad: {p['cantidad']}")
            print(f"   Precio: {p['precio']}")
            print()

# Busca producto por codigo            
def buscar_producto():
    print("\n=== BUSCAR PRODUCTO ===")
    codigo = input("Codigo: ").strip()
    encontrado = False
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Categoria: {p['categoria']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}\n")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.\n")

# Actualiza datos del producto
def actualizar_producto():
    print("\n=== ACTUALIZAR PRODUCTO ===")
    codigo = input("Codigo: ").strip()
    for p in productos:
        if p["codigo"] == codigo:
            nombre = input("Nombre (Enter no cambiar): ").strip()
            if nombre != "":
                p["nombre"] = nombre
            categoria = input("Categoria (Enter no cambiar): ").strip()
            if categoria != "":
                p["categoria"] = categoria
            cantidad = input("Cantidad (Enter no cambiar): ").strip()
            if cantidad != "":
                try:
                    p["cantidad"] = int(cantidad)
                except:
                    print("Error: cantidad debe ser numero.\n")
                    return
            precio = input("Precio (Enter no cambiar): ").strip()
            if precio != "":
                try:
                    p["precio"] = float(precio)
                except:
                    print("Error: precio debe ser numero.\n")
                    return
            print("Producto actualizado.\n")
            return
    print("Producto no encontrado.\n")

# Elimina un producto con confirmacion
def eliminar_producto():
    print("\n=== ELIMINAR PRODUCTO ===")
    codigo = input("Codigo: ").strip()
    for i, p in enumerate(productos):
        if p["codigo"] == codigo:
            confirmacion = input("Confirma? (s/n): ").strip()
            if confirmacion == "s":
                productos.pop(i)
                print("Producto eliminado.\n")
            else:
                print("Cancelado.\n")
            return
    print("Producto no encontrado.\n")

# Calcula el valor total del inventario
def calcular_inventario():
    print("\n=== VALOR TOTAL DEL INVENTARIO ===")
    total = 0
    for p in productos:
        try:
            cantidad = int(p["cantidad"])
            precio = float(p["precio"])
            subtotal = cantidad * precio
            total = total + subtotal
        except:
            print(f"Error al calcular {p['codigo']}")
    print(f"Valor total: {total}\n")

def total_unidades():
    print("\n=== TOTAL DE UNIDADES ===")
    total = 0
    for p in productos:
        total = total + int(p["cantidad"])
    print(f"Total de unidades: {total}\n")

def mayor_precio():
    print("\n=== PRODUCTO DE MAYOR PRECIO ===")
    if len(productos) == 0:
        print("No hay productos.\n")
        return
    
    mayor = productos[0]
    for p in productos:
        if float(p["precio"]) > float(mayor["precio"]):
            mayor = p
    
    print(f"Codigo: {mayor['codigo']}")
    print(f"Nombre: {mayor['nombre']}")
    print(f"Precio: {mayor['precio']}\n")

def mayor_cantidad():
    print("\n=== PRODUCTO CON MAYOR CANTIDAD ===")
    if len(productos) == 0:
        print("No hay productos.\n")
        return
    
    mayor = productos[0]
    for p in productos:
        if int(p["cantidad"]) > int(mayor["cantidad"]):
            mayor = p
    
    print(f"Codigo: {mayor['codigo']}")
    print(f"Nombre: {mayor['nombre']}")
    print(f"Cantidad: {mayor['cantidad']}\n")

def consultar_categoria():
    print("\n=== CONSULTAR POR CATEGORIA ===")
    categoria = input("Categoria a buscar: ").strip()
    
    encontrados = []
    for p in productos:
        if p["categoria"].lower() == categoria.lower():
            encontrados.append(p)
    
    if len(encontrados) == 0:
        print("No hay productos en esa categoria.\n")
    else:
        for p in encontrados:
            print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}")
        print()

def ordenar_alfabeticamente():
    print("\n=== PRODUCTOS ORDENADOS ALFABETICAMENTE ===")
    if len(productos) == 0:
        print("No hay productos.\n")
        return
    
    ordenados = sorted(productos, key=lambda x: x["nombre"])
    for p in ordenados:
        print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}")
    print()

def bajo_inventario():
    print("\n=== PRODUCTOS CON BAJO INVENTARIO (<=5) ===")
    bajos = []
    for p in productos:
        if int(p["cantidad"]) <= 5:
            bajos.append(p)
    
    if len(bajos) == 0:
        print("No hay productos con bajo inventario.\n")
    else:
        for p in bajos:
            print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Cantidad: {p['cantidad']}")
        print()

def guardar_json():
    import json
    print("\n=== GUARDAR EN JSON ===")
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=2)
    print("Datos guardados en productos.json\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            calcular_inventario()
        elif opcion == "7":
            total_unidades()
        elif opcion == "8":
            mayor_precio()
        elif opcion == "9":
            mayor_cantidad()
        elif opcion == "10":
            consultar_categoria()
        elif opcion == "11":
            ordenar_alfabeticamente()
        elif opcion == "12":
            bajo_inventario()
        elif opcion == "13":
            guardar_json()
        elif opcion == "14":
            print("Adios!")
            break
        else:
            print("Opcion invalida.\n")

if __name__ == "__main__":
    main()
