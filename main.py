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
    pass

def consultar_productos():
    pass

def buscar_producto():
    pass

def actualizar_producto():
    pass

def eliminar_producto():
    pass

def calcular_inventario():
    pass

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()