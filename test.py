import tkinter as tk
from tkinter import font
from tkinter import messagebox
import win32com.client
import os

ESTILOS = {
    # Estilos generales de la aplicación
    "bg_principal": "white",
    "color_texto_general": "black",
    "fuente_general": ("Segoe UI", 14),
    "tamaño_fuente_S": 10,
    "tamaño_fuente_M": 14,
    "tamaño_fuente_L": 16,
    "tamaño_fuente_XL": 18,

    # Estilos de la barra superior
    "bg_barra_superior": "#D3D3D3",
    "color_texto_menu": "black",
    "fuente_menu": "Segoe UI",
    "relief_menu": "flat",
    "activebg_menu": "#C0C0C0",

    # Estilos botón ventana principal (pantalla principal)
    "bg_boton_principal": "#9B3B8B",
    "fg_boton_principal": "white",
    "relief_boton_principal": "flat",
    "activebg_boton_principal": "#8B2B7B",
    "padx_boton_principal": 20,
    "pady_boton_principal": 10,

    # Estilos del footer
    "bg_footer": "white",
    "bg_bloque_rojo": "#FF2D2D",
    "bg_bloque_naranja": "#FFB347",
    "bg_bloque_morado": "#9B3B8B",

    # Estilos específicos de la pantalla de entrada (input)
    "bg_pantalla_input": "#C5ABD2",
    "color_fondo_menu_input": "#D9D9D9",
    "color_input_bg": "#BFBFBF",
    "color_btn_input": "#96378C",
    "color_texto_btn_input": "white",
    "relief_btn_input": "flat",
    "fuente_btn_input": ("Segoe UI", 12, "bold"),
    "color_borde_btn_input": "white",
    "fuente_titulo_input": ("Segoe UI", 14, "bold"),
}

class MiInterfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BC Ripley automation")
        self.geometry("720x480")
        self.configure(bg=ESTILOS["bg_principal"])
        self.fuente_grande = font.Font(family=ESTILOS["fuente_general"][0], size=ESTILOS["tamaño_fuente_M"])
        self.ruta_archivo_input = ""
        self.macro_input = ""

        self.barra_superior = tk.Frame(self, bg=ESTILOS["bg_barra_superior"], height=40)
        self.barra_superior.pack(side="top", fill="x")

        boton_menu = tk.Menubutton(
            self.barra_superior,
            text="Menú",
            font=font.Font(family=ESTILOS["fuente_menu"][0], size=ESTILOS["tamaño_fuente_M"]),
            bg=ESTILOS["bg_barra_superior"],
            fg=ESTILOS["color_texto_menu"],
            relief=ESTILOS["relief_menu"],
            activebackground=ESTILOS["activebg_menu"]
        )
        boton_menu.pack(side="left", padx=10, pady=5)

        menu_opciones = tk.Menu(boton_menu, tearoff=0, font=self.fuente_grande)
        menu_opciones.add_command(label="Abrir Otra Pantalla", command=self.mostrar_pantalla_input)
        menu_opciones.add_command(label="Volver a Principal", command=self.mostrar_pantalla_principal)
        menu_opciones.add_command(label="Opción 2 (sin acción)", command=self.mostrar_advertencia)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.quit)
        boton_menu.config(menu=menu_opciones)

        self.contenedor_principal = tk.Frame(self) # Contenedor para las diferentes "páginas"
        self.contenedor_principal.pack(fill="both", expand=True)

        self.pantalla_principal = self.crear_pantalla_principal()
        self.pantalla_input = self.crear_pantalla_input()

        self.pantalla_principal.place(in_=self.contenedor_principal, x=0, y=0, relwidth=1, relheight=1)
        self.pantalla_input.place(in_=self.contenedor_principal, x=0, y=0, relwidth=1, relheight=1)

        self.mostrar_pantalla_principal() # Mostrar la primera pantalla

        self.footer = tk.Frame(self, height=60, bg=ESTILOS["bg_footer"])
        self.bloque_rojo = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_rojo"])
        self.bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
        self.bloque_naranja = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_naranja"])
        self.bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)
        self.bloque_morado = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_morado"])
        self.bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)
        self.footer.pack(side="bottom", fill="x")

    def crear_pantalla_principal(self):
        pantalla = tk.Frame(self.contenedor_principal, bg=ESTILOS["bg_principal"])
        boton_estilizado = tk.Button(
            pantalla,
            text="Ejecutar",
            command=self.ejecutar_macro,
            font=self.fuente_grande,
            bg=ESTILOS["bg_boton_principal"],
            fg=ESTILOS["fg_boton_principal"],
            relief=ESTILOS["relief_boton_principal"],
            activebackground=ESTILOS["activebg_boton_principal"],
            padx=ESTILOS["padx_boton_principal"],
            pady=ESTILOS["pady_boton_principal"]
        )
        boton_estilizado.pack(pady=100)
        return pantalla

    def crear_pantalla_input(self):
        pantalla_input = tk.Frame(self.contenedor_principal, bg=ESTILOS["bg_principal"]) # Considera usar ESTILOS["bg_pantalla_input"]

        tk.Label(pantalla_input, text="INPUT", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_titulo_input"]).grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Fila para "Ruta archivo"
        tk.Label(pantalla_input, text="Ruta archivo", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"]).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada1 = tk.Entry(pantalla_input, bg=ESTILOS["color_input_bg"], font=ESTILOS["fuente_general"])
        self.entrada1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Reemplazado fill="x" con sticky="ew"

        # Fila para "Macro"
        tk.Label(pantalla_input, text="Macro", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"]).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada2 = tk.Entry(pantalla_input, bg=ESTILOS["color_input_bg"], font=ESTILOS["fuente_general"])
        self.entrada2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")  # Reemplazado fill="x" con sticky="ew"

        btn_asignar = tk.Button(
            pantalla_input,
            text="Asignar",
            command=self.validar_datos_input,  # Asignar la función de validación al botón
            bg=ESTILOS["color_btn_input"],
            fg=ESTILOS["color_texto_btn_input"],
            relief=ESTILOS["relief_btn_input"],
            font=ESTILOS["fuente_btn_input"],
            width=10,  # Ajusta el ancho
            height=2   # Ajusta la altura, aunque grid controla el tamaño también
        )
        btn_asignar.grid(row=3, column=1, padx=(40), pady=20, sticky="e")

        # Configurar el peso de las columnas para que la entrada se expanda
        pantalla_input.columnconfigure(1, weight=1)

        return pantalla_input

    def validar_datos_input(self):
        ruta_archivo = self.entrada1.get()
        macro = self.entrada2.get()

        if not ruta_archivo or not macro:
            messagebox.showerror("Error", "Por favor, ingrese datos en ambos campos.")
        else:
            self.ruta_archivo_input = ruta_archivo
            self.macro_input = macro
            print(f"Ruta del archivo introducida: {self.ruta_archivo_input}")
            print(f"Nombre de la macro introducida: {self.macro_input}")
            # Aquí puedes llamar a la siguiente función para procesar los datos si es necesario inmediatamente
            # self.ejecutar_macro() # Podrías llamar ejecutar_macro aquí si "Asignar" siempre implica ejecutar
            self.mostrar_pantalla_principal() # Volver a la pantalla principal después de asignar

    def mostrar_pantalla_input(self):
        self.pantalla_input.tkraise()

    def mostrar_pantalla_principal(self):
        self.pantalla_principal.tkraise()

    def ejecutar_macro(self):
        if not self.ruta_archivo_input or not self.macro_input:
            messagebox.showerror("Error", "No se han asignado la ruta del archivo y/o la macro.")
            return

        try:
            ruta_archivo = self.ruta_archivo_input
            nombre_archivo = os.path.basename(ruta_archivo)
            macro_a_ejecutar = f"{nombre_archivo}!{self.macro_input}"
            print(f"Ejecutando macro: {macro_a_ejecutar}")

            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = True
            wb = excel.Workbooks.Open(ruta_archivo)
            excel.Application.Run(macro_a_ejecutar)
            wb.Save()
            wb.Close()
            excel.Quit()
            del excel
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al ejecutar la macro: {e}")

    def mostrar_advertencia(self):
        messagebox.showwarning("Advertencia", "Funcionalidad fuera de servicio, este software esta en fase de desarrollo.")

if __name__ == "__main__":
    app = MiInterfaz()
    app.mainloop()