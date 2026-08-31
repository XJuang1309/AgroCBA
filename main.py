productos = []

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
    print("7. Salir")
    print("=====================================")

# Permite registrar productos con validaciones
def registrar_producto():
    print("\n=== REGISTRAR PRODUCTO ===")
    codigo = input("Codigo: ").strip()
    if codigo == "":
        print("Error: codigo vacio.\n")
        return
    for p in productos:
        if p["codigo"] == codigo:
            print("Error: codigo duplicado.\n")
            return
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Error: nombre vacio.\n")
        return
    categoria = input("Categoria: ").strip()
    if categoria == "":
        print("Error: categoria vacia.\n")
        return
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            print("Error: cantidad negativa.\n")
            return
    except:
        print("Error: cantidad debe ser numero.\n")
        return
    try:
        precio = float(input("Precio: "))
        if precio <= 0:
            print("Error: precio debe ser mayor que cero.\n")
            return
    except:
        print("Error: precio debe ser numero.\n")
        return
    producto = {"codigo": codigo, "nombre": nombre, "categoria": categoria, "cantidad": cantidad, "precio": precio}
    productos.append(producto)
    print("Producto registrado.\n")

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
            print("Adios!")
            break
        else:
            print("Opcion invalida.\n")

if __name__ == "__main__":
    main()