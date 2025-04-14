#Grid, pack y place de interfaz

import tkinter as tk

ventana = tk.Tk()
ventana.title("Grid, pack and place")


label1 = tk.Label(text="Columna 1")
label1.grid(row=0, column=0, padx= 100, pady= 10)

label2 = tk.Label(text="Columna 2")
label2.grid(row=0, column=1, padx= 100, pady= 10)

for i in range(1,3):
    label = tk.Label(text=f"Label {i}")
    label.grid(row=i)

""""
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady= 10)

for i in range(1,5):
    boton = tk.Button(text=f"boton nro {i}")
    boton.pack(side="left", padx=6)
"""
for i in range(1,5):
    label = tk.Label(text=f"label nro {i}")
    label.place(relx=0.7, rely=0.7)

ventana.mainloop()