import Funciones
from Empleados import empleado
from Productos import inventario
from Ventas import venta
import getpass
from tabulate import tabulate
from datetime import datetime
import os



def Main():
    opcion=True
    while opcion:
        Funciones.BorrarPantalla()
        opcion2=Funciones.MenuPrincipal_Empleados()
        if opcion2=="1" or opcion2=="REGISTRARSE":
            Funciones.BorrarPantalla()
            print("\n\t ..:: 👤➕ Registro de empleados  ::..")
            Nombre=input("\n\t👤 Ingrese su nombre: ").upper().strip()
            while Nombre=="":
                Nombre=input("\t⚠️ Ingrese un nombre Por favor: ").upper().strip()
            Apellidos=input("\t🧬 Ingrese su apellido: ").upper().strip()
            while Apellidos=="":
                Apellidos=input("\t⚠️ Debe ingresar apellidos Por favor : ").upper().strip()
            Correo=input("\t📧 Ingrese su correo: ").lower().strip()
            Validacion=Funciones.ValidacionCorreo(Correo)
            while Validacion==False:
                Correo=input("\t⚠️ Por favor ingrese un correo valido: ").lower().strip()
                Validacion=Funciones.ValidacionCorreo(Correo)
            Password=getpass.getpass("\t[::] Ingrese su contraseña con al menos 10  y maximo 14 caracteres: ").strip()
            while Password=="" or (len(Password)<10 or len(Password)>14):
                Password=getpass.getpass("\t[::] Debe ingresar una contraseña con al menos 10  y maximo 14 caracteres : ").strip()
            respuesta=empleado.AgregarEmpleado(Nombre,Apellidos,Correo,Password)
            if respuesta=="Correct":
                print(f"\n\t::: ✅ Se ha registrado {Nombre} {Apellidos} con exito :::")
            elif respuesta=="key duplicada":
                print("\n\t ⚠️  El correo ingresado ya existe en el sistema")
            elif respuesta==None:
                print("\n\t ❌ Hubo un error al intentar registrar al empleado , por favor intente de nuevo...")
            Funciones.EspereTecla()
       
        elif opcion2=="2" or opcion2=="LOGIN":
            Funciones.BorrarPantalla()
            print("\n \t ..:: 🔐👤 Inicio de sesion de empleados ::..")
            Correo=input("\n\t📧 Ingrese su correo: ").lower().strip()
            Validacion=Funciones.ValidacionCorreo(Correo)
            while Validacion==False:
                Correo=input("\t⚠️ Por favor ingrese un correo valido: ").lower().strip()
                Validacion=Funciones.ValidacionCorreo(Correo)
            Password=getpass.getpass("\t[::] Ingrese su contraseña: ").strip()
            while Password=="" or (len(Password)<10 or len(Password)>14):
                Password=getpass.getpass("\t[::] Debe ingresar una contraseña con al menos 10  y maximo 14 caracteres : ").strip()
            lista_empleados=empleado.Inicio_sesion(Correo,Password)
            try:
                if len(lista_empleados)>0:
                    Menu_Inventario_Ventas(lista_empleados[0],lista_empleados[1],lista_empleados[2])
                else:
                    print("\n\t⚠️  Hubo un error al intentar iniciar sesion.Por favor intente de nuevo")
            except TypeError:
               print("\n\t⚠️  E-mail y/o contraseña incorrectas.Por favor intente de nuevo")

            Funciones.EspereTecla()
        elif opcion2=="3" and opcion2=="SALIR":
            print("\n\t🎉 Terminaste la ejecucion del Sistema...Gracias...")
            opcion=False
        else:
            print("\n\t ⚠️ Opcion invalida por favor intenta de nuevo")
            Funciones.EspereTecla()


