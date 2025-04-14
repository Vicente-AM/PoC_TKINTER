import tkinter as tk

#Ejemplo de eventos

def on_click(event):
    print("boton presionado")

def on_key_press(event):
    if event.char == "a":
        print("tecla a presionada")

def on_resize(event):
    print("Resized")

def on_mouse_move(event):
    print(f"raton en pos {event.x}, {event.y}")

ventana = tk.Tk()

buton = tk.Button(ventana, text="haz click")
buton.pack()

buton.bind("<Button-1>", on_click)

ventana.bind("<KeyPress>", on_key_press) #Asignamos funcion y metodo para que ventana pueda determinar las acciones

#ventana.bind("<Configure>", on_resize)

ventana.bind("<Motion>", on_mouse_move)

ventana.mainloop()