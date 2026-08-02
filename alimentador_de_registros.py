import random
ids = []
nombres = []
codigos = []
tipos = []
fechas = []
estados = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_alimentador_de_registros|--#
#---------------------------------------------#
while True:
    print("menu principal alimentador de registros")
    print("1) crear registro")
    print("2) editar registro")
    print("3) eliminar registro")
    print("4) buscar registro")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_registro|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_registro = 1
        else:
            id_registro = ids[-1] + 1
        nombre = input("nombre del registro: ")
        codigo = input("código: ")
        tipo = input("tipo de registro: ")
        fecha = input("fecha: ")
        estado = input("estado (activo o inactivo): ")
        observacion = input("observación: ")
        ids.append(id_registro)
        nombres.append(nombre)
        codigos.append(codigo)
        tipos.append(tipo)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("registro creado correctamente.")
        print("id:", id_registro)
    #---------------------#
    #--|editar_registro|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar registro")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {codigos[i]} | {tipos[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {codigos[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del registro: ")
                codigos[posicion] = input("nuevo código: ")
                tipos[posicion] = input("nuevo tipo de registro: ")
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_registro|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar registro")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {codigos[i]} | {tipos[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {codigos[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    codigos.pop(posicion)
                    tipos.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_registro|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar registro")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {codigos[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            activos = 0
            inactivos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {codigos[i]} | {tipos[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
            print("estadísticas alimentador de registros")
            print("cantidad de registros:", len(ids))
            print("registros activos:", activos)
            print("registros inactivos:", inactivos)
            print("primer registro:", nombres[0])
            print("último registro:", nombres[-1])
            posicion = random.randint(0, len(ids) - 1)
            print("simulación de alimentación de registros")
            print("registro incorporado al sistema:")
            print(f"{ids[posicion]} | {nombres[posicion]} | {codigos[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el alimentador de registros.")
        break
    else:
        print("opción no válida.")