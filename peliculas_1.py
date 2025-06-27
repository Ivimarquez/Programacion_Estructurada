
#Dict u objeto que permita almacenar los sig atributos:(nombre,categoria,clasificación, genero,idioma) de peliculas

peliculas={
   "nombre":"",
   "categoria":"",
   "clasificacion":"",
   "genero":"",
   "idioma":"",
}

peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Presione una tecla para continuar...")

def agregarPeliculas():
   borrarPantalla()
   print("AGREGAR PELICULAS")
   peliculas.append(input("Ingrese el nombre de la pelicula: ").upper().strip())
   print("LA OPERACION SE REALIZO CON EXITO.")
   espereTecla()

def limpiarPeliculas():
    borrarPantalla()
    print("LIMPIAR O BORRAR TODAS LAS PELICULAS")
    resp=input("¿Deseas borrar todas las peliculas? (Si/No): ").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("LA OPERACION SE REALIZO CON EXITO.")

def buscarPeliculas():
   borrarPantalla()
   print("BUSCAR PELICULAS")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
   if not pelicula_buscar in peliculas:
      print("Esta pelicula a buscar no existe en el sistema")
   else:
      encontro=0
      for i in range (0,len (peliculas)):
          if pelicula_buscar==peliculas[i]:
             print(f"La pelicula {pelicula_buscar} se encuentro en el casillero {i+1} ")
             encontro=1
      print(f"tenemos (encontro) pelicula(s) con el titulo")
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

def mostrarPeliculas():
   borrarPantalla()
   print("MOSTRAR PELICULAS")
   if len(peliculas)==0:
      print("No hay peliculas para mostrar")
   else:
      print("Lista de peliculas:")
      for i in range(0,len(peliculas)):
         print(f"{i+1}. {peliculas[i]}")
   espereTecla()