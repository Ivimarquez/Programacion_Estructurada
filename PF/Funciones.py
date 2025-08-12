from fpdf import FPDF

def BorrarPantalla():
    import os
    os.system("cls")
    
def EspereTecla():
    input("\n\t🕒 Presione cualquier tecla para continuar... ")

def ValidacionCorreo(correo):
    import re
    expresion1=r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{3,}$"
    match=re.match(expresion1,correo)
    return bool(match)

def MenuPrincipal_Empleados():
    BorrarPantalla()
    print("\n\t\t\t...:: 🍬Bienvenid@ a Dulceria Las peris🍬 ::...")
    print("\n\t 1️⃣ ->👤➕ Registarse \n\t 2️⃣ ->🔐👤 Login \n\t 3️⃣ ->🚪 SALIR \n\t")
    opcion2=input("\t👉 Ingrese la opcion deseada del 1-3: ")
    return opcion2 

def Menu_Inventario_Ventas(Nombre,Apellidos):
    BorrarPantalla()
    print("\n\t\t\t...:: 🍬 Dulceria Las peris🍬 ::...")
    print(f"\n \t 👋 Bienvenid@ de nuevo {Nombre} {Apellidos}, has iniciado sesión ...")
    print("\n\t 1️⃣ ->📦 Ir a menu de inventario \n\t 2️⃣ ->💰 Ir a menu de ventas \n\t 3️⃣ ->🚪 SALIR \n\t")
    opcion2=input("\t👉 Ingrese la opcion deseada del 1-3: ")
    return opcion2 


def MenuPincipal_Inventario():
    BorrarPantalla()
    print("\n\t\t\t...:: 🍬 Dulceria Las peris🍬 ::...")
    print("\n\t 1️⃣ ->📝 Agregar productos al inventario \n\t 2️⃣ ->📄 Mostrar inventario \n\t 3️⃣ ->🔄 Modificar producto de inventario \n\t 4️⃣ ->🔍 Buscar productos en inventario \n\t 5️⃣ ->🗑️  Borrar producto del inventario \n\t 6️⃣ ->🚪 SALIR \n\t")
    opcion2=input("\t👉 Ingrese la opcion deseada del 1-6: ")
    return opcion2

def MenuVentas():
    BorrarPantalla()
    print("\n\t\t\t...:: 🍬 Dulceria Las peris🍬 ::...")
    print("\n\t 1️⃣ ->📝 Agregar registro de venta \n\t 2️⃣ ->📄 Mostrar registros de ventas \n\t 3️⃣ ->🔍 Buscar registros de ventas \n\t 4️⃣ ->🔄 Modificar registro de ventas\n\t 5️⃣ ->🗑️  Borrar registros de ventas \n\t 6️⃣ ->🚪 SALIR \n\t")
    opcion2=input("\t👉 Ingrese la opcion deseada del 1-6: ")
    return opcion2

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Inventario de Productos", ln=True, align="C")
        self.ln(5)

    def tabla_inventario(self, datos):
        self.set_font("Arial", "B", 10)
        headers = ["Codigo", "Id_empleado", "Nombre", "Categoria", "Precio", "Unidades", "Cantidad", "Caducidad"]
        col_widths = [25, 25, 30, 30, 15, 20, 20, 30]

        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C")
        self.ln()

        self.set_font("Arial", "", 9)
        for fila in datos:
            for i, item in enumerate(fila):
                self.cell(col_widths[i], 10, str(item), border=1, align="C")
            self.ln()

class PDF2(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Ventas", ln=True, align="C")
        self.ln(5)

    def tabla_ventas(self, datos):
        self.set_font("Arial", "B", 10)
        headers = ["Folio", "Id_empleado", "Codigo", "Nombre", "Cantidad", "Fecha", "Precio", "Subtotal", "IVA", "Total"]
        col_widths = [15, 26, 20, 24, 16, 20, 18, 18, 18, 18]

        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C")
        self.ln()

        self.set_font("Arial", "", 9)
        for fila in datos:
            for i, item in enumerate(fila):
                self.cell(col_widths[i], 10, str(item), border=1, align="C")
            self.ln()



