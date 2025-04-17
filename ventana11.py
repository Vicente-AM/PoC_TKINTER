# Image manipulation
import tkinter as tk
from tkinter import Image, ImageTk #Libreria de manipilacion de imagenes

ventana = tk.Tk()
ventana.title("Image manipulation")

imagen = tk.PhotoImage(file="C:\Workspace\PoC\PoC_env\Resources\Bc ripley.png")
imagen_pil = Image.open()

etiqueta = tk.Label(ventana, image=imagen)
boton = tk.Button(ventana, image=imagen)

etiqueta.pack()
boton.pack()

ventana.mainloop()