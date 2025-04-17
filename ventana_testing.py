import tkinter as tk
from tkinter import font
from tkinter import messagebox
import win32com.client
import os
from ventana_final2 import Open_ventana_input

ESTILOS = {
    "bg_principal": "white",
    "bg_barra_superior": "#D3D3D3",
    "color_texto_menu": "black",
    "fuente_menu": ("Segoe UI", 14),
    "relief_menu": "flat",
    "activebg_menu": "#C0C0C0",
    "bg_boton_principal": "#9B3B8B",
    "fg_boton_principal": "white",
    "relief_boton_principal": "flat",
    "activebg_boton_principal": "#8B2B7B",
    "padx_boton_principal": 20,
    "pady_boton_principal": 10,
    "bg_footer": "white",
    "bg_bloque_rojo": "#FF2D2D",
    "bg_bloque_naranja": "#FFB347",
    "bg_bloque_morado": "#9B3B8B",
    "fuente_general": ("Segoe UI", 14) # Fuente utilizada para otros elementos
}

class MiInterfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BC Ripley automation")
        self.geometry("720x480")
        self.configure(bg=ESTILOS["bg_principal"])
        self.fuente_grande = font.Font(family=ESTILOS["fuente_general"][0], size=ESTILOS["fuente_general"][1])

        # --- Menú superior tipo barra (simulada) ---
        barra_superior = tk.Frame(self, bg=ESTILOS["bg_barra_superior"], height=40)
        barra_superior.pack(side="top", fill="x")

        boton_menu = tk.Menubutton(
            barra_superior,
            text="Menú",
            font=font.Font(family=ESTILOS["fuente_menu"][0], size=ESTILOS["fuente_menu"][1]),
            bg=ESTILOS["bg_barra_superior"],
            fg=ESTILOS["color_texto_menu"],
            relief=ESTILOS["relief_menu"],
            activebackground=ESTILOS["activebg_menu"]
        )
        boton_menu.pack(side="left", padx=10, pady=5)

        menu_opciones = tk.Menu(boton_menu, tearoff=0, font=self.fuente_grande)
        menu_opciones.add_command(label="Abrir Otra Pantalla", command=self.mostrar_otra_pantalla)
        menu_opciones.add_command(label="Opción 2 (sin acción)", command=self.mostrar_advertencia)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.quit)
        boton_menu.config(menu=menu_opciones)

        # --- Contenido de la pantalla principal ---
        self.pantalla_principal = tk.Frame(self, bg=ESTILOS["bg_principal"])
        boton_estilizado = tk.Button(
            self.pantalla_principal,
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
        self.pantalla_principal.pack(fill="both", expand=True) # Mostrar inicialmente

        # --- Inicializar la otra pantalla (pero no mostrarla) ---
        #self.otra_pantalla = Open_ventana_input(self)
        #self.aplicar_estilos_otra_pantalla() # Aplicar estilos a la otra pantalla

        # --- Footer (se mantiene visible en ambas pantallas) ---
        self.footer = tk.Frame(self, height=60, bg=ESTILOS["bg_footer"])
        self.bloque_rojo = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_rojo"])
        self.bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
        self.bloque_naranja = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_naranja"])
        self.bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)
        self.bloque_morado = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_morado"])
        self.bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)
        self.footer.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0)

    def aplicar_estilos_otra_pantalla(self):
        # Asumiendo que Open_ventana_input devuelve un Frame y sus widgets son atributos
        if hasattr(self.otra_pantalla, "config"):
            self.otra_pantalla.config(bg="lightgray") # El bg de la otra pantalla es diferente

        # Si los widgets dentro de self.otra_pantalla también necesitan estilos,
        # deberías acceder a ellos (si los guardaste como atributos en Open_ventana_input)
        # y configurar sus estilos usando el diccionario ESTILOS.
        pass

    def ejecutar_macro(self):
        try:
            ruta_archivo = r'C:\Users\Vixof\OneDrive\Documentos\Empleados\Dataset\dataset_empleados.xlsm'
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = True
            wb = excel.Workbooks.Open(ruta_archivo)
            excel.Application.Run("dataset_empleados.xlsm!Main")
            wb.Save()
            wb.Close()
            excel.Quit()
            del excel
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al ejecutar la macro: {e}")

    def mostrar_advertencia(self):
        messagebox.showwarning("Advertencia", "Funcionalidad fuera de servicio, este software esta en fase de desarrollo.")

    def mostrar_otra_pantalla(self):
        self.pantalla_principal.pack_forget()
        self.otra_pantalla.pack(fill="both", expand=True)

    def mostrar_pantalla_principal(self):
        self.otra_pantalla.pack_forget()
        self.pantalla_principal.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MiInterfaz()
    app.mainloop()