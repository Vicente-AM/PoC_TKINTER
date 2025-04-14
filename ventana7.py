import tkinter as tk

ventana = tk.Tk()
ventana.geometry("720x480")
ventana.title("Principal")

def abrir_ventana_top_level():
    ventana_toplevel = tk.Toplevel(ventana)
    ventana_toplevel.title("a")
    ventana_toplevel.geometry("300x200+50+50")

    

boton = tk.Button(text="abrir ventana pequeña", command=abrir_ventana_top_level)
boton.pack()

ventana.mainloop()