habitaciones = []
usuarios = []

# Estructura potencial: usuarios -> [[usuario], [usuario], [usuario]]
# Estructura potencial de lista usuario = [nombreusuario,correousuario,pinusuario, [casas]]
# Estructura potencial de lista casas = [nombrecasa, [nombrehabitacion [nombredispositivo,estadodispositivo]], [casa2, [habitacion, [nombredispositivo, estadodispositivo]]]]

### TO-DO:
### 1. Limpiar prints y comments de debugging. Encargado: Fabián
### 2. Cargar diagrama de flujo. Encargado: Jordi.

def agregar_usuario():
    nombre = input("Ingrese su nombre: ")
    while True:
        correo = input("Ingrese un correo electrónico: ")
        if "@" not in correo or "." not in correo:
            print ("Correo electrónico inválido. Por favor, ingrese un correo electrónico válido.")
        else:
            break
    pin = input("Ingrese un PIN: ")
    usuarios.append([nombre,correo,pin,[]])
    print("Usuario registrado exitosamente.")

def agregarCasa(listaCasas):
    nombre_casa = input("Ingrese el nombre de la casa: ")
    listaCasas.append([nombre_casa,[]])
    print(listaCasas)
    print("Casa agregada exitosamente.")

def eliminarCasa(listaCasas):
    if listaCasas != []:
        for casa in listaCasas:
            print(f"{listaCasas.index(casa)+1}. {casa [0]}")
        seleccionCasaPorBorrar = int(input("Por favor, seleccione cuál casa desea eliminar: "))
        CasaABorrar = listaCasas [seleccionCasaPorBorrar-1]
        if seleccionCasaPorBorrar in range (1,len(listaCasas)+1):
            print (f"Casa {CasaABorrar [0]} eliminada.")
            listaCasas.remove(CasaABorrar)
        else:
            print("Por favor, ingrese una instancia válida.")
    else:
        print("La casa no tiene instancias habilitadas todavía.")

