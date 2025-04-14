import tkinter as tk

#Ejemplo de eventos

def on_click(event):
    print(f"boton presionado {event.widget['text']} presionado") #Sacamos el texto del boton para printear cuando ese boton es presionado y poner nombre


ventana = tk.Tk()

Buttons = [tk.Button(ventana, text=f"Botón {i}") for i in range(1,4)] #Creamos 3 botones

for Button in Buttons: #Creamos un loop for para asociar los botones a cada función
    Button.pack()
    Button.bind("<Button-1>", on_click)

ventana.mainloop()