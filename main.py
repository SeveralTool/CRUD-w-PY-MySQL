# Menu principal del CRUD

def menu_main():
    print("|| MENU PRINCIPAL ||")
    print("1- Listar clientes")
    print("2- Ingresar Clientes")
    print("3- Borrar Clientes")
    print("4- Actualizar Clientes")
    print("5- Salir")
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion <1 or opcion >5:
        return "Ingrese una opcion correcta..."
    elif opcion == 5:
        exit
    elif opcion == 4:
        opcion(opcion)
    elif opcion == 3:
        opcion(opcion)
    elif opcion == 2:
        opcion(opcion)
    elif opcion == 1:
        opcion(opcion)
    else:
        return "Seleccion invalida..."
        menu_main()
    
    
    def opcion(opcion):
        print(opcion)
    
    
    
menu_main()
    