class Persona:
    estudiantes_reg = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("¡Hola! Soy", self.nombre)


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Persona.estudiantes_reg += 1

    def info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y estudio {self.carrera}")


class Administrativo(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre, None)  # No se necesita edad para un administrativo
        self.salario = salario

    def laborar(self):
        print("Solo estoy esperando la hora de salir")


class EstudianteAdmin(Estudiante, Administrativo):
    def __init__(self, nombre, edad, carrera, salario):
        Estudiante.__init__(self, nombre, edad, carrera)
        Administrativo.__init__(self, nombre, salario)


def ingresar_estudiantes():
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que desea registrar: "))
    estudiantes = []
    for _ in range(cantidad_estudiantes):
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))
        carrera = input("Carrera del estudiante: ")
        estudiantes.append(Estudiante(nombre, edad, carrera))
    return estudiantes


def ingresar_administrativos():
    cantidad_administrativos = int(input("Ingrese la cantidad de administrativos que desea registrar: "))
    administrativos = []
    for _ in range(cantidad_administrativos):
        nombre = input("Nombre del administrativo: ")
        salario = float(input("Salario del administrativo: "))
        administrativos.append(Administrativo(nombre, salario))
    return administrativos


while True:
    opcion = input("\n¿Qué desea hacer?\n1. Ingresar estudiantes\n2. Ingresar administrativos\n3. Salir\nOpción: ")

    if opcion == "1":
        estudiantes = ingresar_estudiantes()
        print("\nInformación de los estudiantes:")
        for estudiante in estudiantes:
            estudiante.saludar()  # Ahora se llama a la función saludar
            estudiante.info()

    elif opcion == "2":
        administrativos = ingresar_administrativos()
        print("\nInformación de los administrativos:")
        for administrativo in administrativos:
            administrativo.saludar()  # Ahora se llama a la función saludar
            print("Nombre:", administrativo.nombre, "Salario:", administrativo.salario)

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

            
            
        
  
     
    