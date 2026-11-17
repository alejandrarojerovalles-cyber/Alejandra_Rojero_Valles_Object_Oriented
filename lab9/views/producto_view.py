import tkinter as tk
from tkinter import ttk

class ProductoView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Inventario y Exportación")
        self.geometry("600x450")
        
        self.controller = None
        self._crear_interfaz()

    def set_controller(self, controller):
        self.controller = controller

    def _crear_interfaz(self):
        # Panel superior: Formulario de alta
        frame_form = ttk.LabelFrame(self, text="Nuevo Producto")
        frame_form.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_form)
        self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Precio:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_precio = ttk.Entry(frame_form)
        self.ent_precio.grid(row=0, column=3, padx=5, pady=5)

        btn_guardar = ttk.Button(frame_form, text="Guardar", command=lambda: self.controller.agregar_producto())
        btn_guardar.grid(row=0, column=4, padx=5, pady=5)

        # Tabla de Productos
        frame_tabla = ttk.Frame(self)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=300)
        self.tabla.column("Precio", width=100, anchor="e")
        self.tabla.pack(fill="both", expand=True)

        # Panel de Exportación (Requerimiento Paso 1)
        frame_export = ttk.LabelFrame(self, text="Módulo de Exportación")
        frame_export.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_export, text="Formato:").pack(side="left", padx=5, pady=5)
        
        # Combobox de solo lectura con los 4 formatos solicitados
        self.combo_formato = ttk.Combobox(
            frame_export, 
            values=["CSV", "TXT", "JSON", "PDF"], 
            state="readonly"
        )
        self.combo_formato.current(0)
        self.combo_formato.pack(side="left", padx=5, pady=5)

        # Botón Exportar Reporte vinculado al Controlador
        btn_exportar = ttk.Button(
            frame_export, 
            text="Exportar Reporte", 
            command=lambda: self.controller.exportar_reporte(self.combo_formato.get())
        )
        btn_exportar.pack(side="left", padx=5, pady=5)

    def actualizar_tabla(self, productos):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for prod in productos:
            self.tabla.insert("", "end", values=(prod[0], prod[1], f"${float(prod[2]):.2f}"))