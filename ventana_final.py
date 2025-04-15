import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz")
ventana.geometry("720x480")
ventana.configure(bg="white")

# Crear barra de menú
barra_menu = tk.Menu(ventana)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Opción 1")
menu_archivo.add_command(label="Opción 2")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

barra_menu.add_cascade(label="Menú", menu=menu_archivo)
ventana.config(menu=barra_menu)

# --- Footer con bloques de colores ---
# Usamos place para ubicar por porcentaje exacto

# Frame contenedor inferior
footer = tk.Frame(ventana, height=60, bg="white")
footer.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0)

# Rojo (~50% del ancho)
bloque_rojo = tk.Frame(footer, bg="#FF2D2D")
bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

# Naranja (~15% del ancho)
bloque_naranja = tk.Frame(footer, bg="#FFB347")
bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)

# Morado (~35% del ancho)
bloque_morado = tk.Frame(footer, bg="#9B3B8B")
bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)

# Iniciar loop principal
ventana.mainloop()
