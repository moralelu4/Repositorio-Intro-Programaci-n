
### 2. Entrada de registro de usuarios: Fabián
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