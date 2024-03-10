
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
