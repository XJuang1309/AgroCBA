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

def registrar_producto():
    print("\n=== REGISTRAR PRODUCTO ===")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }
    
    productos.append(producto)
    print("Producto registrado.\n")

def consultar_productos():
    print("\n=== CONSULTAR PRODUCTOS ===")
    if len(productos) == 0:
        print("No hay productos registrados.\n")
    else:
        for p in productos:
            print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Categoria: {p['categoria']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}")
    print()

def buscar_producto():
    print("\n=== BUSCAR PRODUCTO ===")
    codigo = input("Codigo a buscar: ")
    encontrado = False
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Categoria: {p['categoria']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}\n")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.\n")

def actualizar_producto():
    print("\n=== ACTUALIZAR PRODUCTO ===")
    codigo = input("Codigo del producto a actualizar: ")
    for p in productos:
        if p["codigo"] == codigo:
            print("Deja los campos en blanco para no cambiar")
            nombre = input("Nombre: ")
            categoria = input("Categoria: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")
            
            if nombre != "":
                p["nombre"] = nombre
            if categoria != "":
                p["categoria"] = categoria
            if cantidad != "":
                p["cantidad"] = cantidad
            if precio != "":
                p["precio"] = precio
            
            print("Producto actualizado.\n")
            return
    print("Producto no encontrado.\n")

def eliminar_producto():
    print("\n=== ELIMINAR PRODUCTO ===")
    codigo = input("Codigo del producto a eliminar: ")
    for i, p in enumerate(productos):
        if p["codigo"] == codigo:
            confirmacion = input("Confirma eliminacion? (s/n): ")
            if confirmacion == "s":
                productos.pop(i)
                print("Producto eliminado.\n")
            else:
                print("Eliminacion cancelada.\n")
            return
    print("Producto no encontrado.\n")

def calcular_inventario():
    print("\n=== VALOR TOTAL DEL INVENTARIO ===")
    total = 0
    for p in productos:
        try:
            cantidad = float(p["cantidad"])
            precio = float(p["precio"])
            total = total + (cantidad * precio)
        except:
            pass
    print(f"Valor total: {total}\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
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
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida.\n")

if __name__ == "__main__":
    main()