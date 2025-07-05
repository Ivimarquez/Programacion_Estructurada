
#Dict u objeto que permita almacenar los sig atributos:(nombre,categoria,clasificación, genero,idioma) de peliculas

peliculas={
   "nombre":"",
   "categoria":"",
   "clasificacion":"",
   "genero":"",
   "idioma":"",
}

peliculas = [] 
pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Presione una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("AGREGAR PELICULAS")
    peliculas.update({"nombre": input ("Ingresa el nombre: ").upper().strip()})
    peliculas.update({"categoria": input ("Ingresa la categoria: ").upper().strip()})
    peliculas.update({"clasificacion": input ("Ingresa la clasificacion: ").upper().strip()})
    peliculas.update({"genero": input ("Ingresa el genero: ").upper().strip()})
    peliculas.update({"idioma": input ("Ingresa el idioma: ").upper().strip()})
    print("LA OPERACION SE REALIZO CON EXITO.")

def limpiarPeliculas():
    borrarPantalla()
    print("LIMPIAR O BORRAR TODAS LAS PELICULAS")
    resp=input("¿Deseas borrar todas las peliculas? (Si/No): ").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("LA OPERACION SE REALIZO CON EXITO.")

def modificarPeliculas():   
   borrarPantalla()
   print("MODIFICAR PELICULAS")
   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()    
   encontro=0
   if not pelicula_buscar in peliculas:
      print("No se encuentra la pelicula buscar: ")     
   else:
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
           resp=input("Desea actualizar la pelicula? (Si/No): ").lower().strip()
           if resp=="si":
              peliculas[i]=input("Introduce el nuevo nombre de la pelicula: ").upper().strip()
              encontro+=1
              print("LA OPERACION SE REALIZO CON EXITO.")
      print(f"Se modifico {encontro} pelicula(s) con el titulo {pelicula_buscar}")

def borrarPeliculas():
   borrarPantalla()
   print("BORRAR PELICULAS")
   pelicula_borrar=input("Ingrese el nombre de la pelicula que desea borrar: ").upper().strip()
   encontro=0
   if not pelicula_borrar in peliculas:
      print("No se encuetra la pelicula que desea borrar: ")
   else:
      for i in range(0,len(peliculas)):
         if pelicula_borrar==peliculas[i]:
            resp=input("¿Desea borrar la pelicula? (Si/No): ").lower().strip()
            if resp=="si":
                peliculas.remove(pelicula_borrar)

def agregarCaracteristicaPeliculas():
   borrarPantalla()
   print("AGREGAR CARACTERISTICA A PELICULAS")
   atributo=input("Ingrese el nombre de la nueva caracteristica que desea agregar: ").lower().strip()
   valor_atributo=input(f"Ingrese el valor de la nueva caracteristica que agregaste: ").upper().strip()
   #peliculas.update({atributo: valor_atributo})
   #peliculas["nombre"] = input("Ingrese el nombre: ").upper().strip()
   print("La operacion se realizo con exito.")

def modificarCaracteristicaPeliculas():
 borrarPantalla()
 print("MODIFICAR UNA CARACTERISTICA DE PELICULAS") 
 if len(peliculas)>0:
   for i in peliculas:
       print(f"{i}:  {peliculas[i]}")  
       resp=input(f"Deseas modificar el valor de la caracteristica {i}? (Si/No)") .lower() .strip()
       if resp=="si":
           valor=input(f"Ingresa el nuevo valor de la caracteristica{i}: ") .upper() .strip()
           peliculas[i]=valor
           print("La operacion se realizo con exito")  
           espereTecla()
 else:
     print("No hay peliculas en el sistema")

def borrarCaracteristicaPeliculas():
   borrarPantalla()
   print("Borrar Caracteristicas a Peliculas")
   if len(peliculas)>0:
      for i in peliculas:
       print(f"{i}:  {peliculas[i]}")  
       resp=input("Deseas borrar alguna caracteristica? (Si/No): ") .lower() .strip()
       if resp=="si":
          valor=input("Ingresa la caracteristica que deseas borrar o quitar: ") .upper() .strip()
          print("Operacion realizada con exito")
   else: 
      print("No hay peliculas en el sistema")

def mostrarPeliculas():
    borrarPantalla()
    print("MOSTRAR PELICULAS")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"{i + 1}: {peliculas[i]}")
    else:
        print("NO HAY PELICULAS EN ESTE MOMENTO EN EL SISTEMA")