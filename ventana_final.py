import tkinter as tk
from tkinter import font

ventana = tk.Tk()
ventana.title("Menú con Menubutton")
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

# Menú desplegable asociado
menu_opciones = tk.Menu(boton_menu, tearoff=0, font=fuente_grande)
menu_opciones.add_command(label="Opción 1", command=lambda: print("Opción 1"))
menu_opciones.add_command(label="Opción 2", command=lambda: print("Opción 2"))
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=ventana.quit)

# Asociar menú al botón
boton_menu.config(menu=menu_opciones)

# --- Footer con colores personalizados (como en imagen) ---
footer = tk.Frame(ventana, height=60, bg="white")
footer.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0)

bloque_rojo = tk.Frame(footer, bg="#FF2D2D")
bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

bloque_naranja = tk.Frame(footer, bg="#FFB347")
bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)

bloque_morado = tk.Frame(footer, bg="#9B3B8B")
bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)

ventana.mainloop()
