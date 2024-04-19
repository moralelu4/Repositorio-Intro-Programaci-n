import os
import json

db= "db.json"
if not os.path.exists(db):
    with open(db, 'w', encoding='utf-8') as baseDatos:
        json.dump({}, baseDatos)
with open(db, "r", encoding='utf-8') as baseDatos:
    base= json.load(baseDatos)

def agregarUsuario():
    with open(db, "r", encoding='utf-8') as baseDatos:
        base= json.load(baseDatos)
    nombre = input("Ingrese su nombre: ")
    while True:
        correo = input("Ingrese un correo electrónico: ")
        if "@" not in correo or "." not in correo:
            print ("Correo electrónico inválido. Por favor, ingrese un correo electrónico válido.")
        else:
            break
    pin = input("Ingrese un PIN: ")
    nuevousuario = {"nombre": nombre, "correo": correo, "pin": pin, "casas":[]}
    base["usuarios"] = base.get("usuarios", []) + [nuevousuario]
    with open(db, "w", encoding='utf-8') as baseDatos:
        json.dump(base, baseDatos, indent=4)
    print("Usuario registrado exitosamente.")

def agregarCasa(usuarioDef,base):
    nombreCasa = input("Ingrese el nombre de la casa: ")
    usuarioDef['casas'].append({"nombreCasa": nombreCasa, "instancias": []})
    print("Casa agregada exitosamente.")
    with open(db, 'w', encoding='utf-8') as baseDatos:
        json.dump(base, baseDatos, indent=4)

def eliminarCasa(usuarioDef):
    listaCasas = usuarioDef['casas']

    if listaCasas != []:
        for i, casa in enumerate(listaCasas, start=1):
            print(f"{i}. {casa['nombreCasa']}")
        try:
            seleccionCasaPorBorrar = int(input("Por favor, seleccione cuál casa desea eliminar: "))
            if seleccionCasaPorBorrar in range(1, len(listaCasas)+1):
                casaABorrar = listaCasas[seleccionCasaPorBorrar-1]
                print(f"Casa {casaABorrar['nombreCasa']} eliminada.")
                listaCasas.remove(casaABorrar)
                with open(db, 'r', encoding='utf-8') as baseDatos:
                    data = json.load(baseDatos)
                for usuario in data['usuarios']:
                    if usuario['nombre'] == usuarioDef['nombre']:
                        usuario['casas'] = listaCasas
                with open(db, 'w', encoding='utf-8') as baseDatos:
                    json.dump(data, baseDatos, indent=4)
            else:
                print("Por favor, ingrese una casa válida.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")
    else:
        print("No hay casas registradas todavía.")

