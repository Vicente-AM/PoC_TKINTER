#Radiobuttons y checkbuttons
import tkinter as tk

def radio_sel():
    Seleccion = variable_control.get()
    if Seleccion == 0:
        print("Debe seleccionar un valor")
    else:
        print(f"Valor seleccionado  {Seleccion}")

def check_sel():
    if variable_check.get(): #variable booleana
        boton_check.config(state="normal")
    else:
        boton_check.config(state="disabled")

ventana = tk.Tk()
ventana.geometry("720x480")
ventana.title("Example radio button y check")

variable_control = tk.IntVar() #Varible control para radio button

for i in range(1, 4):
    opcion = tk.Radiobutton(ventana, text=f"Opcion {i}", font=("Arial", 12), fg="blue", bg="gray", variable=variable_control, value=f"{i}")
    opcion.pack()

boton = tk.Button(ventana, text="Print valor seleccionado", command=radio_sel)
boton.pack()

variable_check= tk.BooleanVar()

for i in range(1,2):
    Check= tk.Checkbutton(ventana, text=f"Opcion {i}", font=("Arial", 12), fg="blue", bg="green", variable=variable_check, command=check_sel)
    Check.pack()

boton_check = tk.Button(ventana, text="check", state="disabled")
boton_check.pack()


ventana.mainloop()