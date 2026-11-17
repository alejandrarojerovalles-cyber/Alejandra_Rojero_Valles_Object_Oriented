import csv
import json
from fpdf import FPDF

class Exportador:
    def exportar(self, datos, ruta_archivo):
        """Método base abstracto a ser sobrescrito por las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                file.write(f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: ${producto[2]:.2f}\n")
        print(f"Archivo TXT generado en: {ruta_archivo}")

class ExportadorCSV(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio"])
            for producto in datos:
                writer.writerow([producto[0], producto[1], producto[2]])
        print(f"Archivo CSV generado en: {ruta_archivo}")

class ExportadorJSON(Exportador):
    def exportar(self, datos, ruta_archivo):
        lista_productos = [
            {"id": prod[0], "nombre": prod[1], "precio": float(prod[2])}
            for prod in datos
        ]
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(lista_productos, file, indent=4, ensure_ascii=False)
        print(f"Archivo JSON generado en: {ruta_archivo}")

class ExportadorPDF(Exportador):
    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()
        
        # Configuración del título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        pdf.ln(10)
        
        # Encabezados de tabla
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(30, 10, "ID", border=1, align='C')
        pdf.cell(110, 10, "Nombre", border=1, align='L')
        pdf.cell(50, 10, "Precio", border=1, align='R')
        pdf.ln()
        
        # Cuerpo del reporte
        pdf.set_font("Arial", size=12)
        for producto in datos:
            pdf.cell(30, 10, str(producto[0]), border=1, align='C')
            pdf.cell(110, 10, str(producto[1]), border=1, align='L')
            pdf.cell(50, 10, f"${producto[2]:.2f}", border=1, align='R')
            pdf.ln()
            
        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")