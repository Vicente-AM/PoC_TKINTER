import tkinter as tk
# Variables globales
Button_switch = False

# Funciones
def boton_presionado():
        print("Botón presionado!")
def Cambiar_texto_btn():
        global Button_switch
        etiqueta.config(text="Ejecutado.")
        Button_switch=True

def aplicar_texto():
        texto_entrada = entrada.get()
        etiqueta.config(text=texto_entrada)

#Print debug
print("Estado del botón:", Button_switch)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("POC")

# Establecer el tamaño de la ventana (ancho x alto)
ventana.geometry("720x480")

#Ordenamiento usando un frame
frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="blue", border=4)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="red", border=4)
frame2.pack()

#Agregamos boton
boton = tk.Button(frame1, text="Acción")
boton.config(fg="white", bg="green", font=("Arial", 12))
#boton.config(command=boton_presionado) #Asignamos la funcion boton presionado en command
boton.config(command=aplicar_texto) 
boton.pack()

#Etiqueta
etiqueta = tk.Label(ventana, text="En espera...")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 14, "bold"))
etiqueta.pack()

#Entry es un input de usuario
entrada = tk.Entry(ventana)
entrada.config(fg="blue", bg="yellow", font=("Arial", 14, "bold"))
entrada.insert(0, "Dato prueba")
texto_entrada = entrada.get()
entrada.pack()



if Button_switch == True:
        boton.config(state="disabled")
        boton.config(fg="grey", bg="red")
        print("Estado del botón:", Button_switch)
        boton.pack()

# Mantener la ventana abierta
ventana.mainloop()