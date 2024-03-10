### 5. Entrada de habitaciones: Daniel
### 6. Control de variables: Mariana

correo = ""
nombre_casa = ""
casas = ""
contador_casas = 0

while True:
    if correo == "":
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese un correo electrónico: ")
        pin = input("Ingrese un PIN: ")
        print("Usuario registrado exitosamente.")

    opcion = input("\nBienvenido a la aplicación Smart Home\n1. Iniciar sesión\n2. Registrarse\n3. Salir\nSeleccione una opción: ")

    if opcion == "1":
        correo_login = input("Ingrese su correo electrónico: ")
        pin_login = input("Ingrese su PIN: ")
        if correo == correo_login and pin == pin_login:
            print("Inicio de sesión exitoso.")
            while True:
                print("\nMenú principal:")
                print("1. Ver casas registradas")
                print("2. Registrar nueva casa")
                print("3. Salir")
                opcion_menu = input("Seleccione una opción: ")
                if opcion_menu == "1":
                    print("\nCasas registradas:")
                    print (casas)
                    pass
                elif opcion_menu == "2":
                    nombre_casa = input("Ingrese el nombre de la casa: ")
                    contador_casas += 1
                    casas += f"\n{contador_casas}. {nombre_casa}" # Agrega la habitación a la lista
                    print("Casa agregada exitosamente.")
                elif opcion_menu == "3":
                    break
                else:
                    print("Opción inválida. Inténtelo de nuevo.")
        else:
            print("Usuario no encontrado. Por favor, regístrese.")
    if opcion == 2:
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        pin = input("Ingrese un PIN: ")
        print("Usuario registrado exitosamente.")
    elif opcion == "3":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")