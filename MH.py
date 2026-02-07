# Función para limpiar la terminal
def limpiar_terminal():
    import os
    os.system('cls')
# Clase Cazador
class Cazador:
    def __init__(self, nombre, rango_id, rango_nombre, arma_id, arma_nombre, objetos):
        self.nombre = nombre
        self.rango_id = rango_id
        self.rango_nombre = rango_nombre
        self.arma_id = arma_id
        self.arma_nombre = arma_nombre
        self.objetos = objetos

    def __str__(self):
        return f"{self.nombre} (Rango: {self.rango_nombre}, Arma: {self.arma_nombre}, Objetos: {', '.join(self.objetos)})"


# Clase Misión
class Mision:
    def __init__(self, id_mision, nombre, dia_semana, cazador):
        self.id_mision = id_mision
        self.nombre = nombre
        self.dia_semana = dia_semana
        self.cazador = cazador

    def __str__(self):
        return f"[{self.id_mision}] {self.nombre} | {self.cazador} | Día: {self.dia_semana}"


# Clase Tablero de Misiones
class TableroMisiones:
    def __init__(self):
        # Se muestran las misiones disponibles (ID, Nombre, Rango mínimo)
        self.misiones_disponibles = [
            (1, "Cazar Rathalos", 1, "Bosque", 
     "Un Rathalos ha sido avistado cerca de la aldea, amenaza a los cazadores novatos.", 
     "Media", "Escamas de Rathalos"),
            (2, "Defender la aldea", 1, "Aldea", 
     "Monstruos menores atacan las murallas de la aldea, se requiere defensa inmediata.", 
     "Fácil", "Puntos de defensa y materiales comunes"),

            (3, "Recolectar hierbas raras", 2, "Pantano", 
     "Recolecta hierbas medicinales poco comunes que crecen en zonas húmedas.", 
     "Media", "Hierbas raras y materiales de curación"),

            (4, "Explorar la cueva volcánica", 2, "Volcán", 
     "Investiga la actividad volcánica y posibles monstruos que habitan en las profundidades.", 
     "Difícil", "Minerales raros y cristales volcánicos"),

            (5, "Derrotar al Tigrex", 3, "Tundra", 
     "Un Tigrex salvaje amenaza a los cazadores en las tierras heladas.", 
     "Extremo", "Colmillos de Tigrex y piel endurecida"),

            (6, "Cazar al Nargacuga", 3, "Bosque", 
     "Un Nargacuga acecha en la oscuridad del bosque, rápido y letal.", 
     "Difícil", "Plumas de Nargacuga y garras afiladas"),

            (7, "Derrotar al Rajang", 3, "Montaña", 
     "El poderoso Rajang ha aparecido, su fuerza descomunal aterroriza a los cazadores.", 
     "Extremo", "Cuerno de Rajang y pelaje dorado")

        ]

        # Se muestran los distintos rangos de cazador(RC) (ID, Nombre)
        self.rangos = [
            (1, "Novato"),
            (2, "Experto"),
            (3, "G Rank")
        ]

        # Se muetran las armas disponibles (ID, Nombre)
        self.armas = [
            (1, "Espada Larga"),
            (2, "Martillo"),
            (3, "Arco"),
            (4, "Lanza")
        ]

        # Se muestran los días de la semana disponibles (ID, Nombre)
        self.dias_semana = [
            (1, "Lunes"),
            (2, "Martes"),
            (3, "Miércoles"),
            (4, "Jueves"),
            (5, "Viernes"),
            (6, "Sábado"),
            (7, "Domingo")
        ]

        # Se muestran los objetos
        self.objetos = [
            (1, "Poción"),
            (2, "Bebida fría"),
            (3, "Bebida caliente"),
            (4, "Trampa eléctrica"),
            (5, "Trampa de escollo"),
            (6, "Bomba de luz"),
            (7, "Antídoto"),
            (8, "Piedra de afilar"),
            (9, "Bombas tranquilizantes"),
            (10, "Viales")
        ]

        # Lista de eventos activos y cancelados
        self.eventos = []
        self.canceladas = []
        self.next_id = 1

    
    # Mostrar recursos disponibles (rangos, armas, misiones, detalles de misiones, días y objetos)
    def mostrar_rangos(self):
        print("\nRango Cazador:")
        for id_r, nombre_r in self.rangos:
            print(f"{id_r}. {nombre_r}")

    def mostrar_armas(self):
        print("\nArmas disponibles:")
        for id_a, nombre_a in self.armas:
            print(f"{id_a}. {nombre_a}")

    def mostrar_misiones(self):
        print("\n=== MISIONES DISPONIBLES ===")
        print("")
        
        for id_m, nombre_m, rango_min, _, _, _, _ in self.misiones_disponibles:
            rango_nombre = dict(self.rangos)[rango_min]
            print(f"{id_m}. {nombre_m} (Rango mínimo: {rango_nombre})")
        print("")

    def mostrar_detalles_mision(self, mision_id):
        mision_dict = {m[0]: m for m in self.misiones_disponibles}
        if mision_id not in mision_dict:
            print("La misión seleccionada no existe.")
            return
    
        _, nombre, rango_min, zona, descripcion, dificultad, recompensa = mision_dict[mision_id]
        rango_nombre = dict(self.rangos)[rango_min]

        print("\n=== DETALLES DE LA MISIÓN ===\n")
        print(f"Nombre: {nombre}")
        print(f"Rango mínimo: {rango_nombre}")
        print(f"Zona: {zona}")
        print(f"Descripción: {descripcion}")
        print(f"Dificultad: {dificultad}")
        print(f"Recompensa: {recompensa}")

    def mostrar_dias(self):
        print("\nDías disponibles:")
        for id_d, nombre_d in self.dias_semana:
            print(f"{id_d}. {nombre_d}")

    def mostrar_objetos(self):
        print("\nObjetos disponibles:")
        for id_o, nombre_o in self.objetos:
            print(f"{id_o}. {nombre_o}")

    # Validaciones
    def validar_objeto_mision(self, mision_id, objeto, arma):
        reglas = {
            1: ["Poción", "Bomba de luz", "Antídoto", "Piedra de afilar", "Viales"],  # Rathalos 
            2: ["Poción", "Piedra de afilar", "Viales"],  # Defender la aldea
            3: ["Poción"],  # Recolectar hierbas raras
            4: ["Poción", "Bebida fría", "Piedra de afilar", "Viales"],  # Cueva volcánica
            5: ["Poción", "Bebida caliente", "Trampa de escollo", "Bomba de luz", "Bombas tranquilizantes", "Piedra de afilar", "Viales"],  # Tigrex
            6: ["Poción", "Bomba de luz", "Piedra de afilar", "Viales"],  # Nargacuga
            7: ["Poción", "Trampa eléctrica", "Bombas tranquilizantes", "Piedra de afilar", "Viales"]  # Rajang
        }

        if objeto not in reglas[mision_id]:
            if objeto == "Piedra de afilar" and arma in ["Espada Larga", "Martillo", "Lanza"]:
                return True
            if objeto == "Viales" and arma == "Arco":
                return True
            return False
        return True

    def validar_objeto_arma(self, objeto, arma):
        if objeto == "Piedra de afilar" and arma == "Arco":
            return False
        if objeto == "Viales" and arma in ["Espada Larga", "Martillo", "Lanza"]:
            return False
        return True

    def validar_objeto_objeto(self, objetos):
        if "Piedra de afilar" in objetos and "Viales" in objetos:
            return False
        if "Trampa de escollo" in objetos and "Trampa eléctrica" in objetos:
            return False
        if "Bebida fría" in objetos and "Bebida caliente" in objetos:
            return False
        if ("Trampa de escollo" in objetos or "Trampa eléctrica" in objetos) and "Bombas tranquilizantes" not in objetos:
            return False
        return True

    # Agregar una nueva misión al tablón de misiones
    def planificar_evento(self, mision_id, cazador, dia_semana):
        mision_dict = {m[0]: m for m in self.misiones_disponibles}
        if mision_id not in mision_dict:
            return "Misión inválida."

        _, nombre_m, rango_minimo, zona, descripcion, dificultad, recompensa = mision_dict[mision_id]

        # Restricción de rango mínimo, así se limita la entrada de cazadores novatos a misiones de rangos superiores
        if cazador.rango_id < rango_minimo:
            return f"El rango {cazador.rango_nombre} no es suficiente para '{nombre_m}'."

        # Verificar conflictos de cazador y arma en el mismo día
        for evento in self.eventos:
            if evento.cazador.nombre == cazador.nombre and evento.dia_semana == dia_semana:
                    return f"El cazador {cazador.nombre} ya está en otra misión ese día."
            if evento.cazador.arma_id == cazador.arma_id and evento.dia_semana == dia_semana:
                    return f"El arma {cazador.arma_nombre} ya está en uso ese día."

        # Añadir misión o crear evento
        nuevo_evento = Mision(self.next_id, nombre_m, dia_semana, cazador)
        self.eventos.append(nuevo_evento)
        self.next_id += 1
        salida = (
            f"\n=== MISIÓN PUBLICADA ===\n"            
            f"\nMisión: '{nombre_m}' asignada a '{cazador.nombre}'.\n"
            f"Descripción: {descripcion}.\n"
            f"Rango Cazador: {cazador.rango_nombre}.\n"
            f"Arma: {cazador.arma_nombre}.\n"
            f"Objetos: {', '.join(cazador.objetos)}.\n"
            f"Día: {dia_semana}.\n"
        )
        return salida

    # Cancelar misión
    def cancelar_evento(self, id_mision):
        for evento in self.eventos:
            if evento.id_mision == id_mision:
                self.eventos.remove(evento)
                self.canceladas.append(evento)
                return f"Evento '{evento.nombre}' cancelado, recursos liberados."
        return "No se ha encontrado ningún evento."

    
    # Listar eventos activos
    def listar_eventos(self):
        if not self.eventos:
            return ["No hay misiones activas."]        
        return [str(e) for e in self.eventos]

    def mostrar_detalles_evento(self, id_evento):
        evento = next((ev for ev in self.eventos if ev.id_mision == id_evento), None)
        if not evento:
            print("La misión seleccionada no existe.")
            return
        print("\n=== DETALLES DE LA MISIÓN ===\n")
        print(f"Nombre: {evento.nombre}")
        print(f"Rango: {evento.cazador.rango_nombre}")
        print(f"Arma: {evento.cazador.arma_nombre}")
        print(f"Objetos: {', '.join(evento.cazador.objetos)}")
        print(f"Día: {evento.dia_semana}")

    # Listar misiones canceladas
    def listar_canceladas(self):
        if not self.canceladas:
            return ["No hay misiones canceladas."]
        return [f"[{e.id_mision}] {e.nombre} | {e.cazador} | CANCELADA" for e in self.canceladas]