def agregarDispositivos (listaDispositivos, instanciaAUso,data):
    try:
        tipoDispositivoAgregar = input("¿De qué tipo será el dispositivo por agregar?\n1. Electrónico (Apagador, tomacorriente...)\n2. Cerradura:\n")
        if tipoDispositivoAgregar in ["1", "2"]:
            if tipoDispositivoAgregar == "1":
                tipoDispositivoAgregar = "Electrónico"
                nombreDispositivoAgregar = input("¿Cuál nombre le asignará al dispositivo? ")
                try:
                    estadoDispositivoAgregar = input("¿El dispositivo se encuentra encendido o apagado?\n1.Encendido\n2.Apagado\n") #Cambiar etiquetado de estados.
                    if estadoDispositivoAgregar in ["1", "2"]:
                        if estadoDispositivoAgregar == "1":
                            estadoDispositivoAgregar = "Encendido"
                        if estadoDispositivoAgregar == "2":
                            estadoDispositivoAgregar = "Apagado"
                        listaDispositivos.append({"tipoDispositivo": tipoDispositivoAgregar, "nombreDispositivo": nombreDispositivoAgregar, "estadoDispositivo": estadoDispositivoAgregar})
                        print ("Dispositivo electrónico agregado exitosamente.")
                    else:
                        print("Por favor, ingrese un estado válido.")
                except ValueError:
                    print("Por favor, ingrese un estado válido.")
            elif tipoDispositivoAgregar == "2":
                tipoDispositivoAgregar = "Cerradura"
                nombreCerraduraAgregar = input("¿Cuál nombre le asignará a la cerradura? ")
                try:
                    estadoCerraduraAgregar = input("¿La cerradura se encuentra abierta o cerrada?\n1.Abierta\n2.Cerrada\n")
                    if estadoCerraduraAgregar in ["1", "2"]:
                        if estadoCerraduraAgregar == "1":
                            estadoCerraduraAgregar = "Abierta"
                        if estadoCerraduraAgregar == "2":
                            estadoCerraduraAgregar = "Cerrada"
                        while True:
                            pinCerradura = input ("Por favor, asígnele un pin de 4 dígitos o mayor extensión a la cerradura: ")
                            if len(pinCerradura) >= 4:
                                listaDispositivos.append({"tipoDispositivo": tipoDispositivoAgregar, "nombreDispositivo": nombreCerraduraAgregar, "estadoDispositivo": estadoCerraduraAgregar, "pinCerradura": pinCerradura})
                                print (f"Cerradura {nombreCerraduraAgregar} agregada exitosamente.")
                                break
                            else:
                                print("Por favor, asígnele un pin de mayor extensión")
                    else:
                        print("Por favor, ingrese un estado válido.")
                except ValueError:
                    print("Por favor, ingrese un estado válido.")
    except ValueError:
        print("Por favor, ingrese una opción válida.")
    if instanciaAUso:
        instanciaAUso['dispositivos'] = listaDispositivos
    with open(db, 'w', encoding='utf-8') as baseDatos:
        json.dump(data, baseDatos, indent=4)

def actualizacionDispositivo(listaDispositivos, instanciaAUso, data):
    if listaDispositivos != []:
        for dispositivo in listaDispositivos:
            nombreDispositivo = dispositivo ["nombreDispositivo"]
            estadoDispositivo = dispositivo ["estadoDispositivo"]
            print(f"{listaDispositivos.index(dispositivo)+1}. {nombreDispositivo} Estado: {estadoDispositivo}")
        try:
            dispositivoPedido = int(input("¿De cuál dispositivo de la lista desea cambiar el estado? "))
            if dispositivoPedido in range(1,len(listaDispositivos)+1):
                dispositivoSeleccionado = listaDispositivos [dispositivoPedido-1]
                tipoDispositivoSeleccionado = dispositivoSeleccionado ["tipoDispositivo"]
                estadoDispositivoSeleccionado = dispositivoSeleccionado ["estadoDispositivo"]
                if tipoDispositivoSeleccionado == 'Electrónico':
                    try:
                        nuevoEstadoDispositivo = input("¿Desea encender o apagar el dispositivo? \n1.Encender\n2.Apagar\n")
                        if nuevoEstadoDispositivo in ["1", "2"]:
                            if nuevoEstadoDispositivo == "1":
                                nuevoEstadoDispositivo = "Encendido"
                            if nuevoEstadoDispositivo == "2":
                                nuevoEstadoDispositivo = "Apagado"
                            dispositivoSeleccionado ["estadoDispositivo"] = nuevoEstadoDispositivo
                            print(f"Ahora, el dispositivo {dispositivoSeleccionado['nombreDispositivo']} está: {nuevoEstadoDispositivo}")
                        else:
                            print("Por favor, ingrese un estado válido.")
                    except ValueError:
                        print("Por favor, ingrese un estado válido.")
                if tipoDispositivoSeleccionado == 'Cerradura':
                    pinDispositivo = dispositivoSeleccionado ["pinCerradura"]
                    while True:
                        pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                        if pinDispositivo == pinComparacion:
                            break
                        else:
                            print("Pin incorrecto. Por favor, ingrese el válido.")
                    try:
                        nuevoEstadoDispositivo = input("¿Desea abrir o cerrar la cerradura? \n1.Abrir\n2.Cerrar\n")
                        if nuevoEstadoDispositivo in ["1", "2"]:
                            if nuevoEstadoDispositivo == "1":
                                nuevoEstadoDispositivo = "Abierta"
                            if nuevoEstadoDispositivo == "2":
                                nuevoEstadoDispositivo = "Cerrada"
                            dispositivoSeleccionado ["estadoDispositivo"] = nuevoEstadoDispositivo
                            print(f"Ahora, la cerradura {dispositivoSeleccionado ['nombreDispositivo']} está: {nuevoEstadoDispositivo}")
                        else:
                            print("Por favor, ingrese un estado válido.")
                    except ValueError:
                        print("Por favor, ingrese un estado válido.")
            else:
                print("Por favor, ingrese un valor válido.")
        except ValueError:
            print("Por favor, ingrese un valor válido.")
    else:
        print("Esta instancia no tiene dispositivos añadidos.")
    if instanciaAUso:
        instanciaAUso['dispositivos'] = listaDispositivos
    with open(db, 'w', encoding='utf-8') as baseDatos:
        json.dump(data, baseDatos, indent=4)

