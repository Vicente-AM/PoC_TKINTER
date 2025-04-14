#Variables de control StringVar, IntVar, DoubleVar y BooleanVar
import tkinter as tk

def actualizar_etiqueta(*args): #obtenemos de manera dinamica los cambios que se efectuen en la interfaz
    etiqueta.config(text=texto.get())

def actualizar_entero(*args):
    print("esta es mi variable entero nueva " + str(entero.get()))

ventana = tk.Tk()
ventana.title("Variables control")

#String
texto = tk.StringVar(value="Hola") #Este tipo de variable no se puede printear simplemente, se debe tratar de siguiente manera
print(texto.get()) #Asi debemos printearla o llamarla
texto.set("Nuevo valor") #Podemos asignarle un valor nuevo de esta forma

#Int
entero = tk.IntVar(value=22)
print("esta es mi variable entero " + str(entero.get()))

for i in range(1, 4):
    i = tk.Radiobutton(ventana, text=f"Opcion {i}", font=("Arial", 12), fg="blue", bg="gray", variable=entero, value=f"{i}")
    i.pack()


#Double
double = tk.DoubleVar(value=2.2)

entrada = tk.Entry(ventana, textvariable=texto)
entrada.pack()

etiqueta = tk.Label(text="label test")
etiqueta.pack()

entero.trace_add("write", actualizar_entero)
texto.trace_add("write", actualizar_etiqueta)

ventana.mainloop()