def menu():
    tablero = TableroMisiones()
    # Se muestran las distintas opciones de acción que puede hacer el usuario
    while True:
        limpiar_terminal()
        print("\n=== TABLERO DE MISIONES MONSTER HUNTER ===\n")
        print("1. Listar misiones disponibles")
        print("2. Planificar nueva misión")
        print("3. Listar misiones activas")
        print("4. Cancelar misión")
        print("5. Ver historial de misiones canceladas")
        print("6. Salir")
        # Elección de la opción deseada
        opcion = input("\nElige una opción: ")

        # Se muestra una lista de las misiones(eventos) que estén activos en ese momento
        if opcion == "1":            
            # Bucle para mostrar misiones y pedir una selección válida
            while True:                
                limpiar_terminal()
                tablero.mostrar_misiones()
                try:
                    seleccion = int(input("Elija una misión para ver los detalles o presione [0] para regresar al menú: "))
                    print("")
                    if seleccion == 0:
                        break  # Regresa al menú principal
                    else:
                        limpiar_terminal()
                        tablero.mostrar_detalles_mision(seleccion)
                        print("")
                        
                        while True:
                            entrada = input("Presione [0] para regresar al menú: ")
                            if entrada.strip() == "":
                                print("\nEntrada inválida. Tiene que escribir un número.")
                            else:
                                try:
                                    opcion_detalle = int(entrada)
                                    if opcion_detalle == 0:
                                        break  # vuelve al menú 2
                                    else:
                                        print("\nSolo debe presionar 0. Intente de nuevo.")
                                except ValueError:
                                    print("\nEntrada inválida. Tiene que escribir un número.")
                except ValueError:
                    print("\nEntrada inválida. Debes escribir un número.")        

        elif opcion == "2":
            limpiar_terminal()
            print("\n=== PLANIFICAR NUEVA MISIÓN ===\n")
            nombre = input("Nombre del cazador: ")

            # El usuario debe elegir el rango de cazador que guste, y esto afecta a las misiones que estén disponibles para ese rango
            while True:
                try:                    
                    tablero.mostrar_rangos()
                    rango_id = int(input("Elige tu rango (número): "))
                    if rango_id in dict(tablero.rangos):
                        rango_nombre = dict(tablero.rangos)[rango_id]
                        break
                    else:
                        print("Ese rango de cazador no existe. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

            # Aquí se elige la misión, aunque dependiendo del rango escogido anteriormente puede que algunas no sean accesibles
            while True:
                try:
                    tablero.mostrar_misiones()
                    mision_id = int(input("Elige la misión (número): "))
                    mision_dict = {m[0]: m for m in tablero.misiones_disponibles}
                    if mision_id not in mision_dict:
                        print("La misión seleccionada no ha sido encontrada. Intenta de nuevo.")
                        continue
                    _, nombre_m, rango_min, _, _, _, _ = mision_dict[mision_id]
                    if rango_id < rango_min:
                        print(f"Tu rango ({rango_nombre}) no alcanza para la misión '{nombre_m}'. Escoge otra misión.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

            # Se debe de seleccionar el arma con la que mejor crea que podrá desempeñar la misión
            while True:
                try:
                    tablero.mostrar_armas()
                    arma_id = int(input("Elige tu arma (número): "))
                    if arma_id in dict(tablero.armas):
                        arma_nombre = dict(tablero.armas)[arma_id]
                        break
                    else:
                        print("El arma seleccionada no existe. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

            # Se procede a elegir el/los objetos a llevar durante la misión
            objetos_lista = dict(tablero.objetos)
            while True:
                try:
                    tablero.mostrar_objetos()
                    seleccion = input("Elige uno o varios objetos separados por comas: ")
                    objetos_ids = [int(x.strip()) for x in seleccion.split(",")]
                    objetos_elegidos = [objetos_lista[i] for i in objetos_ids if i in objetos_lista]

                    # Aqué se validan los objetos según la misión, arma y objetos elegidos
                    valido = True
                    for obj in objetos_elegidos:
                        if not tablero.validar_objeto_mision(mision_id, obj, arma_nombre):
                            print("")
                            print(f"El objeto '{obj}' no está permitido en la misión '{nombre_m}'.")
                            valido = False
                            break

                        if not tablero.validar_objeto_arma(obj, arma_nombre):
                            print("")
                            print(f"El objeto '{obj}' no es compatible con el arma '{arma_nombre}'.")
                            valido = False
                            break

                    if valido and not tablero.validar_objeto_objeto(objetos_elegidos):
                        print("La combinación de objetos elegida no cumple las restricciones.")
                        valido = False

                    if valido:
                        break
                    else:
                        print("Vuelve a elegir los objetos correctamente.")
                except ValueError:
                    print("Entrada inválida. Debes escribir números separados por comas.")

            # Se muestran los días de la semana para la selección del usuario
            while True:
                try:
                    tablero.mostrar_dias()
                    dia_id = int(input("Elige el día de la semana: "))
                    if dia_id in dict(tablero.dias_semana):
                        dia_semana = dict(tablero.dias_semana)[dia_id]
                        break
                    else:
                        print("Ese día no existe. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

            cazador = Cazador(nombre, rango_id, rango_nombre, arma_id, arma_nombre, objetos_elegidos)
            resultado = tablero.planificar_evento(mision_id, cazador, dia_semana)
            limpiar_terminal()
            print("")
            print(resultado)

            while True:
                seleccion = input("\nPresione [0] para regresar al menú: ")
                if seleccion == "0":
                    break
                else:
                    print("\nSolo debe presionar [0]. Intenta de nuevo")
        # Se muestra la lista de misiones(eventos) que estén activos
        elif opcion == "3":  
            while True:
                limpiar_terminal()                
                print("\n=== MISIONES ACTIVAS ===\n")
                
                eventos = tablero.eventos

                if not eventos:
                    print("No hay misiones activas.\n")
                    while True:
                        try:
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:                                
                                print("\nSolo debe presionar [0]. Intenta de nuevo.")
                        except ValueError:                            
                            print("\nEntrada inválida. Debes escribir un número.")
                    break                  

        # Mostrar lista de misiones activas con cazador
                for e in eventos:
                    print(f"{e.id_mision}. {e.nombre} | {e.cazador.nombre}")

                print("")
                try:
                    seleccion = int(input("Elija una misión para ver los detalles o presione [0] para regresar al menú: "))
                    if seleccion == 0:
                        break
                    else:
                        limpiar_terminal()
                        tablero.mostrar_detalles_evento(seleccion)
                        while True:
                            entrada = input("\nPresione [0] para regresar al menú: ")
                            if entrada.strip() == "":
                                print("\nEntrada inválida. Tiene que escribir un número.")
                            else:                                
                                try:                                    
                                    opcion_detalle = int(entrada)
                                    if opcion_detalle == 0:
                                        break  # vuelve al menú de misiones activas
                                    else:
                                        print("\nSolo debe presionar 0. Intente de nuevo.")
                                except ValueError:
                                    print("Entrada inválida. Tiene que escribir un número.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")
        # Se le pide al usuario dar el nombre del cazador que haya dado y así eliminar la misión en la que esté siendo utilizado este
        elif opcion == "4":
            
            while True:
                limpiar_terminal()
                print("\n=== MISIONES ACTIVAS ===\n")
                eventos = tablero.listar_eventos()
                for e in eventos:
                    print(e)
                
                if eventos == ["No hay misiones activas."]:                    
                    while True:
                        try:
                            seleccion = int(input("\nPresione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("\nSolo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("\nEntrada inválida. Debe escribir un número.")
                    break

                confirmar = input("\n¿Está seguro que desea cancelar alguna misión? (si/no): ").strip().lower()

                if confirmar == "si":
                    print("")    
                    while True:
                        try:
                            id_mision = int(input("ID de la misión a cancelar: "))# El ID de la misión no es el de l misión original sino el que obtiene al crear el evento
                            break
                        except ValueError:
                            print("Entrada inválida. Debes escribir un número.")
                    resultado = tablero.cancelar_evento(id_mision)
                    print("")
                    print(resultado)

                    #
                    while True:
                        try:
                            print("")
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("\nSolo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("\nEntrada inválida. Debe escribir un número.")
                    break

                elif confirmar == "no":
                    while True:
                        try:
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("\nSolo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("\nEntrada inválida. Debe escribir un número.")
                    break
                else:
                    print("\nEntrada inválida. Escriba 'si' o 'no'.")                
        # Muestra una lista o historial de las misiones que han sido canceladas (eventos eliminados)
        elif opcion == "5": 
            limpiar_terminal()  
            while True:
                print("\n=== HISTORIAL DE MISIONES CANCELADAS ===\n")
                for e in tablero.listar_canceladas():
                    print(e)
                    print("")
                while True:
                    try:
                        seleccion = int(input("Presione [0] para regresar al menú: "))
                        if seleccion == 0:
                            break
                        else:
                            print("\nSolo debe presionar [0]. Intenta de nuevo.")
                    except ValueError:
                        print("\nEntrada inválida. Debes escribir un número.")
                break

        elif opcion == "6":
            limpiar_terminal()
            print("¡Hasta la próxima cacería!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Punto de entrada
if __name__ == "__main__":
    menu()