def controlCasas(listaCasas):
    if listaCasas != []:
        for casa in listaCasas:
            print(f"{listaCasas.index(casa)+1}. {casa [0]}")
        casa_seleccionada =int(input("Seleccione una casa: "))
        if casa_seleccionada in range (1,len(listaCasas)+1):
            modo_casa = True
            casaAUso = listaCasas [casa_seleccionada-1]
            print (f"Bienvenido a {casaAUso [0]}")
            while modo_casa == True:
                #[nombrecasa, [nombrehabitacion [nombredispositivo,estadodispositivo]], [casa2, [habitacion, [nombredispositivo, estadodispositivo]]]]
                opcionCasa = input("\n1. Controlar instancias\n2. Añadir instancias\n3. Eliminar instancias\n4. Salir\nSeleccione una opción: ")
                listaInstancias = casaAUso [1]
                if opcionCasa == "1":
                    if listaInstancias != []:
                        for instancia in listaInstancias:
                            print(f"{listaInstancias.index(instancia)+1}. {instancia [0]}")
                        instanciaEscogida = int(input("Seleccione cuál instancia desea controlar: "))
                        if instanciaEscogida in range (1,len(listaInstancias)+1):
                            instanciaAUso = listaInstancias [instanciaEscogida-1]
                            print (f"Bienvenido a {instanciaAUso [0]}.")
                            listaDispositivos = instanciaAUso [1]
                            modoControlDispositivos = True
                            while modoControlDispositivos == True:
                                opcionDispositivos = input("\n1. Agregar dispositivo\n2. Actualizar dispositivo\n3. Actualizar pin de cerradura\n4. Eliminar dispositivo\n5. Salir\nSeleccione una opción: ")
                                if opcionDispositivos == "1":
                                    tipoDispositivoAgregar = int(input("¿De qué tipo será el dispositivo por agregar?\n1. Electrónico (Apagador, tomacorriente...)\n2. Cerradura:\n"))
                                    if tipoDispositivoAgregar == 1:
                                        nombreDispositivoAgregar = input("¿Cuál nombre le asignará al dispositivo? ")
                                        estadoDispositivoAgregar = int(input("¿El dispositivo se encuentra encendido o apagado?\n1.Encendido\n2.Apagado\n"))
                                        listaDispositivos.append([tipoDispositivoAgregar,nombreDispositivoAgregar,estadoDispositivoAgregar])
                                    elif tipoDispositivoAgregar == 2:
                                        nombreCerraduraAgregar = input("¿Cuál nombre le asignará a la cerradura? ")
                                        estadoCerraduraAgregar = int(input("¿La cerradura se encuentra abierta o cerrada?\n1.Abierta\n2.Cerrada\n"))
                                        while True:
                                            pinCerradura = input ("Por favor, asígnele un pin de 4 dígitos o mayor extensión a la cerradura: ")
                                            if len(pinCerradura) >= 4:
                                                listaDispositivos.append([tipoDispositivoAgregar,nombreCerraduraAgregar,estadoCerraduraAgregar,pinCerradura])
                                                break
                                            else:
                                                print("Por favor, asígnele un pin de mayor extensión")
                                    else:
                                        print("Por favor, ingrese una opción válida.")
                                    print(listaDispositivos)
                                elif opcionDispositivos == "2":
                                    if listaDispositivos != []:
                                        for dispositivo in listaDispositivos:
                                            tipoDispositivo = dispositivo [0]
                                            nombreDispositivo = dispositivo [1]
                                            estadoDispositivo = dispositivo [2]
                                            if tipoDispositivo == 1:
                                                if estadoDispositivo == 1:
                                                    estadoDisplay = "Encendido"
                                                if estadoDispositivo == 2:
                                                    estadoDisplay = "Apagado"
                                            if tipoDispositivo == 2:
                                                if estadoDispositivo == 1:
                                                    estadoDisplay = "Abierto"
                                                if estadoDispositivo == 2:
                                                    estadoDisplay = "Cerrado"
                                            print(f"{listaDispositivos.index(dispositivo)+1}. {nombreDispositivo} Estado: {estadoDisplay}")
                                        dispositivoPedido = int(input("¿De cuál dispositivo de la lista desea cambiar el estado? "))
                                        if dispositivoPedido in range(1,len(listaDispositivos)+1):
                                            dispositivoSeleccionado = listaDispositivos [dispositivoPedido-1]
                                            tipoDispositivoSeleccionado = dispositivoSeleccionado [0]
                                            estadoDispositivoSeleccionado = dispositivoSeleccionado [2]
                                            if tipoDispositivoSeleccionado == 1:
                                                NuevoEstadoDispositivo = int(input("¿Desea encender o apagar el dispositivo: \n1.Encender\n2.Apagar\n"))
                                                while True:
                                                    if NuevoEstadoDispositivo in range (1,3):
                                                        estadoDispositivoSeleccionado = NuevoEstadoDispositivo
                                                        break
                                                    else:
                                                        print("Por favor, ingrese un estado válido.")
                                            if tipoDispositivoSeleccionado == 2:
                                                pinDispositivo = dispositivoSeleccionado [3]
                                                while True:
                                                    pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                                                    if pinDispositivo == pinComparacion:
                                                        break
                                                    else:
                                                        print("Pin incorrecto. Por favor, ingrese el válido.")
                                                NuevoEstadoDispositivo = int(input("¿Desea abrir o cerrar la cerradura: \n1.Abrir\n2.Cerrar\n"))
                                                while True:
                                                    if NuevoEstadoDispositivo in range (1,3):
                                                        estadoDispositivoSeleccionado = NuevoEstadoDispositivo
                                                        break
                                                    else:
                                                        print("Por favor, ingrese un estado válido.")
                                        else:
                                            print("Por favor, ingrese un valor válido.")
                                    else:
                                        print("Esta instancia no tiene dispositivos añadidos.")
                                elif opcionDispositivos == "3":
                                    if listaDispositivos != []:
                                        listaCerraduras = []
                                        for dispositivo in listaDispositivos:
                                            tipoDispositivo = dispositivo [0]
                                            nombreDispositivo = dispositivo [1]
                                            if tipoDispositivo == 1:
                                                pass
                                            if tipoDispositivo == 2:
                                                listaCerraduras.append(dispositivo)
                                                print(f"{listaCerraduras.index(dispositivo)+1}. {nombreDispositivo}")
                                        cerraduraPedida = int(input("¿De cuál cerradura de la lista desea cambiar el pin? "))
                                        if cerraduraPedida in range(1,len(listaCerraduras)+1):
                                            cerraduraSeleccionada = listaCerraduras [cerraduraPedida-1]
                                            pinCerraduraSeleccionada = cerraduraSeleccionada [3]
                                            listaDispositivos.remove(cerraduraSeleccionada)
                                            while True:
                                                pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                                                if pinCerraduraSeleccionada == pinComparacion:
                                                    print("Pin válido")
                                                    nuevoPin = input ("Por favor, asigne un nuevo pin de 4 dígitos o mayor extensión a la cerradura: ")
                                                    if len(nuevoPin) >= 4:
                                                        cerraduraSeleccionada [3] = nuevoPin
                                                        listaDispositivos.append(cerraduraSeleccionada)
                                                        break
                                                    else:
                                                        print("Por favor, asígnele un pin de mayor extensión")
                                                else:
                                                    print("Pin incorrecto. Por favor, ingrese el válido.")
                                elif opcionDispositivos == "4":
                                    if listaDispositivos != []:
                                        for dipositivo in listaDispositivos:
                                            print(f"{listaDispositivos.index(dipositivo)+1}. {dipositivo [1]}")
                                        seleccionDispositivo = int(input("Seleccione cuál instancia desea eliminar: "))
                                        dispositivoABorrar = listaDispositivos[seleccionDispositivo-1]
                                        if seleccionDispositivo in range (1,len(listaDispositivos)+1):
                                            print (f"Dipositivo {dispositivoABorrar [1]} eliminado.")
                                            listaDispositivos.remove(dispositivoABorrar)
                                        else:
                                            print("Por favor, ingrese un dispositivo válido.")
                                    else:
                                        print("La casa no tiene dispositivos habilitados todavía.")
                                elif opcionDispositivos == "5":
                                    modoControlDispositivos = False
                                else:
                                    print("Por favor, ingrese una opción válida.")
                        else:
                            print("Por favor, ingrese una instancia válida.")
                    else:
                        print("No tiene instancias agregadas.\nPor favor, agregue una instancia válida.")
                elif opcionCasa == "2":
                    nombresInstancias = []
                    for instancia in listaInstancias:
                        nombresInstancias.append(instancia [0])
                    while True:
                        nombreInstancia = input ("Por favor, ingrese el nombre de la instancia que desea agregar: ")
                        if nombreInstancia not in nombresInstancias: 
                            listaInstancias.append ([nombreInstancia,[]])
                            break
                        else:
                            print("Este nombre ya está asignado a una instancia.\nPor favor, pruebe con otro nombre.")
                elif opcionCasa == "3":
                    if listaInstancias != []:
                        for instancia in listaInstancias:
                            print(f"{listaInstancias.index(instancia)+1}. {instancia [0]}")
                        seleccionInstancia = int(input("Seleccione cuál instancia desea eliminar: "))
                        instanciaABorrar = listaInstancias[seleccionInstancia-1]
                        if seleccionInstancia in range (1,len(listaInstancias)+1):
                            print (f"Instancia {instanciaABorrar [0]} eliminada.")
                            listaInstancias.remove(instanciaABorrar)
                        else:
                            print("Por favor, ingrese una instancia válida.")
                    else:
                        print("La casa no tiene instancias habilitadas todavía.")
                elif opcionCasa == "4":
                    modo_casa = False
                    break
                else:
                    print("Por favor, seleccione una opción válida.")
        else:
            print ("Por favor, seleccione una casa válida.")
    else:
        print ("No hay casas registradas. Por favor, ingrese una nueva.")
    