def actualizacionPinCerradura(listaDispositivos, instanciaAUso, data):
    if listaDispositivos != []:
        listaCerraduras = [dispositivo for dispositivo in listaDispositivos if dispositivo['tipoDispositivo'] == 'Cerradura']
        for i, cerradura in enumerate(listaCerraduras):
            print(f"{i+1}. {cerradura['nombreDispositivo']}")
        if not listaCerraduras:
            print("No hay cerraduras conectadas todavía.")
        else:
            try:
                cerraduraPedida = int(input("¿De cuál cerradura de la lista desea cambiar el pin? "))
                if 1 <= cerraduraPedida <= len(listaCerraduras):
                    cerraduraSeleccionada = listaCerraduras[cerraduraPedida-1]
                while True:
                    pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                    if cerraduraSeleccionada['pinCerradura'] == pinComparacion:
                        print("Pin válido")
                        nuevoPin = input("Por favor, asigne un nuevo pin de 4 dígitos o mayor extensión a la cerradura: ")
                        if len(nuevoPin) >= 4:
                            cerraduraSeleccionada['pinCerradura'] = nuevoPin
                            break
                        else:
                            print("Por favor, asígnele un pin de mayor extensión")
                    else:
                        print("Pin incorrecto. Por favor, ingrese el válido.")
                else:
                    print("Por favor, ingrese una cerradura válida.")
            except ValueError:
                print("Por favor, ingrese un valor válido.")
            if instanciaAUso:
                instanciaAUso['dispositivos'] = listaDispositivos
            with open(db, 'w', encoding='utf-8') as baseDatos:
                json.dump(data, baseDatos, indent=4)
    else:
        print("Esta instancia no tiene dispositivos añadidos.")

def eliminacionDispositivo(listaDispositivos, instanciaAUso, data):
    if listaDispositivos != []:
        for i, instancia in enumerate(listaDispositivos, start=1):
            print(f"{i}. {instancia['nombreDispositivo']}")
        try:
            while True:
                seleccionDispositivo = int(input("Seleccione cuál instancia desea eliminar: "))
                if seleccionDispositivo in range (1,len(listaDispositivos)+1):
                    dispositivoABorrar = listaDispositivos[seleccionDispositivo-1]
                    print (f"Dipositivo {dispositivoABorrar ['nombreDispositivo']} eliminado.")
                    listaDispositivos.remove(dispositivoABorrar)
                    if instanciaAUso:
                        instanciaAUso['dispositivos'] = listaDispositivos
                    break
                else:
                    print("Por favor, ingrese un dispositivo válido.")
        except ValueError:
            print("Por favor, ingrese un valor válido.")
        with open(db, 'w', encoding='utf-8') as baseDatos:
            json.dump(data, baseDatos, indent=4)
    else:
        print("Esta instancia no tiene dispositivos añadidos.")

