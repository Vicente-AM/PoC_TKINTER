import win32com.client

# Ruta al archivo Excel
ruta_archivo = r'C:\Users\Vixof\OneDrive\Documentos\Empleados\Dataset\dataset_empleados.xlsm'

# Abre Excel en segundo plano
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

# Abre el archivo
wb = excel.Workbooks.Open(ruta_archivo)

# Ejecuta la macro
excel.Application.Run("dataset_empleados.xlsm!Main")

# Guarda y cierra
wb.Save()
wb.Close()

# Cierra Excel
excel.Quit()

# Limpieza
del excel