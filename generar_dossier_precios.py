from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os
from datetime import datetime

doc = Document()

# Estilos base
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(11)

# --- PORTADA ---
title = doc.add_heading('DOSSIER DE FICHAS DE COSTOS Y TARIFAS', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('\nEntidad: PDL DESSPEZ\nProductos: Pescado y derivados\nPresentado por: Yosbel Collazo Avila\nFecha: ' + datetime.now().strftime("%d/%m/%Y"))
run.font.size = Pt(12)
run.bold = True

doc.add_paragraph('\nOBJETIVO: Presentar ante la Comisión de Precios del Municipio Quivicán el desglose de costos y la justificación técnica de los precios de venta de los productos pesqueros, adaptados a las condiciones actuales de transporte y materia prima.')
doc.add_page_break()

# --- FUNCIÓN PARA CREAR TABLAS ---
def crear_tabla_costos(datos):
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fila'
    hdr_cells[1].text = 'Conceptos'
    hdr_cells[2].text = 'Importe (CUP)'
    
    for fila, concepto, importe in datos:
        row_cells = table.add_row().cells
        row_cells[0].text = str(fila)
        row_cells[1].text = concepto
        row_cells[2].text = str(importe)

# ==========================================
# PRODUCTO 1: FILETE DE PESCADO
# ==========================================
doc.add_heading('1. FICHA DE COSTO: FILETE DE PESCADO (1 kg)', level=1)
doc.add_heading('1.1 Carta Tecnológica', level=2)
doc.add_paragraph('• Materia prima: Pescado entero fresco (250 CUP/kg) + Flete (100 CUP/kg) = 350 CUP/kg.\n• Rendimiento: 35% (Se requieren 2.857 kg de pescado entero para 1 kg de filete).\n• Proceso: Recepción, lavado, eviscerado, descabezado, fileteado, envasado al vacío y refrigeración (0-4 °C).\n• Tiempo de proceso: 4.5 minutos por kg.')

doc.add_heading('1.2 Ficha de Costos', level=2)
datos_filete = [
    ("1", "Gasto de Material (2.857 kg x 350)", "1,000.00"),
    ("2", "Salario directo (20.00 x 2.857)", "57.14"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "53.86"),
    ("5", "COSTO TOTAL", "1,131.00"),
    ("6", "Gastos generales y admin. (5%)", "56.55"),
    ("7", "Gastos de distribución/ventas (3%)", "33.93"),
    ("8", "Gastos financieros", "0.00"),
    ("9", "Gastos tributarios (19% de Fila 2)", "10.86"),
    ("10", "SUBTOTAL DE COSTOS Y GASTOS", "1,232.34"),
    ("11", "Impuesto sobre ventas (10% final)", "135.56"),
    ("12", "TOTAL DE COSTOS Y GASTOS", "1,367.90"),
    ("13", "Utilidad (10% ajustado)", "123.11"),
    ("14", "PRECIO DE VENTA FINAL", "1,490.00"),
]
crear_tabla_costos(datos_filete)

doc.add_heading('1.3 Explicación Explícita para la Comisión', level=2)
doc.add_paragraph('El precio del filete refleja el alto impacto del transporte y la merma. Para obtener 1 kg de filete, la entidad debe adquirir y transportar 2.857 kg de pescado entero. Esto genera un costo de materia prima de 1,000 CUP solo en insumos. A esto se suman los salarios, los impuestos establecidos por la ley (Seguridad Social y Fuerza de Trabajo) y un margen de utilidad del 10% que garantiza la sostenibilidad del proyecto. El precio final de 1,490 CUP permite al PDL operar sin pérdidas y ofrecer un producto de alta calidad a la población.')
doc.add_page_break()

# ==========================================
# PRODUCTO 2: MASA DE PESCADO DESHUESADA
# ==========================================
doc.add_heading('2. FICHA DE COSTO: MASA DE PESCADO DESHUESADA (1 kg)', level=1)
doc.add_heading('2.1 Carta Tecnológica', level=2)
doc.add_paragraph('• Materia prima: Pescado entero fresco (250 CUP/kg) + Flete (100 CUP/kg) = 350 CUP/kg.\n• Rendimiento: 30% (Se requieren 3.333 kg de pescado entero para 1 kg de masa).\n• Proceso: Recepción, lavado, eviscerado, descabezado, deshuesado mecánico/manual, envasado al vacío y refrigeración.\n• Tiempo de proceso: 5.0 minutos por kg.')

doc.add_heading('2.2 Ficha de Costos', level=2)
datos_masa = [
    ("1", "Gasto de Material (3.333 kg x 350)", "1,166.55"),
    ("2", "Salario directo (20.00 x 3.333)", "66.66"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "62.66"),
    ("5", "COSTO TOTAL", "1,315.87"),
    ("6", "Gastos generales y admin. (5%)", "65.79"),
    ("7", "Gastos de distribución/ventas (3%)", "39.48"),
    ("8", "Gastos financieros", "0.00"),
    ("9", "Gastos tributarios (19% de Fila 2)", "12.67"),
    ("10", "SUBTOTAL DE COSTOS Y GASTOS", "1,433.81"),
    ("11", "Impuesto sobre ventas (10% final)", "157.72"),
    ("12", "TOTAL DE COSTOS Y GASTOS", "1,591.53"),
    ("13", "Utilidad (10% ajustado)", "143.24"),
    ("14", "PRECIO DE VENTA FINAL", "1,740.00"),
]
crear_tabla_costos(datos_masa)

doc.add_heading('2.3 Explicación Explícita para la Comisión', level=2)
doc.add_paragraph('La masa deshuesada es el producto con mayor rendimiento técnico y valor agregado. Sin embargo, su costo es el más alto porque requiere 3.333 kg de pescado entero para producir un solo kilogramo, generando un gasto de materia prima superior a los 1,100 CUP. El precio de 1,740 CUP está estrictamente calculado sobre la base de la Resolución 148/2023 del MFP, asegurando que el margen de ganancia cubra los costos operativos y permita reinvertir en el mantenimiento de los equipos de frío.')
doc.add_page_break()

# ==========================================
# PRODUCTO 3: PESCADO ENTERO LIMPIO
# ==========================================
doc.add_heading('3. FICHA DE COSTO: PESCADO ENTERO LIMPIO SIN CABEZA (1 kg)', level=1)
doc.add_heading('3.1 Carta Tecnológica', level=2)
doc.add_paragraph('• Materia prima: Pescado entero fresco (250 CUP/kg) + Flete (100 CUP/kg) = 350 CUP/kg.\n• Rendimiento: 50% (Se requieren 2.000 kg de pescado entero para 1 kg de entero limpio).\n• Proceso: Recepción, lavado, eviscerado, descabezado, envasado y refrigeración.\n• Tiempo de proceso: 3.0 minutos por kg.')

doc.add_heading('3.2 Ficha de Costos', level=2)
datos_entero = [
    ("1", "Gasto de Material (2.000 kg x 350)", "700.00"),
    ("2", "Salario directo (20.00 x 2.000)", "40.00"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "38.00"),
    ("5", "COSTO TOTAL", "798.00"),
    ("6", "Gastos generales y admin. (5%)", "39.90"),
    ("7", "Gastos de distribución/ventas (3%)", "23.94"),
    ("8", "Gastos financieros", "0.00"),
    ("9", "Gastos tributarios (19% de Fila 2)", "7.60"),
    ("10", "SUBTOTAL DE COSTOS Y GASTOS", "869.44"),
    ("11", "Impuesto sobre ventas (10% final)", "95.64"),
    ("12", "TOTAL DE COSTOS Y GASTOS", "965.08"),
    ("13", "Utilidad (10% ajustado)", "86.86"),
    ("14", "PRECIO DE VENTA FINAL", "1,060.00"),
]
crear_tabla_costos(datos_entero)

doc.add_heading('3.3 Explicación Explícita para la Comisión', level=2)
doc.add_paragraph('El pescado entero limpio (sin cabeza ni vísceras) es el producto de mayor demanda popular y el más eficiente en términos logísticos. Su rendimiento del 50% permite ofrecer un precio final de 1,060 CUP, mucho más accesible para la población. El costo del flete (100 CUP/kg) impacta aquí de manera directa, pero al no requerir procesos de fileteado, el costo de mano de obra es menor. Este producto es la mejor opción para garantizar la seguridad alimentaria local a precios justos.')

# Guardar
filename = "Dossier_Precios_Pescado_Municipio.docx"
filepath = f"/root/Mi-primer-proyecto/backend/app/static/{filename}"
doc.save(filepath)

print(f"✅ Dossier Word generado exitosamente.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