def observacionDispositivos(listaDispositivos):
    print ("\n")
    if listaDispositivos != []:
        for dispositivo in listaDispositivos:
            nombreDispositivo = dispositivo ["nombreDispositivo"]
            estadoDispositivo = dispositivo ["estadoDispositivo"]
            print(f"{listaDispositivos.index(dispositivo)+1}. {nombreDispositivo} Estado: {estadoDispositivo}")
    else:
        print("Esta instancia no tiene dispositivos añadidos.")

def controlInstancias(listaInstancias, casaAUso, data):
    if listaInstancias != []:
        for i, instancia in enumerate(listaInstancias, start=1):
            print(f"{i}. {instancia['nombreInstancia']}")
        try:
            instanciaEscogida = int(input("Seleccione cuál instancia desea controlar: "))
            if instanciaEscogida in range (1,len(listaInstancias)+1):
                instanciaAUso = listaInstancias [instanciaEscogida-1]
                print (f"Bienvenido a {instanciaAUso ['nombreInstancia']}.")
                listaDispositivos = instanciaAUso ["dispositivos"]
                modoControlDispositivos = True
                while modoControlDispositivos == True:
                    opcionDispositivos = input("\n1. Agregar dispositivo\n2. Actualizar dispositivo\n3. Actualizar pin de cerradura\n4. Eliminar dispositivo\n5. Observación de dispositivos\n6. Salir\nSeleccione una opción: ")
                    if opcionDispositivos == "1":
                        agregarDispositivos(listaDispositivos, instanciaAUso, data)
                    elif opcionDispositivos == "2":
                        actualizacionDispositivo(listaDispositivos, instanciaAUso, data)
                    elif opcionDispositivos == "3":
                        actualizacionPinCerradura(listaDispositivos, instanciaAUso, data)
                    elif opcionDispositivos == "4":
                        eliminacionDispositivo(listaDispositivos, instanciaAUso, data)
                    elif opcionDispositivos == "5":
                        observacionDispositivos(listaDispositivos)
                    elif opcionDispositivos == "6":
                        modoControlDispositivos = False
                    else:
                        print("Por favor, ingrese una opción válida.")
                if casaAUso:
                    casaAUso['instancias'] = listaInstancias
                with open(db, 'w', encoding='utf-8') as baseDatos:
                    json.dump(data, baseDatos, indent=4)
            else:
                print("Por favor, ingrese una instancia válida.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")
    else:
        print("No tiene instancias agregadas.\nPor favor, agregue una instancia válida.")


