import tkinter as tk
from tkinter import font
from tkinter import messagebox
import win32com.client
import subprocess
import os

def ejecutar_macro():
    print("Ejecutado.")
    """"
    ruta_script = r"C:\Workspace\PoC\Ejecucion.py"
    subprocess.run(["python", ruta_script])
    """
    
def mostrar_advertencia():
    messagebox.showwarning("Advertencia", "Funcionalidad fuera de servicio, este software esta en fase de desarrollo.")

ventana = tk.Tk()
ventana.title("BC Ripley automation")
ventana.geometry("720x480")
ventana.configure(bg="white")

# Fuente grande
fuente_grande = font.Font(family="Segoe UI", size=14)

# --- Menú superior tipo barra (simulada) ---
barra_superior = tk.Frame(ventana, bg="#D3D3D3", height=40)
barra_superior.pack(side="top", fill="x")

# Menubutton estilo menú desplegable
boton_menu = tk.Menubutton(barra_superior, text="Menú", font=fuente_grande, bg="#D3D3D3", relief="flat", activebackground="#C0C0C0")
boton_menu.pack(side="left", padx=10, pady=5)

# --- Botón grande en el centro con mismo estilo ---
boton_estilizado = tk.Button(
    ventana,
    text="Ejecutar Macro Excel",
    command=ejecutar_macro,
    font=fuente_grande,
    bg="#9B3B8B",
    fg="white",
    relief="flat",
    activebackground="#8B2B7B",
    padx=20,
    pady=10
)
boton_estilizado.pack(pady=100)

# Menú desplegable asociado
menu_opciones = tk.Menu(boton_menu, tearoff=0, font=fuente_grande)
menu_opciones.add_command(label="Opción 1", command=mostrar_advertencia)
menu_opciones.add_command(label="Opción 2", command=mostrar_advertencia)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=ventana.quit)

# Asociar menú al botón
boton_menu.config(menu=menu_opciones, font=fuente_grande, bg="#D3D3D3", relief="flat", activebackground="#C0C0C0")

# --- Footer con colores personalizados (como en imagen) ---
footer = tk.Frame(ventana, height=60, bg="white")
footer.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0)

bloque_rojo = tk.Frame(footer, bg="#FF2D2D")
bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

bloque_naranja = tk.Frame(footer, bg="#FFB347")
bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)

bloque_morado = tk.Frame(footer, bg="#9B3B8B")
bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)

#Lanzamos la ventana
ventana.mainloop()