def Menu_Inventario_Ventas(Id_empleado,Nombre_empleado,Apellidos):
    Funciones.BorrarPantalla()
    opcion=True
    while opcion:
        opcion2=Funciones.Menu_Inventario_Ventas(Nombre_empleado,Apellidos)
        if opcion2=="1" or opcion2=="INVENTARIO":
            #OPCION INVENTARIO
            Funciones.BorrarPantalla()
            op=True
            while op:
                op2=Funciones.MenuPincipal_Inventario()
                if op2=="1" or op2=="AGREGAR":
                    Funciones.BorrarPantalla()
                    print("\n\t\t ..:: 📝 Agregar Productos ::..\n")
                    nombre=input("\n\t 🍬 Ingrese el nombre del producto: ").upper().strip()
                    while nombre=="":
                        nombre=input("\t ⚠️ Por favor debe ingresar el nombre del producto: ").upper().strip()
                    categoria=input("\t 🔖 Ingrese la categoria del producto: ").upper().strip()
                    while categoria=="":
                        categoria=input("\t ⚠️ Por favor debe ingresar la categoria del producto: ").upper().strip()
                    cantidad=input("\t 🔢 Ingrese la cantidad de gramos por unidad: ")
                    while cantidad=="":
                        cantidad=input("\t ⚠️ Por favor debe ingresar la cantidad de gramos por unidad: ").upper().strip()
                    codigo=input("\t ▍▎▎▍Ingrese el codigo del producto del 8-12 digitos: ").strip()
                    while (len(codigo)==0) or (len(codigo)<8 or len(codigo)>10):
                        codigo=input("\t ⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").strip()
                    continua=True
                    while continua:
                        try:
                            precio=float(input("\t💲 Ingrese el precio del producto: "))
                            continua=False
                        except ValueError:
                            print("\t ⚠️ Por favor ingrese datos numericos en precio ")
                    continua2=True
                    while continua2:
                        try:
                            unidades=float(input("\t🔢 Ingrese la cantidad de unidades del producto: "))
                            continua2=False
                        except ValueError:
                            print("\t ⚠️ Por favor ingrese datos numericos en cantidad de unidades ")
                    continua3=True
                    while continua3:
                        try:
                            fecha=input("\t📆 Ingrese la caducidad del producto AAAA-MM-DD (ej. 2025-12-01): ").upper().strip()
                            caducidad = datetime.strptime(fecha, "%Y-%m-%d")
                            continua3=False
                        except ValueError:
                                print("\t ⚠️ Por favor ingrese correctamente la fecha de caducidad AAAA-MM-DD")
                    respuesta=inventario.AgregarProducto(codigo,Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad)
                    if respuesta:
                        print(f"\n\t ::: ✅ Se ha registrado el producto con exito :::")
                    else:
                        print("\n\t ❌ Hubo un error al intentar registrar el producto , por favor intente de nuevo...")
                    Funciones.EspereTecla()

                elif op2=="2" or op2=="MOSTRAR":
                    Funciones.BorrarPantalla()
                    print("\n\t\t\t\t\t ..:: 📄 Mostrar inventario ::..")
                    Lista_inventario=inventario.MostrarProductos()
                    try:
                        if len(Lista_inventario)>0:
                            importar=input("\n\tDesea exportar la tabla a PDF? si/no?: ").strip().upper()
                            while importar!="SI" and importar!="NO":
                                importar=input("\tDesea exportar la tabla a PDF? Debe contestar si/no: ").strip().upper()
                            if importar=="SI":
                                from Funciones import PDF
                                pdf = PDF()
                                pdf.add_page()
                                pdf.tabla_inventario(Lista_inventario)
                                pdf.output("inventario.pdf")
                                os.startfile("inventario.pdf")
                            elif importar=="NO":
                                headers = ["Código", "ID Empleado", "Nombre", "Categoría", "Precio", "Unidades", "Cantidad", "Caducidad"]
                                data =Lista_inventario
                                print(tabulate(data, headers=headers, tablefmt="grid"))
                        else:
                            print("\t ⚠️ No hay productos en el inventario ")
                    except TypeError:
                        print("\t ⚠️ Hubo un error al intentar consultar el inventario.Por favor intente de nuevo... ")

                    Funciones.EspereTecla()

                elif op2=="3" or op2=="MODIFICAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 🔄 Modificar producto de inventario ::..")
                    codigo=input("\n\t ▍▎▎▍ Ingrese el codigo del producto que desea modificar: ").strip()
                    while (len(codigo)==0) or (len(codigo)<8 or len(codigo)>10):
                        codigo=input("\t ⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").strip()
                    Funciones.BorrarPantalla
                    lista_producto=inventario.BuscarProductos(codigo)
                    try:
                        if len(lista_producto)>0:
                            headers = ["Código", "ID Empleado", "Nombre", "Categoría", "Precio", "Unidades", "Cantidad", "Caducidad"]
                            data =lista_producto
                            print(tabulate([data], headers=headers, tablefmt="grid"))
                            resp=input("\n\t ⚠️ Desea realmente modificar el producto si/no: ").upper().strip()
                            while resp!="SI" and resp!="NO":
                                resp=input("\t ⚠️ Desea realmente modificar el producto, debe responder si/no: ").upper().strip()
                            if resp=="SI":
                                nombre=input("\t 🍬 Ingrese el nombre del producto: ").upper().strip()
                                while nombre=="":
                                    nombre=input("\t ⚠️ Por favor debe ingresar el nombre del producto: ").upper().strip()
                                categoria=input("\t 🔖 Ingrese la categoria del producto: ").upper().strip()
                                while categoria=="":
                                    categoria=input("\t ⚠️ Por favor debe ingresar la categoria del producto: ").upper().strip()
                                cantidad=input("\t 🔢 Ingrese la cantidad de gramos por unidad: ")
                                while cantidad=="":
                                    cantidad=input("\t ⚠️ Por favor debe ingresar la cantidad de gramos por unidad: ").upper().strip()
                                continua=True
                                while continua:
                                    try:
                                        precio=float(input("\t💲 Ingrese el precio del producto: "))
                                        continua=False
                                    except ValueError:
                                        print("\t ⚠️ Por favor ingrese datos numericos en precio ")
                                continua2=True
                                while continua2:
                                    try:
                                        unidades=float(input("\t🔢 Ingrese la cantidad de unidades del producto: "))
                                        continua2=False
                                    except ValueError:
                                        print("\t ⚠️ Por favor ingrese datos numericos en cantidad de unidades ")
                                continua3=True
                                while continua3:
                                    try:
                                        fecha=input("\t📆 Ingrese la caducidad del producto AAAA-MM-DD (ej. 2025-12-01): ").upper().strip()
                                        caducidad = datetime.strptime(fecha, "%Y-%m-%d").date()
                                        continua3=False
                                    except ValueError:
                                            print("\t ⚠️ Por favor ingrese correctamente la fecha de caducidad AAAA-MM-DD")
                                respuesta=inventario.ModificarProducto(Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad,codigo)
                                if respuesta==True:
                                    print(f"\n\t ::: ✅ Se ha modificado el producto con exito :::")
                                else:
                                    print("\n\t ❌ Hubo un error al intentar modificar el producto.Por favor intente de nuevo...")
                        else:
                            print("\n\t ⚠️ Hubo un error al intentar buscar el producto.Por favor intente de nuevo...")
                    except TypeError:
                        print("\t ⚠️ No se encontro el producto con ese codigo.Por favor intente de nuevo...")
                    Funciones.EspereTecla()
                    
                elif op2=="4" or op2=="BUSCAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 🔍 Buscar productos en inventario  ::..")
                    codigo=input("\n\t ▍▎▎▍ Ingrese el codigo del producto que desea buscar: ").strip()
                    while (len(codigo)==0) or (len(codigo)<8 or len(codigo)>10):
                        codigo=input("\t ⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").strip()
                    lista_buscar=inventario.BuscarProductos(codigo)
                    Funciones.BorrarPantalla()
                    try:
                        if len(lista_buscar)>0:
                            headers = ["Código", "ID Empleado", "Nombre", "Categoría", "Precio", "Unidades", "Cantidad", "Caducidad"]
                            data =lista_buscar
                            print(tabulate([data], headers=headers, tablefmt="grid"))
                            Funciones.EspereTecla
                        else:
                            print("\n\t ❌ Hubo un error al buscar el producto.Por favor intente de nuevo...")                    
                    except TypeError:
                       print("\t ⚠️  Producto no encontrado.Por favor intente de nuevo ")
                    Funciones.EspereTecla()

                elif op2=="5" or op2=="BORRAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 🗑️  Borrar producto en inventario  ::..")
                    codigo=input("\n\t ▍▎▎▍ Ingrese el codigo del producto que desea borrar: ").strip()
                    while (len(codigo)==0) or (len(codigo)<8 or len(codigo)>10):
                        codigo=input("\n\t ⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").strip()
                    conf=venta.ProductoInVenta(codigo)
                    if conf==True:
                        print("\n\t ⚠️  Para eliminar el producto del inventario debera eliminar antes su venta correspondiente ")
                        return
                    else:
                        lista_producto=inventario.BuscarProductos(codigo)
                        try:
                            if len(lista_producto)>0:
                                headers = ["Código", "ID Empleado", "Nombre", "Categoría", "Precio", "Unidades", "Cantidad", "Caducidad"]
                                data =lista_producto
                                print(tabulate([data], headers=headers, tablefmt="grid"))
                                resp=input("Desea continuar si/no: ").upper().strip()
                                while resp!="SI" and resp!="NO":
                                    resp=input("Desea continuar debe responder si/no: ").upper().strip()
                                if resp=="SI":
                                    lista_producto=inventario.BorrarProducto(codigo)
                                elif resp=="NO":
                                    print()
                        except TypeError:
                            print("\t ⚠️  Producto no encontrado en inventario ")
                    Funciones.EspereTecla()

                elif op2=="6" or op2=="SALIR":
                    Funciones.BorrarPantalla()
                    print("\n\t🎉 Terminaste la ejecucion del Sistema...Gracias...")
                    op=False

                else:
                    print("\n\t ⚠️ Opcion invalida por favor intenta de nuevo")
                    Funciones.EspereTecla()

        #OPCION VENTAS
        elif opcion2=="2" or opcion2=="VENTAS":
            Funciones.BorrarPantalla()
            op=True
            while op:
                op2=Funciones.MenuVentas()
                if op2=="1" or op2=="AGREGAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 📝 Agregar registro de venta  ::..")
                    Id_producto=input("\n\t  ▍▎▎▍ Ingrese el codigo del producto: ").strip()
                    while (len(Id_producto)==0) or (len(Id_producto)<8 or len(Id_producto)>10):
                        Id_producto=input("\n\t ⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").strip()
                    continua2=True
                    while continua2:
                        try:
                            cantidad_productos=int(input("\n\t 🔢 Ingrese la cantidad de productos: "))
                            continua2=False
                        except ValueError:
                            print("\t ⚠️ Por favor ingrese datos numericos en cantidad de productos")
                    resp3=inventario.BuscarProductos(Id_producto)
                    try:
                        if len(resp3)>0:
                            subtotal=cantidad_productos*float(resp3[4])
                            iva=subtotal*.16
                            total=subtotal+iva
                            resp4=venta.AgregarVenta(Id_empleado,Id_producto,resp3[2],cantidad_productos,resp3[4],subtotal,iva,total)
                            if resp4:
                                print(f"\n\t ::: ✅ Se ha registrado la venta con exito :::")
                                n=inventario.VentaProducto(Id_producto,cantidad_productos)
                                print(n)
                            else:
                                print("\n\t ❌ Hubo un error al intentar registrar la venta .Por favor intente de nuevo...")
                    except TypeError:
                        print("\n\t ⚠️ Por favor ingrese ventas de productos existentes en inventario")

                    Funciones.EspereTecla()

                elif op2=="2" or op2=="MOSTRAR":
                    Funciones.BorrarPantalla()
                    print("\n\t\t\t\t\t\t ..:: 📄 Mostrar ventas ::..")
                    Lista_ventas=venta.MostrarVentas()
                    try:
                        if len(Lista_ventas)>0:
                            importar=input("\n\tDesea exportar la tabla a PDF? si/no?: ").strip().upper()
                            while importar!="SI" and importar!="NO":
                                importar=input("\tDesea exportar la tabla a PDF? Debe contestar si/no: ").strip().upper()
                            if importar=="SI":
                                from Funciones import PDF2
                                pdf = PDF2()
                                pdf.add_page()
                                pdf.tabla_ventas(Lista_ventas)
                                pdf.output("ventas.pdf")
                                os.startfile("ventas.pdf")
                            elif importar=="NO":
                                headers =["Folio","Id_empleado","Codigo", "Nombre","Cantidad","Fecha","Precio","Subtotal","IVA","Total"]
                                data =Lista_ventas
                                print(tabulate(data, headers=headers, tablefmt="grid"))
                        else:
                            print("\t ⚠️  No hay ventas registradas ")
                    except TypeError:
                        print("\t ❌ Hubo un error al intentar consultar las ventas .Por favor intente de nuevo...")

                    Funciones.EspereTecla()

                elif op2=="3" or op2=="BUSCAR":
                    Funciones.BorrarPantalla()
                    print("\n\t\t..:: 🔍 Buscar ventas  ::..")
                    folio=input("\n\t🧾 Ingrese el folio de la venta que desea buscar: ").strip()
                    while (len(folio)==0):
                        folio=input("\t ⚠️ Por favor debe ingresar un folio ").strip()
                    lista_buscar=venta.BuscarVenta(folio)
                    Funciones.BorrarPantalla()
                    try:
                        if len(lista_buscar)>0:
                            headers =["Folio","Id_empleado","Codigo", "Nombre","Cantidad","Fecha","Precio","Subtotal","IVA","Total"]
                            data =lista_buscar 
                            print(tabulate([data], headers=headers, tablefmt="grid"))
                            input("\n\t 🕒 Presione cualquier tecla para continuar... ")
                        else:
                            print("\t ❌ Hubo un error al intentar consultar la venta .Por favor intente de nuevo...")
                    except TypeError:
                        print(f"\t ⚠️ No se encontraron ventas con el folio {folio}")
                    Funciones.EspereTecla

                elif op2=="4" or op2=="MODIFICAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 🔄 Modificar producto de inventario ::..")
                    folio=input("\n\t🧾 Ingrese el folio de la venta que desea modificar: ").strip()
                    while (len(folio)==0):
                        folio=input("\t ⚠️ Por favor debe ingresar un folio").strip()
                    lista_buscar=venta.BuscarVenta(folio)
                    Funciones.BorrarPantalla()
                    try:
                        if len(lista_buscar)>0:
                            headers =["Folio","Id_empleado","Codigo", "Nombre","Cantidad","Fecha","Precio","Subtotal","IVA","Total"]
                            data =lista_buscar 
                            print(tabulate([data], headers=headers, tablefmt="grid"))
                            conf2=input("\n\t Desea continuar modificando la venta? si/no: ").upper().strip()
                            while conf2!="SI" and conf2!="NO":
                                conf2=input("\t ⚠️ Desea continuar modificando la venta? Debe contestar si/no: ").upper().strip()
                            if conf2=="SI":
                                continua2=True
                                while continua2:
                                    try:
                                        cantidad_productos=int(input("\t 🔢 Ingrese la cantidad de productos: "))
                                        continua2=False
                                    except ValueError:
                                        print("\t ⚠️ Por favor ingrese datos numericos en cantidad de productos")
                                continua3=True
                                while continua3:
                                    try:
                                        fecha1=input("\t📆 Ingrese la fecha de la venta AAAA-MM-DD (ej. 2025-12-01): ").upper().strip()
                                        fecha = datetime.strptime(fecha1, "%Y-%m-%d")
                                        continua3=False
                                    except ValueError:
                                        print("\t ⚠️ Por favor ingrese correctamente la fecha de la venta AAAA-MM-DD")
                                resp3=inventario.BuscarProductos(lista_buscar[2])
                                subtotal=cantidad_productos*float(resp3[4])
                                iva=subtotal*.16
                                total=subtotal+iva
                                resultado=venta.ModificarVenta(cantidad_productos,fecha,subtotal,iva,total,lista_buscar[0])
                                if resultado==True:
                                    print(f"\n\t ::: ✅ Se ha modificado la venta con exito :::")
                                elif resultado==False:
                                    print("\t ❌ Hubo un error al intentar modificar la venta .Por favor intente de nuevo...")
                            elif conf2=="NO":
                                print()
                        else:
                            print("\t ❌ Hubo un error al intentar consultar la venta .Por favor intente de nuevo...")
                    except TypeError:
                        print(f"\t ⚠️ No se encontraron ventas con el folio {folio}")
                    Funciones.EspereTecla()


                elif op2=="5" or op2=="BORRAR":
                    Funciones.BorrarPantalla()
                    print("\n\t ..:: 🗑️ Borrar registros de ventas ::..")
                    folio=input("\n\t🧾 Ingrese el folio de la venta que desea modificar: ").strip()
                    while (len(folio)==0):
                        folio=input("\t ⚠️ Por favor debe ingresar un folio").strip()
                    lista_ventas=venta.BuscarVenta(folio)
                    Funciones.BorrarPantalla()
                    try:
                        if len(lista_ventas)>0:
                            headers =["Folio","Id_empleado","Codigo", "Nombre","Cantidad","Fecha","Precio","Subtotal","IVA","Total"]
                            data =lista_ventas
                            print(tabulate([data], headers=headers, tablefmt="grid"))
                            confirmacion=input("Desea realmente borrar el registro de la venta? si/no: ").strip().upper()
                            while confirmacion!="SI" and confirmacion!="NO":
                                confirmacion=input("⚠️ Desea continuar modificando la venta? Debe contestar si/no: ").upper().strip()
                            if confirmacion=="SI":
                                venta.BorrarVenta(folio)
                            elif confirmacion=="NO":
                                print()
                    except TypeError:
                        print(f"\t ⚠️ No se encontraron ventas con el folio {folio}")
                    Funciones.EspereTecla()

                elif op2=="6" or op2=="SALIR":
                        Funciones.BorrarPantalla()
                        print("\n\t🎉 Terminaste la ejecucion del Sistema...Gracias...")
                        op=False
                        
                else:
                    print("\n\t ⚠️ Opcion invalida por favor intenta de nuevo")
                    Funciones.EspereTecla()
        #OPCION SALIR
        elif opcion2=="3" or opcion2=="SALIR":
            Funciones.BorrarPantalla()
            print("\n\t🎉 Terminaste la ejecucion del Sistema...Gracias...")
            opcion=False

        else:
            print("\n\t ⚠️ Opcion invalida por favor intenta de nuevo")
            Funciones.EspereTecla()


Main()   
