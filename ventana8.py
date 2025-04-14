#Menu, Menubutton y menu contextual
import tkinter as tk

def abrir_archivo():
    print("archivo abierto")

def abrir_menu_contextual(event):
    Menu_contextual.tk_popup(event.x_root, event.y_root)


ventana = tk.Tk()
ventana.geometry("720x480")
ventana.title("")

#Creacion menu dinamico (se puede poner en cualquier parte de nuestra ventana)
BotonMenu = tk.Menubutton(ventana, text="archivo") #Creamos el boton de tipo menubutton que diga archivo
BotonMenu.pack()

Menu = tk.Menu(BotonMenu) #creamos el menu como tal y asignamos el boton ya declarado
BotonMenu.config(menu=Menu) #Asignamos el menu creado al boton menu

# Opciones de menu desplegable dinamico
Menu.add_command(label="Abrir", command=abrir_archivo)
Menu.add_command(label="Guardar")



#Creamos una barra menu estatica en la ventana
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)#Asignamos a ventana el menu barra menu declarado

archivo_menu = tk.Menu(barra_menu)#Despegable que contendra nuestras opciones
barra_menu.add_cascade(label="Actividades", menu=archivo_menu)

archivo_menu.add_command(label="Nuevo", command=abrir_archivo)
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir")

#Creamos un menu contextual
Menu_contextual = tk.Menu(ventana, tearoff=0)
Menu_contextual.add_command(label="Copiar")
Menu_contextual.add_command(label="Cortar")
Menu_contextual.add_command(label="Pegar")

ventana.bind("<Button 3>", abrir_menu_contextual)



ventana.mainloop()