# Text widgets: Text & Scrolled text
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
ventana.title("Scrolled text")

# Texto estatico sin scrollbar
texto = tk.Text(ventana, width=40, height=10, wrap="word", bg="lightgrey", fg="black", padx=1, pady=10, font=("Arial", 12))#FG = color letra
texto.pack()

# Texto con srollbar
texto_desplazable = ScrolledText(ventana, width=40, height=10, wrap="word", bg="lightgrey", fg="black", padx=1, pady=10, font=("Arial", 12))
texto_desplazable.pack()

ventana.mainloop()