###Revisar formato de los json.dump

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
    with open(db, "w") as json_file:
        json.dump(base, json_file, indent=4)
        print(str(json_file))
    print("Usuario registrado exitosamente.")

def agregarCasa(usuarioDef,base):
    nombreCasa = input("Ingrese el nombre de la casa: ")
    usuarioDef['casas'].append({"nombreCasa": nombreCasa, "habitaciones": []})
    print("Casa agregada exitosamente.")
    with open('db.json', 'w', encoding='utf-8') as json_file:
        json.dump(base, json_file, indent=4)

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
                with open('db.json', 'r') as f:
                    data = json.load(f)
                for usuario in data['usuarios']:
                    if usuario['nombre'] == usuarioDef['nombre']:
                        usuario['casas'] = listaCasas
                with open('db.json', 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                print("Por favor, ingrese una casa válida.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")
    else:
        print("No hay casas registradas todavía.")

def agregarDispositivos (listaDispositivos):
    try:
        tipoDispositivoAgregar = int(input("¿De qué tipo será el dispositivo por agregar?\n1. Electrónico (Apagador, tomacorriente...)\n2. Cerradura:\n"))
        if tipoDispositivoAgregar in [1, 2]:
            if tipoDispositivoAgregar == 1:
                nombreDispositivoAgregar = input("¿Cuál nombre le asignará al dispositivo? ")
                try:
                    estadoDispositivoAgregar = int(input("¿El dispositivo se encuentra encendido o apagado?\n1.Encendido\n2.Apagado\n"))
                    if estadoDispositivoAgregar in [1, 2]:
                        listaDispositivos.append([tipoDispositivoAgregar,nombreDispositivoAgregar,estadoDispositivoAgregar])
                    else:
                        print("Por favor, ingrese un estado válido.")
                except ValueError:
                    print("Por favor, ingrese un estado válido.")
            elif tipoDispositivoAgregar == 2:
                nombreCerraduraAgregar = input("¿Cuál nombre le asignará a la cerradura? ")
                try:
                    estadoCerraduraAgregar = int(input("¿La cerradura se encuentra abierta o cerrada?\n1.Abierta\n2.Cerrada\n"))
                    if estadoCerraduraAgregar in [1, 2]:
                        while True:
                            pinCerradura = input ("Por favor, asígnele un pin de 4 dígitos o mayor extensión a la cerradura: ")
                            if len(pinCerradura) >= 4:
                                listaDispositivos.append([tipoDispositivoAgregar,nombreCerraduraAgregar,estadoCerraduraAgregar,pinCerradura])
                                break
                            else:
                                print("Por favor, asígnele un pin de mayor extensión")
                    else:
                        print("Por favor, ingrese un estado válido.")
                except ValueError:
                    print("Por favor, ingrese un estado válido.")
    except ValueError:
        print("Por favor, ingrese una opción válida.")

def actualizacionDispositivo(listaDispositivos):
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
        try:
            dispositivoPedido = int(input("¿De cuál dispositivo de la lista desea cambiar el estado? "))
            if dispositivoPedido in range(1,len(listaDispositivos)+1):
                dispositivoSeleccionado = listaDispositivos [dispositivoPedido-1]
                tipoDispositivoSeleccionado = dispositivoSeleccionado [0]
                estadoDispositivoSeleccionado = dispositivoSeleccionado [2]
                if tipoDispositivoSeleccionado == 1:
                    try:
                        nuevoEstadoDispositivo = int(input("¿Desea encender o apagar el dispositivo? \n1.Encender\n2.Apagar\n"))
                        if nuevoEstadoDispositivo in [1, 2]:
                            dispositivoSeleccionado [2] = nuevoEstadoDispositivo
                            if nuevoEstadoDispositivo == 1:
                                nuevoEstadoDisplay = "Encendido"
                            if nuevoEstadoDispositivo == 2:
                                nuevoEstadoDisplay = "Apagado"
                            print(f"Ahora, el dispositivo {dispositivoSeleccionado [1]} está: {nuevoEstadoDisplay}")
                        else:
                            print("Por favor, ingrese un estado válido.")
                    except ValueError:
                        print("Por favor, ingrese un estado válido.")
                if tipoDispositivoSeleccionado == 2:
                    pinDispositivo = dispositivoSeleccionado [3]
                    while True:
                        pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                        if pinDispositivo == pinComparacion:
                            break
                        else:
                            print("Pin incorrecto. Por favor, ingrese el válido.")
                    try:
                        nuevoEstadoDispositivo = int(input("¿Desea abrir o cerrar la cerradura? \n1.Abrir\n2.Cerrar\n"))
                        if nuevoEstadoDispositivo in [1, 2]:
                            dispositivoSeleccionado [2] = nuevoEstadoDispositivo
                            if nuevoEstadoDispositivo == 1:
                                nuevoEstadoDisplay = "Abierto"
                            if nuevoEstadoDispositivo == 2:
                                nuevoEstadoDisplay = "Cerrado"
                            print(f"Ahora, el dispositivo {dispositivoSeleccionado [1]} está: {nuevoEstadoDisplay}")
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

def actualizacionPinCerradura(listaDispositivos):
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
        if listaCerraduras == []:
            print("No hay cerraduras conectadas todavía.")
        else:
            try:
                cerraduraPedida = int(input("¿De cuál cerradura de la lista desea cambiar el pin? "))
                if cerraduraPedida in range(1,len(listaCerraduras)+1):
                    cerraduraSeleccionada = listaCerraduras [cerraduraPedida-1]
                    pinCerraduraSeleccionada = cerraduraSeleccionada [3]
                    listaDispositivos.remove(cerraduraSeleccionada)
                    while True:
                        pinComparacion = input("Por motivos de seguridad, para este proceso se le solicitará el pin de la cerradura: ")
                        if pinCerraduraSeleccionada == pinComparacion:
                            print("Pin válido")
                            nuevoPin = input("Por favor, asigne un nuevo pin de 4 dígitos o mayor extensión a la cerradura: ")
                            if len(nuevoPin) >= 4:
                                cerraduraSeleccionada [3] = nuevoPin
                                listaDispositivos.append(cerraduraSeleccionada)
                                break
                            else:
                                print("Por favor, asígnele un pin de mayor extensión")
                        else:
                            print("Pin incorrecto. Por favor, ingrese el válido.")
                else:
                    print("Por favor, ingrese una cerradura válida.")
            except ValueError:
                print("Por favor, ingrese un valor válido.")
    else:
        print("Esta instancia no tiene dispositivos añadidos.")

def eliminacionDispositivo(listaDispositivos):
    if listaDispositivos != []:
        for dispositivo in listaDispositivos:
            print(f"{listaDispositivos.index(dispositivo)+1}. {dispositivo [1]}")
        try:
            seleccionDispositivo = int(input("Seleccione cuál instancia desea eliminar: "))
            if seleccionDispositivo in range (1,len(listaDispositivos)+1):
                dispositivoABorrar = listaDispositivos[seleccionDispositivo-1]
                print (f"Dipositivo {dispositivoABorrar [1]} eliminado.")
                listaDispositivos.remove(dispositivoABorrar)
            else:
                print("Por favor, ingrese un dispositivo válido.")
        except ValueError:
            print("Por favor, ingrese un valor válido.")
    else:
        print("Esta instancia no tiene dispositivos añadidos.")

def controlInstancias(listaInstancias):
    if listaInstancias != []:
        for i, instancia in enumerate(listaInstancias, start=1):
            print(f"{i}. {instancia['nombreInstancia']}")
        try:
            instanciaEscogida = int(input("Seleccione cuál instancia desea controlar: "))
            if instanciaEscogida in range (1,len(listaInstancias)+1):
                instanciaAUso = listaInstancias [instanciaEscogida-1]
                print (f"Bienvenido a {instanciaAUso ['nombreInstancia']}.")
                listaDispositivos = instanciaAUso [1] ###Acá empieza gestión de dispositivos.
                modoControlDispositivos = True
                while modoControlDispositivos == True:
                    opcionDispositivos = input("\n1. Agregar dispositivo\n2. Actualizar dispositivo\n3. Actualizar pin de cerradura\n4. Eliminar dispositivo\n5. Salir\nSeleccione una opción: ")
                    if opcionDispositivos == "1":
                        agregarDispositivos(listaDispositivos)
                    elif opcionDispositivos == "2":
                        actualizacionDispositivo(listaDispositivos)
                    elif opcionDispositivos == "3":
                        actualizacionPinCerradura(listaDispositivos)
                    elif opcionDispositivos == "4":
                        eliminacionDispositivo(listaDispositivos)
                    elif opcionDispositivos == "5":
                        modoControlDispositivos = False
                    else:
                        print("Por favor, ingrese una opción válida.")
            else:
                print("Por favor, ingrese una instancia válida.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")
    else:
        print("No tiene instancias agregadas.\nPor favor, agregue una instancia válida.")


def controlCasas(casasUsuario, usuarioDef):
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
                    listaInstancias = casaAUso['habitaciones']
                    if opcionCasa == "1":
                        controlInstancias(listaInstancias)
                    elif opcionCasa == "2":
                        nombresInstancias = [instancia['nombreInstancia'] for instancia in listaInstancias]
                        while True:
                            nombreInstancia = input("Por favor, ingrese el nombre de la instancia que desea agregar: ")
                            if nombreInstancia not in nombresInstancias: 
                                listaInstancias.append({'nombreInstancia': nombreInstancia, 'dispositivos': []})
                                with open('db.json', 'r') as f:
                                    data = json.load(f)
                                for usuario in data['usuarios']:
                                    if usuario['nombre'] == usuarioDef['nombre']:
                                        for casa in usuario['casas']:
                                            if casa['nombreCasa'] == casaAUso['nombreCasa']:
                                                casa['instancias'] = listaInstancias
                                with open('db.json', 'w') as f:
                                    json.dump(data, f, indent=4)
                                break
                            else:
                                print("Este nombre ya está asignado a una instancia.\nPor favor, pruebe con otro nombre.")
                    elif opcionCasa == "3":
                        if listaInstancias != []:
                            for i, instancia in enumerate(listaInstancias, start=1):
                                print(f"{i}. {instancia['nombreInstancia']}")
                            try:
                                seleccionInstancia = int(input("Seleccione cuál instancia desea eliminar: "))
                                if seleccionInstancia in range(1, len(listaInstancias)+1):
                                    instanciaABorrar = listaInstancias[seleccionInstancia-1]
                                    print(f"Instancia {instanciaABorrar['nombreInstancia']} eliminada.")
                                    listaInstancias.remove(instanciaABorrar)
                                    with open('db.json', 'w') as f:
                                        json.dump(casasUsuario, f, indent=4)
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
            usuarioDef = {}
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