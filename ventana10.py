# Listbox y combobox
import tkinter as tk
from tkinter import ttk # Importamos el modulo ttk para Combobox

# LISTBOX
def on_selection(event): # Insertamos el evento como argumento
    indice = listbox.curselection() # Entrega valor contenido en indice seleccionado
    elemento = listbox.get(indice)
    print(f"Selección: {elemento}")

def on_click(event):
    print("Click")

def on_doble_click(event):
    print("Doble click")

ventana = tk.Tk()
ventana.title("Listbox y Combobox")

listbox = tk.Listbox(ventana, width=30, height=10, font=("Arial", 12), fg="grey", bg="black")#FG = color letra)

for i in range(1,4):
    listbox.insert(tk.END,f"Elemento {i}")
listbox.insert(0, "Elemento 0") # Insertamos con (posición y contenido)
listbox.pack()
listbox.delete(2) # Borramos selectivamente por posicion

listbox.bind("<<ListboxSelect>>", on_selection) # Bindeamos el evento ListboxSelect al elemento Listbox para que funcione con nuestra función
listbox.bind("<Button-1>", on_click)
listbox.bind("<Double-Button-1>", on_doble_click)

# COMBOBOX
def on_selection_cb(event):
    valor = combobox.get()
    print(f"Selección {valor}")

combobox = ttk.Combobox(ventana, width=30, height=10, font=("Arial", 12), foreground="black", background="white") # Creacion de cb

# Agregamos elementos a nuestra combobox
elementos_cb = []
for i in range(1, 4):
    elementos_cb.append(f"Elemento {i}")

combobox["values"] = elementos_cb # Asignamos los valores del combobox nuestra lista creada

combobox.bind("<<ComboboxSelected>>", on_selection_cb) # Bindeamos el evento ComboboxSelected al elemento Combobox para que funcione con nuestra función

combobox.pack()

ventana.mainloop()