from tkinter import filedialog, messagebox
from services.exportadores import (
    ExportadorCSV, 
    ExportadorTXT, 
    ExportadorJSON, 
    ExportadorPDF
)

class ProductoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.cargar_productos()

    def cargar_productos(self):
        datos = self.model.obtener_todos()
        self.view.actualizar_tabla(datos)

    def agregar_producto(self):
        nombre = self.view.ent_nombre.get().strip()
        precio_str = self.view.ent_precio.get().strip()

        if not nombre or not precio_str:
            messagebox.showwarning("Atención", "Por favor completa todos los campos.")
            return

        try:
            precio = float(precio_str)
            self.model.insertar(nombre, precio)
            self.view.ent_nombre.delete(0, 'end')
            self.view.ent_precio.delete(0, 'end')
            self.cargar_productos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido.")

    def exportar_reporte(self, formato_seleccionado):
        # 1. Obtener los datos actuales del Modelo
        datos = self.model.obtener_todos()

        if not datos:
            messagebox.showwarning("Sin datos", "No hay registros disponibles para exportar.")
            return

        # 2. Mapear la opción del Combobox a la instancia de la clase hija correspondiente
        mapa_exportadores = {
            "CSV": (ExportadorCSV, ".csv", "Archivos CSV (*.csv)"),
            "TXT": (ExportadorTXT, ".txt", "Archivos de Texto (*.txt)"),
            "JSON": (ExportadorJSON, ".json", "Archivos JSON (*.json)"),
            "PDF": (ExportadorPDF, ".pdf", "Documentos PDF (*.pdf)")
        }

        clase_exportador, ext, filtro = mapa_exportadores[formato_seleccionado]

        # 3. Solicitar la ruta donde guardar el archivo
        ruta_archivo = filedialog.asksaveasfilename(
            defaultextension=ext,
            filetypes=[(filtro, f"*{ext}"), ("Todos los archivos", "*.*")]
        )

        if not ruta_archivo:
            return

        try:
            # Polimorfismo: Se instancia la clase correspondiente y se ejecuta .exportar()
            exportador = clase_exportador()
            exportador.exportar(datos, ruta_archivo)

            messagebox.showinfo("Éxito", f"Reporte exportado exitosamente en:\n{ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error de Exportación", f"Ocurrió un error al generar el archivo: {e}")