def modo_usuario ():
    for i in usuarios:
        print(f"{usuarios.index(i)+1}. {i [0]}")
    while True:
        seleccionUsuario = int(input("Por favor, seleccione con cuál usuario piensa conectarse: "))
        if seleccionUsuario not in range (1, len(usuarios)+1):
            print ("Por favor, seleccione un usuario válido.")
        else:
            correo_match = usuarios [seleccionUsuario-1] [1]
            pin_match = usuarios [seleccionUsuario-1] [2]
            break
    while True:
        correo_login = input("Ingrese su correo electrónico: ")
        pin_login = input("Ingrese su PIN: ")
        if correo_match == correo_login and pin_match == pin_login:
            print("Inicio de sesión exitoso.")
            usuario_def = usuarios [seleccionUsuario-1]
            print (f"Bienvenido, {usuario_def [0]}\n")
            break
        else:
            print("Por favor, ingrese los datos correctos.")
    while usuario_def != []:
        casas_usuario = usuario_def[3]
        opcion_usuario = input ("\nMenú principal: \n1. Controlar casa\n2. Registrar nueva casa\n3. Eliminar casa\n4. Salir\nSeleccione una opción: ")
        if opcion_usuario == "1":
            controlCasas(casas_usuario)
            
        elif opcion_usuario == "2":
            agregarCasa(casas_usuario)
            
        elif opcion_usuario == "3":
            eliminarCasa(casas_usuario)

        elif opcion_usuario  == "4":
            usuario_def[3] = casas_usuario
            break

        else:
            print("Por favor, ingrese una opción válida.")

while True:
    if usuarios == []:
        agregar_usuario()
    opcion = input("\nBienvenido a la aplicación Smart Home\n1. Iniciar sesión\n2. Registrarse\n3. Salir\nSeleccione una opción: ")
    if opcion == "1":
        modo_usuario()
    elif opcion == "2":
        agregar_usuario()
    elif opcion == "3":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
    print(usuarios)
    ()