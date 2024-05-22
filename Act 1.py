class JugadorDeFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero, goles=0, asistencias=0, amarillas=0, rojas=0):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numero = numero
        self.goles = goles
        self.asistencias = asistencias
        self.amarillas = amarillas
        self.rojas = rojas
        self.premios = []

    def actualizar_informacion(self, nombre=None, edad=None, posicion=None, equipo=None, pais=None, numero=None):
        if nombre: self.nombre = nombre
        if edad: self.edad = edad
        if posicion: self.posicion = posicion
        if equipo: self.equipo = equipo
        if pais: self.pais = pais
        if numero: self.numero = numero

    def actualizar_estadisticas(self, goles=0, asistencias=0, amarillas=0, rojas=0):
        self.goles += goles
        self.asistencias += asistencias
        self.amarillas += amarillas
        self.rojas += rojas
        self.actualizacion_estadisticas()

    def calcular_promedio_goles(self, partidos):
        if partidos == 0:
            return 0
        return self.goles / partidos

    def es_goleador(self):
        return self.goles > 20

    def agregar_premio(self, premio):
        self.premios.append(premio)

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)

    def actualizacion_estadisticas(self):
        print("Las estadísticas del jugador han sido actualizadas.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Posición: {self.posicion}")
        print(f"Equipo: {self.equipo}")
        print(f"País: {self.pais}")
        print(f"Número: {self.numero}")
        print(f"Goles: {self.goles}")
        print(f"Asistencias: {self.asistencias}")
        print(f"Tarjetas amarillas: {self.amarillas}")
        print(f"Tarjetas rojas: {self.rojas}")
        print(f"Premios: {', '.join(self.premios) if self.premios else 'Ninguno'}")


def menu():
    jugadores = {}

    while True:
        print("\nMenú de Interacción")
        print("1. Crear un nuevo jugador de fútbol")
        print("2. Mostrar la información de un jugador existente")
        print("3. Actualizar la información de un jugador existente")
        print("4. Calcular el promedio de goles por partido de un jugador")
        print("5. Verificar si un jugador es un goleador")
        print("6. Agregar un premio o reconocimiento a un jugador")
        print("7. Eliminar un premio o reconocimiento de un jugador")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            posicion = input("Posición: ")
            equipo = input("Equipo: ")
            pais = input("País: ")
            numero = int(input("Número: "))
            jugador = JugadorDeFutbol(nombre, edad, posicion, equipo, pais, numero)
            jugadores[nombre] = jugador
            print(f"Jugador {nombre} creado exitosamente.")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                jugador.mostrar_informacion()
            else:
                print("Jugador no encontrado.")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
                nueva_edad = input("Nueva edad (dejar en blanco para no cambiar): ")
                nueva_posicion = input("Nueva posición (dejar en blanco para no cambiar): ")
                nuevo_equipo = input("Nuevo equipo (dejar en blanco para no cambiar): ")
                nuevo_pais = input("Nuevo país (dejar en blanco para no cambiar): ")
                nuevo_numero = input("Nuevo número (dejar en blanco para no cambiar): ")

                jugador.actualizar_informacion(
                    nombre=nuevo_nombre or None,
                    edad=int(nueva_edad) if nueva_edad else None,
                    posicion=nueva_posicion or None,
                    equipo=nuevo_equipo or None,
                    pais=nuevo_pais or None,
                    numero=int(nuevo_numero) if nuevo_numero else None
                )
                print("Información actualizada correctamente.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                partidos = int(input("Número de partidos jugados: "))
                promedio = jugador.calcular_promedio_goles(partidos)
                print(f"El promedio de goles por partido de {nombre} es {promedio:.2f}.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '5':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                if jugador.es_goleador():
                    print(f"{nombre} es un goleador.")
                else:
                    print(f"{nombre} no es un goleador.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '6':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                premio = input("Ingrese el premio o reconocimiento: ")
                jugador.agregar_premio(premio)
                print(f"Premio '{premio}' agregado a {nombre}.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '7':
            nombre = input("Ingrese el nombre del jugador: ")
            jugador = jugadores.get(nombre)
            if jugador:
                premio = input("Ingrese el premio o reconocimiento a eliminar: ")
                jugador.eliminar_premio(premio)
                print(f"Premio '{premio}' eliminado de {nombre}.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '8':
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
