def borrarPantalla():
    import os
    os.system('cls')

def espereTecla():
    input("Presione una tecla para continuar...")

def menu_principal():
    print(" 📖 SISTEMA DE GESTION DE CALIFICACIONES 📖")
    print("1️⃣. Agregar Calificaciones")
    print("2️⃣. Mostrar Calificaciones")
    print("3️⃣. Calcular Promedios")
    print("4️⃣. Salir")
    opcion = input(" 👉 Seleccione una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre = input(" 👤 Nombre del alumno 👤: ") .upper() .strip()
    calificaciones=[]
    for i in range(1,4):
      continua = True
      while continua:
          try: 
              cal= float(input(f"Calificacion {i}: "))
              if cal>=0 and cal<=10:
                 calificaciones.append(cal)
                 continua = False
              else:
                 print("Ingrese un valor comprendido entre 0 y 10")
          except ValueError:
              print("Ingresa un valor numerico")
    lista.append([nombre] + calificaciones)
    print(" ✅ Accion realizada con exito ✅")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar Calificaciones")
    if len(lista) >0:
        print(f"  {'nombre':<15} {'calif.1':<10} {'calif.2':<10} {'calif.3':<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]:<15}  {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*60)
        cuantos = len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("No hay calificaciones en el sistema.")

def calcular_promedios(lista):
    borrarPantalla()
    print("Promedio de los alumnos")
    if len(lista) >0:
        print(f"{'nombre':<15} {'promedio':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
            nombre = fila[0]
            #promedio=(fila[1] + fila[2] + fila[3])/3
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15} {promedio:.2f}")
            promedio_grupal += promedio
        print("-"*40)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal:.2f}")
    else:
        print("No hay calificaciones en el sistema.")
