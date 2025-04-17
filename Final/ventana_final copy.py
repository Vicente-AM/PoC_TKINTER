import tkinter as tk
from tkinter import font
from tkinter import messagebox
import win32com.client
import subprocess
import os
from ventana_final2 import Ventana_input

class MiInterfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BC Ripley automation")
        self.geometry("720x480")
        self.configure(bg="white")
        self.fuente_grande = font.Font(family="Segoe UI", size=14)

        # --- Menú superior tipo barra (simulada) ---
        barra_superior = tk.Frame(self, bg="#D3D3D3", height=40)
        barra_superior.pack(side="top", fill="x")

        boton_menu = tk.Menubutton(barra_superior, text="Menú", font=self.fuente_grande, bg="#D3D3D3", relief="flat", activebackground="#C0C0C0")
        boton_menu.pack(side="left", padx=10, pady=5)

        # --- Botón grande en el centro con mismo estilo ---
        boton_estilizado = tk.Button(
            self,
            text="Ejecutar Macro Excel",
            command=self.realizar_accion_integrado,
            font=self.fuente_grande,
            bg="#9B3B8B",
            fg="white",
            relief="flat",
            activebackground="#8B2B7B",
            padx=20,
            pady=10
        )
        boton_estilizado.pack(pady=100)
        # Menú desplegable asociado
        menu_opciones = tk.Menu(boton_menu, tearoff=0, font=self.fuente_grande)
        menu_opciones.add_command(label="Opción 1", command=self.abrir_otra_pantalla) # Ahora es 'self.abrir_otra_pantalla'
        menu_opciones.add_command(label="Opción 2", command=self.mostrar_advertencia)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.quit)

        # Asociar menú al botón
        boton_menu.config(menu=menu_opciones, font=self.fuente_grande, bg="#D3D3D3", relief="flat", activebackground="#C0C0C0")

        # --- Footer con colores personalizados (como en imagen) ---
        footer = tk.Frame(self, height=60, bg="white")
        footer.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0)

        bloque_rojo = tk.Frame(footer, bg="#FF2D2D")
        bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

        bloque_naranja = tk.Frame(footer, bg="#FFB347")
        bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)

        bloque_morado = tk.Frame(footer, bg="#9B3B8B")
        bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)

    def abrir_otra_pantalla(self): # Toplevel - Ahora es un método de la clase
        self.ventana_final = Ventana_input(self) # Crear una instancia de la Toplevel

    def realizar_accion_integrado(self):
        try:
            # Ruta al archivo Excel
            #!!!tkinter.filedialog!!! EVALUAR
            ruta_archivo = r'C:\Users\Vixof\OneDrive\Documentos\Empleados\Dataset\dataset_empleados.xlsm'
            # Abre Excel en segundo plano
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = True
            # Abre el archivo
            wb = excel.Workbooks.Open(ruta_archivo)
            # Ejecuta la macro
            excel.Application.Run("dataset_empleados.xlsm!Main")
            # Guarda y cierra
            wb.Save()
            wb.Close()
            # Cierra Excel
            excel.Quit()
            # Limpieza
            del excel
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al ejecutar la macro: {e}")

    def ejecutar_macro(self):
        print("Ejecutando...")
        ruta_script = r"C:\Workspace\PoC\Ejecucion.py"
        subprocess.run(["python", ruta_script])

    def mostrar_advertencia(self):
        messagebox.showwarning("Advertencia", "Funcionalidad fuera de servicio, este software esta en fase de desarrollo.")

if __name__ == "__main__":
    app = MiInterfaz()
    app.mainloop()