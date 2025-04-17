import tkinter as tk
from tkinter import font

# --- DICCIONARIO DE ESTILOS ---
ESTILOS_VENTANA2 = {
    "color_fondo_menu": "#D9D9D9",
    "color_fondo_principal": "#C5ABD2",
    "color_input": "#BFBFBF",
    "color_btn": "#96378C",
    "color_texto_btn": "black",
    "relief_btn": "flat",
    "fuente_btn": ("Arial", 10, "bold"),
    "color_borde_btn": "white",
    "color_footer_izq": "#FF2B34",
    "color_footer_centro": "#FFB347",
    "color_footer_der": "#96378C",
    "fuente_titulo": ("Arial", 14, "bold"),
    "fuente_texto": ("Arial", 12),
    "fuente_texto_normal": ("Arial", 10)
}

class VentanaInput(tk.Frame): # Ahora es una clase que hereda de tk.Frame
    def __init__(self, parent, estilos=ESTILOS_VENTANA2):
        super().__init__(parent, bg=estilos["color_fondo_principal"])

        # ----- MENÚ SUPERIOR (Dentro de este Frame) -----
        menu_superior = tk.Frame(self, bg=estilos["color_fondo_menu"], height=40)
        menu_superior.pack(side="top", fill="x")
        tk.Label(menu_superior, text="Menú", bg=estilos["color_fondo_menu"], anchor="w", padx=10).pack(side="left", fill="y")

        tk.Label(self, text="INPUT", bg=estilos["color_fondo_principal"], font=estilos["fuente_titulo"]).pack(pady=(20, 10))

        entrada1 = tk.Entry(self, bg=estilos["color_input"], font=estilos["fuente_texto"])
        entrada1.pack(padx=40, pady=10, fill="x")

        entrada2 = tk.Entry(self, bg=estilos["color_input"], font=estilos["fuente_texto"])
        entrada2.pack(padx=40, pady=10, fill="x")

        btn_asignar = tk.Button(
            self,
            text="Asignar",
            bg=estilos["color_btn"],
            fg=estilos["color_texto_btn"],
            relief=estilos["relief_btn"],
            font=estilos["fuente_btn"]
        )
        btn_asignar.pack(anchor="e", padx=40, pady=20)

        # ----- ETIQUETAS LATERALES (Dentro de este Frame) -----
        tk.Label(self, text="Ruta archivo", bg=estilos["color_fondo_principal"], font=estilos["fuente_texto_normal"]).place(x=10, y=130)
        tk.Label(self, text="Macro", bg=estilos["color_fondo_principal"], font=estilos["fuente_texto_normal"]).place(x=10, y=190)

        # ----- FOOTER (Dentro de este Frame - Opcional, si quieres un footer diferente) -----
        # Si quieres usar el footer común de la ventana principal, no necesitas este footer aquí.
        # Si quieres un footer específico para esta "página", descomenta lo siguiente y ajústalo.
        """
        footer = tk.Frame(self, height=50)
        footer.pack(side="bottom", fill="x")
        footer_izq = tk.Frame(footer, bg=estilos["color_footer_izq"], width=550).pack(side="left", fill="y")
        footer_centro = tk.Frame(footer, bg=estilos["color_footer_centro"], width=100).pack(side="left", fill="y")
        footer_der = tk.Frame(footer, bg=estilos["color_footer_der"]).pack(side="left", fill="both", expand=True)
        """

if __name__ == "__main__":
    app = MiInterfaz()
    app.mainloop()