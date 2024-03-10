
### 3. Inicio de sesión de usuario: Anderson
### 4. Control de casas: Luis
### 5. Entrada de habitaciones: Daniel
### 6. Control de variables: Mariana

while True:
    opcion = input("\nBienvenido a la aplicación Smart Home\n1. Iniciar sesión\n2. Registrarse\n3. Salir\nSeleccione una opción: ")

    if opcion == "1":
        print("Opción de inicio de sesión")
    elif opcion == "2":
        print("Opción de registro de usuario")
        break
    elif opcion == "3":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
        
correo = ""
while True:
    if correo == "":
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese un correo electrónico: ")
        pin = input("Ingrese un PIN: ")
        print("Usuario registrado exitosamente.")

    opcion = input("\nBienvenido a la aplicación Smart Home\n1. Iniciar sesión\n2. Registrarse\n3. Salir\nSeleccione una opción: ")

    if opcion == "1":
        print("Opción de inicio de sesión.")
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
            print("Entrada a casas.")
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
        

 ### TO-DO LIST: ###
        # 1. Estaría interesante poder validar los correos (de momento, cualquier string pasa como correo).
        # 2. Orden en el caso de las casas: 1. Casa. 2. Habitación. 3. (ya para siguiente entrega) dispositivos (Párrafos 6 y 7 de las instrucciones). Falta la parte de registrar la habitación.