def controlCasas(casasUsuario, usuarioDef):
    with open(db, 'r', encoding='utf-8') as baseDatos:
        data = json.load(baseDatos)
    if casasUsuario != []:
        for i, casa in enumerate(casasUsuario, start=1):
            print(f"{i}. {casa['nombreCasa']}")
        try:
            casaSeleccionada = int(input("Seleccione una casa: "))
            if casaSeleccionada in range(1, len(casasUsuario)+1):
                modoCasa = True
                casaAUso = casasUsuario[casaSeleccionada-1]
                print(f"Bienvenido a {casaAUso['nombreCasa']}")
                while modoCasa == True:
                    opcionCasa = input("\n1. Controlar instancias\n2. Añadir instancias\n3. Eliminar instancias\n4. Salir\nSeleccione una opción: ")
                    usuario = next((user for user in data['usuarios'] if user['nombre'] == usuarioDef['nombre']), None)
                    casaAUso = next((house for house in usuario['casas'] if house['nombreCasa'] == casaAUso['nombreCasa']), None) if usuario else None
                    listaInstancias = casaAUso['instancias']

                    if opcionCasa == "1":
                        controlInstancias(listaInstancias, casaAUso, data)
                    elif opcionCasa == "2":
                        nombresInstancias = [instancia['nombreInstancia'] for instancia in listaInstancias]
                        while True:
                            nombreInstancia = input("Por favor, ingrese el nombre de la instancia que desea agregar: ")
                            if nombreInstancia not in nombresInstancias: 
                                listaInstancias.append({'nombreInstancia': nombreInstancia, 'dispositivos': []})
                                if casaAUso:
                                    casaAUso['instancias'] = listaInstancias
                                break
                            else:
                                print("Este nombre ya está asignado a una instancia.\nPor favor, pruebe con otro nombre.")
                    elif opcionCasa == "3":
                        if listaInstancias != []:
                            for i, instancia in enumerate(listaInstancias, start=1):
                                print(f"{i}. {instancia['nombreInstancia']}")
                            try:
                                while True:
                                    seleccionInstancia = int(input("Seleccione cuál instancia desea eliminar: "))
                                    if seleccionInstancia in range(1, len(listaInstancias)+1):
                                        instanciaABorrar = listaInstancias[seleccionInstancia-1]
                                        print(f"Instancia {instanciaABorrar['nombreInstancia']} eliminada.")
                                        listaInstancias.remove(instanciaABorrar)
                                        if casa:
                                            casa['instancias'] = listaInstancias
                                        break
                                    else:
                                        print("Por favor, ingrese una instancia válida.")
                            except ValueError:
                                print("Por favor, ingrese un valor válido.")
                        else:
                            print("La casa no tiene instancias habilitadas todavía.")
                    elif opcionCasa == "4":
                        modoCasa = False
                        break
                    else:
                        print("Por favor, seleccione una opción válida.")
                    with open(db, 'w', encoding='utf-8') as baseDatos:
                        json.dump(data, baseDatos, indent=4) ###Revisar por qué acá no hace la escritura en utf-8
            else:
                print("Por favor, seleccione una casa válida.")
        except ValueError:
            print("Por favor, ingrese un valor válido.")
    else:
        print("No hay casas registradas. Por favor, ingrese una nueva.")
    
def modoUsuario():
    with open(db, 'r', encoding='utf-8') as baseDatos:
        base = json.load(baseDatos)
    usuarios = base["usuarios"]
    usuarioDef = None
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nombre']}")
    while True:
        try:
            seleccionUsuario = int(input("Por favor, seleccione con cuál usuario piensa conectarse: "))
            if seleccionUsuario not in range(1, len(usuarios)+1):
                print("Por favor, seleccione un usuario válido.")
            else:
                correoMatch = usuarios[seleccionUsuario-1]['correo']
                pinMatch = usuarios[seleccionUsuario-1]['pin']
                break
        except ValueError:
            print("Por favor, ingrese una opción válida.")
    while True:
        correoLogin = input("Ingrese su correo electrónico: ")
        pinLogin = input("Ingrese su PIN: ")
        if correoMatch == correoLogin and pinMatch == pinLogin:
            print("Inicio de sesión exitoso.")
            usuarioDef = usuarios[seleccionUsuario-1]
            print(f"Bienvenido, {usuarioDef['nombre']}\n")
            break
        else:
            print("Por favor, ingrese los datos correctos.")
    while usuarioDef != {}:
        casasUsuario = usuarioDef['casas']
        opcionUsuario = input("\nMenú principal: \n1. Controlar casa\n2. Registrar nueva casa\n3. Eliminar casa\n4. Salir\nSeleccione una opción: ")
        if opcionUsuario == "1":
            controlCasas(casasUsuario, usuarioDef)
        elif opcionUsuario == "2":
            agregarCasa(usuarioDef,base)
        elif opcionUsuario == "3":
            eliminarCasa(usuarioDef)
        elif opcionUsuario == "4":
            break
        else:
            print("Por favor, ingrese una opción válida.")

while True:
    if base == {}:
        agregarUsuario()
    opcion = input("\nBienvenido a la aplicación Smart Home\n1. Iniciar sesión\n2. Registrarse\n3. Salir\nSeleccione una opción: ")
    if opcion == "1":
        modoUsuario()
    elif opcion == "2":
        agregarUsuario()
    elif opcion == "3":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")