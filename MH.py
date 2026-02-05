# Función para limpiar la terminal
def limpiar_terminal():
    import os
    os.system('cls')
# Clase Cazador
class Cazador:
    def __init__(self, nombre, rango_id, rango_nombre, arma_id, arma_nombre):
        self.nombre = nombre
        self.rango_id = rango_id
        self.rango_nombre = rango_nombre
        self.arma_id = arma_id
        self.arma_nombre = arma_nombre

    def __str__(self):
        return f"{self.nombre} (Rango {self.rango_nombre}, Arma {self.arma_nombre})"


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
            (1, "Cazar Rathalos", 1),
            (2, "Defender la aldea", 1),
            (3, "Recolectar hierbas raras", 2),
            (4, "Derrotar al Tigrex", 3)
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
        # Lista de eventos activos y cancelados
        self.eventos = []
        self.canceladas = []
        self.next_id = 1

    
    # Mostrar recursos disponibles (rangos, armas, misiones, días)
    def mostrar_rangos(self):
        print("\nRangos disponibles:")
        for id_r, nombre_r in self.rangos:
            print(f"{id_r}. {nombre_r}")

    def mostrar_armas(self):
        print("\nArmas disponibles:")
        for id_a, nombre_a in self.armas:
            print(f"{id_a}. {nombre_a}")

    def mostrar_misiones(self):
        print("\nMisiones disponibles:")
        print("")
        
        for id_m, nombre_m, rango_min in self.misiones_disponibles:
            rango_nombre = dict(self.rangos)[rango_min]
            print(f"{id_m}. {nombre_m} (Rango mínimo: {rango_nombre})")
        print("")

    def mostrar_dias(self):
        print("\nDías disponibles:")
        for id_d, nombre_d in self.dias_semana:
            print(f"{id_d}. {nombre_d}")

    # Agregar una nueva misión al tablón de misiones
    def planificar_evento(self, mision_id, cazador, dia_semana):
        mision_dict = {m[0]: (m[1], m[2]) for m in self.misiones_disponibles}
        if mision_id not in mision_dict:
            return "Misión inválida."

        mision_nombre, rango_minimo = mision_dict[mision_id]

        # Restricción de rango mínimo, así se limita la entrada de cazadores novatos a misiones de rangos superiores
        if cazador.rango_id < rango_minimo:
            return f"El rango {cazador.rango_nombre} no es suficiente para '{mision_nombre}'."

        # Verificar conflictos de cazador y arma en el mismo día
        for evento in self.eventos:
            if evento.cazador.nombre == cazador.nombre and evento.dia_semana == dia_semana:
                    return f"El cazador {cazador.nombre} ya está en otra misión ese día."
            if evento.cazador.arma_id == cazador.arma_id and evento.dia_semana == dia_semana:
                    return f"El arma {cazador.arma_nombre} ya está en uso ese día."

        # Añadir misión o crear evento
        nuevo_evento = Mision(self.next_id, mision_nombre, dia_semana, cazador)
        self.eventos.append(nuevo_evento)
        self.next_id += 1
        return f"Misión '{mision_nombre}' asignada a {cazador.nombre} (Rango: {cazador.rango_nombre}, Arma: {cazador.arma_nombre}, Día: {dia_semana})"

    
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
        print("\n=== TABLERO DE MISIONES MONSTER HUNTER ===")
        print("")
        print("1. Listar misiones disponibles")
        print("2. Planificar nueva misión")
        print("3. Listar misiones activas")
        print("4. Cancelar misión")
        print("5. Ver historial de misiones canceladas")
        print("6. Salir")
        print("")
        # Elección de la opción deseada
        opcion = input("Elige una opción: ")

        # Se muestra una lista de las misiones(eventos) que estén activos en ese momento
        if opcion == "1":
            limpiar_terminal()
            # Bucle para mostrar misiones y pedir una selección válida
            while True:
                tablero.mostrar_misiones()
                try:
                    seleccion = int(input("Presione [0] para regresar al menú: "))
                    print("")
                    if seleccion == 0:
                        break  # Regresa al menú principal
                    else:
                        print("Solo debe presionar [0]. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")        

        elif opcion == "2":
            limpiar_terminal()
            print("")
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

            # Aquí se elige la misión, aunque dependiendo del rango escogido anteriormente puede que algunas no sean accesibles
            while True:
                try:
                    tablero.mostrar_misiones()
                    mision_id = int(input("Elige la misión (número): "))
                    if mision_id in {m[0] for m in tablero.misiones_disponibles}:
                        break
                    else:
                        print("La misión seleccionada no ha sido encontrada. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

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

            cazador = Cazador(nombre, rango_id, rango_nombre, arma_id, arma_nombre)
            resultado = tablero.planificar_evento(mision_id, cazador, dia_semana)
            print("")
            print(resultado)

            while True:
                print("")
                seleccion = input("Presione [0] para regresar al menú: ")
                if seleccion == "0":
                    break
                else:
                    print("Solo debe presionar [0]. Intenta de nuevo")
        # Se muestra la lista de misiones(eventos) que estén activos
        elif opcion == "3":            
            limpiar_terminal()
            while True:                
                print("\nMisiones activas:")
                print("")
                for e in tablero.listar_eventos():
                    print(e)
                print("")
                try:
                    seleccion = int(input("Presione [0] para regresar al menú: "))
                    if seleccion== 0:
                        break
                    else:
                        print("Solo debe presionar [0]. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")
        # Se le pide al usuario dar el nombre del cazador que haya dado y así eliminar la misión en la que esté siendo utilizado este
        elif opcion == "4":
            limpiar_terminal()
            while True:
                print("\nMisiones activas:")
                print("")
                eventos = tablero.listar_eventos()
                for e in eventos:
                    print(e)
                
                if eventos == ["No hay misiones activas."]:
                    
                    while True:
                        try:
                            print("")
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("")
                                print("Solo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("")
                            print("Entrada inválida. Debe escribir un número.")
                    break

                print("")
                confirmar = input("¿Está seguro que desea cancelar alguna misión? (si/no): ").strip().lower()

                if confirmar == "si":
                    print("")    
                    while True:
                        try:
                            id_mision = int(input("ID de la misión a cancelar: "))# El ID de la misión no es el de l misión original sino el que obtiene al crear el evento
                            break
                        except ValueError:
                            print("Entrada inválida. Debes escribir un número.")
                    resultado = tablero.cancelar_evento(nombre, id_mision)
                    print(resultado)

                    #
                    while True:
                        try:
                            print("")
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("Solo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("Entrada inválida. Debe escribir un número.")
                    break

                elif confirmar == "no":
                    while True:
                        try:
                            seleccion = int(input("Presione [0] para regresar al menú: "))
                            if seleccion == 0:
                                break
                            else:
                                print("Solo debes presionar [0]. Intenta de nuevo.")
                        except ValueError:
                            print("Entrada inválida. Debe escribir un número.")
                    break
                else:
                    print("Entrada inválida. Escriba 'si' o 'no'.")                
        # Muestra una lista o historial de las misiones que han sido canceladas (eventos eliminados)
        elif opcion == "5": 
            limpiar_terminal()           
            while True:                
                print("\nHistorial de misiones canceladas:")
                print("")
                for e in tablero.listar_canceladas():
                    print(e)
                print("")
                try:
                    seleccion = input("Presione [0] para regresar al menú: ")
                    if seleccion == "0":
                        break
                    else:
                        print("")
                        print("Solo debe presionar [0]. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes escribir un número.")

        elif opcion == "6":
            limpiar_terminal()
            print("¡Hasta la próxima cacería!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Punto de entrada
if __name__ == "__main__":

    menu()
