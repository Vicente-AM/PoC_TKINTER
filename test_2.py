import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import win32com.client
import os
import json  # Importamos la biblioteca para parametros de reinicio

ESTILOS = {
    # Estilos generales de la aplicación
    "bg_principal": "white",
    "color_texto_general": "black",
    "fuente_general": ("Segoe UI", 14),
    "tamaño_fuente_S": 10,
    "tamaño_fuente_M": 14,
    "tamaño_fuente_L": 16,
    "tamaño_fuente_XL": 18,

    # Estilos de la barra superior
    "bg_barra_superior": "#D3D3D3",
    "color_texto_menu": "black",
    "fuente_menu": "Segoe UI",
    "relief_menu": "flat",
    "activebg_menu": "#C0C0C0",

    # Estilos botón ventana principal (pantalla principal)
    "bg_boton_principal": "#9B3B8B",
    "fg_boton_principal": "white",
    "relief_boton_principal": "flat",
    "activebg_boton_principal": "#8B2B7B",
    "fuente_titulo": ("Segoe UI", 24, "bold"),

    # Estilos del footer
    "bg_footer": "white",
    "bg_bloque_rojo": "#FF2D2D",
    "bg_bloque_naranja": "#FFB347",
    "bg_bloque_morado": "#9B3B8B",

    # Estilos específicos de la pantalla de entrada (input)
    "bg_pantalla_input": "#C5ABD2",
    "color_fondo_menu_input": "#D9D9D9",
    "color_input_bg": "#BFBFBF",
    "color_btn_input": "#96378C",
    "color_texto_btn_input": "white",
    "relief_btn_input": "flat",
    "fuente_btn_input": ("Segoe UI", 12, "bold"),
    "color_borde_btn_input": "white",
    "fuente_titulo_input": ("Segoe UI", 14, "bold"),

    # Estilos pantalla parametría
}

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BC Ripley automation")
        self.geometry("720x480")
        self.configure(bg=ESTILOS["bg_principal"])
        self.fuente_grande = font.Font(family=ESTILOS["fuente_general"][0], size=ESTILOS["tamaño_fuente_M"])
        # Parámetros de reinicio app
        self.parametros_guardados = {}
        self.config_file_json = "parametros_app.json"
        self.load_parametros_json()
        # ---
        # Debug de archivo, se debe cambiar en caso de cambiar de ambiente de pruebas, de archivo y/o de macro
        self.ruta_archivo_input = "C:\Workspace\PoC\Test.xlsm"
        self.macro_input = "Main"
        # ---
        # Variables para input de macro, en desuso actualmente
        self.ruta_label_texto = tk.StringVar()  # Variables para el texto de los labels
        self.macro_label_texto = tk.StringVar()
        self.ruta_label_texto.set("Ruta no asignada") # Texto inicial
        self.macro_label_texto.set("Macro no asignada") # Texto inicial
        # ---
        self.menu_contextual_entrada = tk.Menu(self, tearoff=0) # Menú contextual para copiar, cortar y pegar
        # Parametros de input, agregar más de ser necesario
        self.parametro1_input = ""
        self.parametro2_input = ""
        self.parametro3_input = ""

        self.barra_superior = tk.Frame(self, bg=ESTILOS["bg_barra_superior"], height=40)
        self.barra_superior.pack(side="top", fill="x")

        boton_menu = tk.Menubutton(
            self.barra_superior,
            text="Menú",
            font=font.Font(family=ESTILOS["fuente_menu"][0], size=ESTILOS["tamaño_fuente_M"], weight="normal"), # Añadimos weight="normal"
            bg=ESTILOS["bg_barra_superior"],
            fg=ESTILOS["color_texto_menu"],
            relief=ESTILOS["relief_menu"],
            activebackground=ESTILOS["activebg_menu"]
        )
        boton_menu.pack(side="left", padx=10, pady=5)

        # Definición de menú estatico, cada uno hace referencia a una opción del menú
        menu_opciones = tk.Menu(boton_menu, tearoff=0, font=self.fuente_grande)
        menu_opciones.add_command(label="Pantalla Principal", command=self.mostrar_pantalla_principal)
        menu_opciones.add_command(label="Pantalla Input*", command=self.mostrar_pantalla_input)
        menu_opciones.add_command(label="Pantalla Parametría", command=self.mostrar_pantalla_parametria) # Nueva opción
        #menu_opciones.add_command(label="Opción 3 (sin acción)", command=self.mostrar_advertencia)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.quit)
        boton_menu.config(menu=menu_opciones)

        self.contenedor_principal = tk.Frame(self) # Contenedor para las diferentes "páginas"
        self.contenedor_principal.pack(fill="both", expand=True)

        # Creamos instacia de ventanas
        self.pantalla_principal = self.crear_pantalla_principal()
        self.pantalla_input = self.crear_pantalla_input()
        self.pantalla_parametria = self.crear_pantalla_parametria()

        # Insertamos ventanas en contenedor principal
        self.pantalla_principal.place(in_=self.contenedor_principal, x=0, y=0, relwidth=1, relheight=1)
        self.pantalla_input.place(in_=self.contenedor_principal, x=0, y=0, relwidth=1, relheight=1)
        self.pantalla_parametria.place(in_=self.contenedor_principal, x=0, y=0, relwidth=1, relheight=1)

        self.mostrar_pantalla_principal() # Mostrar la primera pantalla

        self.footer = tk.Frame(self, height=60, bg=ESTILOS["bg_footer"])
        self.bloque_rojo = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_rojo"])
        self.bloque_rojo.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
        self.bloque_naranja = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_naranja"])
        self.bloque_naranja.place(relx=0.5, rely=0.0, relwidth=0.2, relheight=1.0)
        self.bloque_morado = tk.Frame(self.footer, bg=ESTILOS["bg_bloque_morado"])
        self.bloque_morado.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)
        self.footer.pack(side="bottom", fill="x")

        # Establecer el tamaño mínimo de la ventana
        self.minsize(600, 470) # Ejemplo: ancho mínimo de 600 píxeles y alto mínimo de 400 píxeles


    def crear_pantalla_principal(self):
        pantalla = tk.Frame(self.contenedor_principal, bg=ESTILOS["bg_principal"])
        """ Comentamos estos label ya que no estarán en uso, puede que se usen en version futura
        # Labels para mostrar la información
        ruta_label = tk.Label(pantalla, textvariable=self.ruta_label_texto, bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"])
        ruta_label.pack(pady=10)

        macro_label = tk.Label(pantalla, textvariable=self.macro_label_texto, bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"])
        macro_label.pack(pady=10)
        """
        # En caso de esta interfaz en particular le agregamos el nombre de la iniciativa directamente
        ruta_label = tk.Label(pantalla, text="Circular B-2234", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_titulo"])
        ruta_label.pack(pady=10)

        boton_estilizado = tk.Button(
            pantalla,
            text="Ejecutar",
            command=self.ejecutar_macro,
            font=self.fuente_grande,
            bg=ESTILOS["bg_boton_principal"],
            fg=ESTILOS["fg_boton_principal"],
            relief=ESTILOS["relief_boton_principal"],
            activebackground=ESTILOS["activebg_boton_principal"],
            padx=20,
            pady=10,
            cursor="hand2"  # Cambia el cursor a una mano
        )

        # Se añaden funciones para responsividad del boton ejecutar
        def on_enter(event):
            boton_estilizado.config(bg=ESTILOS["activebg_boton_principal"])

        def on_leave(event):
            boton_estilizado.config(bg=ESTILOS["bg_boton_principal"])

        boton_estilizado.bind("<Enter>", on_enter)
        boton_estilizado.bind("<Leave>", on_leave)

        boton_estilizado.pack(pady=100)
        return pantalla

    def crear_pantalla_input(self):
        pantalla_input = tk.Frame(self.contenedor_principal, bg=ESTILOS["bg_principal"]) # Considera usar ESTILOS["bg_pantalla_input"]

        tk.Label(pantalla_input, text="INPUT", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_titulo_input"]).grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Label para "Ruta archivo"
        tk.Label(pantalla_input, text="Ruta archivo", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"]).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada1 = tk.Entry(pantalla_input, bg=ESTILOS["color_input_bg"], font=ESTILOS["fuente_general"])
        self.entrada1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Reemplazado fill="x" con sticky="ew"
        self.entrada1.bind("<Button-3>", self.mostrar_menu_contextual_entrada) # Binding


        # Label para "Macro"
        tk.Label(pantalla_input, text="Macro", bg=ESTILOS["bg_principal"], font=ESTILOS["fuente_general"]).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada2 = tk.Entry(pantalla_input, bg=ESTILOS["color_input_bg"], font=ESTILOS["fuente_general"])
        self.entrada2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")  # Reemplazado fill="x" con sticky="ew"
        self.entrada2.bind("<Button-3>", self.mostrar_menu_contextual_entrada) # Binding

        # Configurar el menú contextual añadiendo opciones
        self.menu_contextual_entrada.add_command(label="Copiar", command=self.copiar_seleccion)
        self.menu_contextual_entrada.add_command(label="Cortar", command=self.cortar_seleccion)
        self.menu_contextual_entrada.add_command(label="Pegar", command=self.pegar_en_seleccion)


        btn_asignar = tk.Button(
            pantalla_input,
            text="Asignar",
            command=self.validar_datos_input,  # Asignar la función de validación al botón
            bg=ESTILOS["color_btn_input"],
            fg=ESTILOS["color_texto_btn_input"],
            relief=ESTILOS["relief_btn_input"],
            font=ESTILOS["fuente_btn_input"],
            width=10,  # Ajusta el ancho
            height=2,   # Ajusta la altura, aunque grid controla el tamaño también
            cursor="hand2"  # Cambia el cursor a una mano
        )
        btn_asignar.grid(row=3, column=1, padx=(40), pady=20, sticky="e")

        # Se añaden funciones para responsividad del boton asignar
        def on_enter(event):
            btn_asignar.config(bg=ESTILOS["activebg_boton_principal"])

        def on_leave(event):
            btn_asignar.config(bg=ESTILOS["bg_boton_principal"])

        btn_asignar.bind("<Enter>", on_enter)
        btn_asignar.bind("<Leave>", on_leave)

        # Configurar el peso de las columnas para que la entrada se expanda
        pantalla_input.columnconfigure(1, weight=1)

        return pantalla_input
    
    # Reinicio de app, recarga de ultima ejecución de parámetros
    def load_parametros_json(self):
        try:
            with open(self.config_file_json, 'r') as f:
                self.parametros_guardados = json.load(f)
        except FileNotFoundError:
            self.parametros_guardados = {}
        except json.JSONDecodeError:
            self.parametros_guardados = {}
    # ---
    def crear_pantalla_parametria(self):
        pantalla_parametria = ttk.Frame(self.contenedor_principal, style="TFrame")
        pantalla_parametria.pack(fill="both", expand=True)

        # Canvas para contener los widgets con scroll
        self.canvas = tk.Canvas(pantalla_parametria, highlightthickness=0) # Guardamos la referencia en self.canvas
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(pantalla_parametria, orient="vertical", command=self.canvas.yview) # Usamos self.canvas aquí
        scrollbar.pack(side="right", fill="y")

        # Configurar el canvas para usar el scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set) # Usamos self.canvas aquí
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))) # Usamos self.canvas aquí

        # Frame interno para contener todos los widgets de los parámetros
        self.parametros_frame = ttk.Frame(self.canvas, style="TFrame") # El frame interno va dentro del canvas
        self.parametros_frame.pack(fill="both", expand=True)

        # Título
        tk.Label(self.parametros_frame, text="Parametría", font=ESTILOS["fuente_titulo_input"]).grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="ew")

        # Si queremos añadir más parametros a la vista de la pantalla parametria, basta con añadirlos a esta lista
        Parametros_list = ["Parametro 1", "Parametro 2", "Parametro 3"]
        self.entradas_parametros = {}

        for i, nombre_parametro in enumerate(Parametros_list):
            fila = i + 1
            # Label para el nombre del parámetro
            tk.Label(self.parametros_frame, text=f"{nombre_parametro}:", font=ESTILOS["fuente_general"]).grid(row=fila, column=0, padx=10, pady=5, sticky="w")
            # Entry para el valor del parámetro
            entry = tk.Entry(self.parametros_frame, bg=ESTILOS["color_input_bg"], font=ESTILOS["fuente_general"])
            entry.grid(row=fila, column=1, padx=10, pady=5, sticky="ew")
            entry.bind("<Button-3>", self.mostrar_menu_contextual_entrada)
            if nombre_parametro in self.parametros_guardados:
                entry.insert(0, self.parametros_guardados[nombre_parametro])
            self.entradas_parametros[nombre_parametro] = entry

        btn_guardar_parametros = tk.Button(
            self.parametros_frame,
            text="Guardar",
            command=self.guardar_parametros,
            bg=ESTILOS["bg_boton_principal"],
            fg=ESTILOS["fg_boton_principal"],
            relief=ESTILOS["relief_boton_principal"],
            activebackground=ESTILOS["activebg_boton_principal"],
            width=10,
            height=2,
            cursor="hand2"
        )
        # Locacion en pantalla del botón
        btn_guardar_parametros.grid(row=len(Parametros_list) + 1, column=1, padx=(40), pady=20, sticky="e")
        # Se añaden funciones para responsividad del boton ejecutar
        def on_enter(event):
            btn_guardar_parametros.config(bg=ESTILOS["activebg_boton_principal"])

        def on_leave(event):
            btn_guardar_parametros.config(bg=ESTILOS["bg_boton_principal"])

        btn_guardar_parametros.bind("<Enter>", on_enter)
        btn_guardar_parametros.bind("<Leave>", on_leave)

        # Configurar el peso de las columnas para la responsividad dentro del frame de parámetros
        self.parametros_frame.columnconfigure(0, weight=1)
        self.parametros_frame.columnconfigure(1, weight=2)

        # Modificación importante aquí: Configurar el canvas para que el frame interno se expanda con él
        self.canvas_window = self.canvas.create_window((0, 0), window=self.parametros_frame, anchor="nw")
        self.canvas.bind('<Configure>', self._on_canvas_configure)

        return pantalla_parametria

    def _on_canvas_configure(self, event):
        """Función para actualizar el ancho y la región de scroll del canvas cuando se redimensiona el canvas."""
        self.canvas.itemconfig(self.canvas_window, width=event.width)
        self.canvas.configure(scrollregion=self.parametros_frame.bbox("all")) # Usamos el bbox del frame interno
    
    # Obtenemos y guardamos los parametros ingresados en interfaz
    def guardar_parametros(self):
        # Definimos explícitamente las variables de destino para cada parámetro (Lista de parametros definida "Parametros_list")
        # Aqui se deben usar los parametros y definir los nombre entre comillas "" tal cual en la lista "Parametros_list"
        self.parametro_1 = self.entradas_parametros.get("Parametro 1", tk.StringVar()).get()
        self.parametro_2 = self.entradas_parametros.get("Parametro 2", tk.StringVar()).get()
        self.parametro_3 = self.entradas_parametros.get("Parametro 3", tk.StringVar()).get()
        # Imprimimos los valores guardados para verificar
        print("Valores de los parámetros guardados explícitamente:")
        print(f"Parametro 1: {self.parametro_1}")
        print(f"Parametro 2: {self.parametro_2}")
        print(f"Parametro 3: {self.parametro_3}")
        # Si necesitas guardar todos los parámetros en un diccionario también puedes hacerlo
        self.parametros_guardados = {
            "Parametro 1": self.parametro_1,
            "Parametro 2": self.parametro_2,
            "Parametro 3": self.parametro_3
        }
        print("Diccionario de parámetros guardados:", self.parametros_guardados)

        #messagebox.showinfo("Parámetros", "Parámetros guardados.")
        
        # Guardamos los parametros insertados en pantalla en json de reinicio
        parametros_a_guardar = {}
        for nombre_parametro, entrada in self.entradas_parametros.items():
            parametros_a_guardar[nombre_parametro] = entrada.get()

        try:
            with open(self.config_file_json, 'w') as f:
                json.dump(parametros_a_guardar, f)
            messagebox.showinfo("Parámetros", "Parámetros guardados.")
        except IOError as e:
            messagebox.showerror("Error", f"Error al guardar la configuración: {e}")
        # --- Fin guardado ---
        try:
            # Asegúrate de que self.ruta_archivo_input contiene la ruta correcta del archivo Excel
            if not self.ruta_archivo_input:
                messagebox.showerror("Error", "No se ha asignado la ruta del archivo Excel.")
                return

            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False  # No mostrar Excel durante la operación
            wb = excel.Workbooks.Open(self.ruta_archivo_input)
            sh = wb.Sheets("Parametros")  # Accede a la hoja llamada "Parámetros"

            # Escribe los valores en celdas específicas. Ajusta las celdas según tu necesidad.
            # Por ejemplo, escribe el valor de Parametro 1 en la celda A1, Parametro 2 en B1, etc.
            sh.Cells(2, 2).Value = self.parametro_1  # Celda B2 - 2, 2 Fila y columna respectivamente
            sh.Cells(3, 2).Value = self.parametro_2  # Celda B3 - 3 => fila 3, 2 => columna B
            #sh.Cells(1, 3).Value = self.parametro_3  # Celda C1

            wb.Save()
            wb.Close()
            excel.Quit()
            del excel

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al escribir en Excel: {e}")

        #messagebox.showinfo("Parámetros", "Parámetros guardados.")
        

    # Funciones copiar, cortar y pegar
    def mostrar_menu_contextual_entrada(self, event):
        try:
            self.menu_contextual_entrada.post(event.x_root, event.y_root)
            self._menu_entry_widget = event.widget # Guardar el widget que activó el menú
        finally:
            self.menu_contextual_entrada.grab_release()

    def copiar_seleccion(self):
        try:
            texto = self._menu_entry_widget.selection_get()
            self.clipboard_clear()
            self.clipboard_append(texto)
        except tk.TclError:
            pass

    def cortar_seleccion(self):
        try:
            texto = self._menu_entry_widget.selection_get()
            self.clipboard_clear()
            self.clipboard_append(texto)
            self._menu_entry_widget.delete("sel.first", "sel.last")
        except tk.TclError:
            pass

    def pegar_en_seleccion(self):
        try:
            texto = self.clipboard_get()
            self._menu_entry_widget.insert(tk.INSERT, texto)
        except tk.TclError:
            pass


    
    # Validamos los datos de entrada de input en la pestaña de input para ejecucion de macro
    def validar_datos_input(self):
        ruta_archivo = self.entrada1.get()
        macro = self.entrada2.get()

        if not ruta_archivo or not macro:
            messagebox.showerror("Error", "Por favor, ingrese datos en ambos campos.")
        else:
            self.ruta_archivo_input = ruta_archivo
            self.macro_input = macro
            # Actualizar el texto de los labels en la pantalla principal
            self.ruta_label_texto.set(f"Ruta asignada: {self.ruta_archivo_input}")
            self.macro_label_texto.set(f"Macro asignada: {self.macro_input}")
            print(f"Ruta del archivo introducida: {self.ruta_archivo_input}")
            print(f"Nombre de la macro introducida: {self.macro_input}")
            self.mostrar_pantalla_principal() # Volver a la pantalla principal después de asignar

    # Implementamos la muestra de pantallas con el metodo tkraise
    def mostrar_pantalla_input(self):
        self.pantalla_input.tkraise()

    def mostrar_pantalla_principal(self):
        self.pantalla_principal.tkraise()
    
    def mostrar_pantalla_parametria(self):
        self.pantalla_parametria.tkraise()

    # Ejecución de macro
    def ejecutar_macro(self):
        if not self.ruta_archivo_input or not self.macro_input:
            messagebox.showerror("Error", "No se han asignado la ruta del archivo y/o la macro.")
            return

        try:
            ruta_archivo = self.ruta_archivo_input
            nombre_archivo = os.path.basename(ruta_archivo)
            macro_a_ejecutar = f"{nombre_archivo}!{self.macro_input}"
            print(f"Ejecutando macro: {macro_a_ejecutar}")

            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = True
            wb = excel.Workbooks.Open(ruta_archivo)
            excel.Application.Run(macro_a_ejecutar)
            wb.Save()
            wb.Close()
            excel.Quit()
            del excel
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al ejecutar la macro: {e}")

    def mostrar_advertencia(self):
        messagebox.showwarning("Advertencia", "Funcionalidad fuera de servicio, este software esta en fase de desarrollo.")

if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()