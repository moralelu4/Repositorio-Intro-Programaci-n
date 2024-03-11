correo = ""
nombre_casa = ""
casas = ""
contador_casas = 0
habitaciones ="1. Cuarto principal\n 2.Sala de estar\n3. Cocina\n4. Garaje"
contador_habitaciones = 4

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
            modo_usuario = True
            while modo_usuario == True:
                print("\nMenú principal:")
                print("1. Ver casas registradas")
                print("2. Registrar nueva casa")
                print("3. Salir")
                opcion_menu = int(input("Seleccione una opción: "))
                if opcion_menu == 1:
                    if casas != "":
                            print("\nCasas registradas:")
                            print (casas)
                            casa =int(input("Seleccione una casa: "))
                            if casa in range (1,contador_casas+1):
                                modo_casa = True
                                while modo_casa == True:
                                    print("¡Bienvenido a la casa!")
                                    print("1. Seleccionar habitación")
                                    print("2. Añadir nueva habitación")
                                    print("3. Salir")
                                    opcion_habitacion = int(input ("\nSeleccione una acción: "))
                                    if opcion_habitacion == 1:
                                        print(habitaciones)
                                    elif opcion_habitacion == 2:
                                        nombre_habitacion = input("Ingrese el nombre de la habitación: ")
                                        contador_habitaciones += 1
                                        habitaciones += f"\n{contador_habitaciones}. {nombre_habitacion}" # Agrega la habitación a la lista
                                        print("Habitación agregada exitosamente.")
                                    elif opcion_habitacion == 3:
                                        modo_casa = False
                                        break
                            else:
                                print("Por favor, ingrese una casa válida")

                    else:
                        print ("No hay casas registradas. Por favor, ingrese una nueva.")
                    
                elif opcion_menu == 2:
                    nombre_casa = input("Ingrese el nombre de la casa: ")
                    contador_casas += 1
                    casas += f"\n{contador_casas}. {nombre_casa}" # Agrega la habitación a la lista
                    print("Casa agregada exitosamente.")
                elif opcion_menu == 3:
                    modo_usuario = False
                else:
                    print("Opción inválida. Por favor, seleccione una correcta.")
        else:
            print("Usuario no encontrado. Por favor, regístrese.")
    elif opcion == "2":
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        pin = input("Ingrese un PIN: ")
        print("Usuario registrado exitosamente.")
    elif opcion == "3":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")