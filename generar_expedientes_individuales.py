from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from datetime import datetime
import os

def crear_documento(nombre_archivo, titulo_producto, proceso_pasos, tabla_datos, explicacion, equipos):
    doc = Document()
    
    # Estilos
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)

    # Portada / Encabezado
    title = doc.add_heading(f'EXPEDIENTE TÉCNICO: {titulo_producto.upper()}', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'\nEntidad: PDL DESSPEZ\nFecha: {datetime.now().strftime("%d/%m/%Y")}\nDocumento Oficial para la Comisión de Precios')
    run.font.size = Pt(10)
    run.italic = True
    
    doc.add_heading('1. CARTA TECNOLÓGICA Y PROCESO OPERATIVO', level=1)
    doc.add_paragraph('A continuación se detallan los pasos técnicos y las normas de manipulación para garantizar la inocuidad y calidad del producto:')
    for paso in proceso_pasos:
        doc.add_paragraph(paso, style='List Number')
        
    doc.add_heading('Equipos y Normas de Higiene:', level=2)
    doc.add_paragraph(equipos)
    
    doc.add_heading('2. FICHA DE COSTOS Y TARIFAS', level=1)
    doc.add_paragraph('Cálculo basado en la Resolución 148/2023 del MFP, incluyendo materia prima (250 CUP) y transporte (100 CUP).')
    
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fila'
    hdr_cells[1].text = 'Conceptos'
    hdr_cells[2].text = 'Importe (CUP)'
    
    for fila, concepto, importe in tabla_datos:
        row_cells = table.add_row().cells
        row_cells[0].text = str(fila)
        row_cells[1].text = concepto
        row_cells[2].text = str(importe)
        
    doc.add_heading('3. EXPLICACIÓN Y JUSTIFICACIÓN', level=1)
    doc.add_paragraph(explicacion)
    
    # Guardar
    filepath = f"/root/Mi-primer-proyecto/backend/app/static/{nombre_archivo}"
    doc.save(filepath)
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{nombre_archivo}")


# ==========================================
# 1. FILETE DE PESCADO
# ==========================================
pasos_filete = [
    "Recepción y Lavado: Recibir el pescado a 0-4 °C y lavarlo con agua potable.",
    "Eviscerado y Descabezado: Extraer vísceras y cortar la cabeza.",
    "Fileteado: Corte longitudinal desde la cola hasta la cabeza, siguiendo la espina dorsal.",
    "Despellejado: Separar la piel del músculo del filete.",
    "Desespinado: Retirar manualmente cualquier espina residual.",
    "Empaque: Empacar en bolsas de nailon o al vacío.",
    "Refrigeración: Mantener a 0-4 °C."
]
tabla_filete = [
    ("1", "Gasto de Material (2.857 kg x 350)", "1,000.00"),
    ("2", "Salario directo (20.00 x 2.857)", "57.14"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "53.86"),
    ("5", "COSTO TOTAL", "1,131.00"),
    ("6", "Gastos generales y admin. (5%)", "56.55"),
    ("7", "Gastos de distribución/ventas (3%)", "33.93"),
    ("8", "Gastos tributarios (19% de Fila 2)", "10.86"),
    ("9", "SUBTOTAL DE COSTOS Y GASTOS", "1,232.34"),
    ("10", "Impuesto sobre ventas (10%)", "135.56"),
    ("11", "TOTAL DE COSTOS Y GASTOS", "1,367.90"),
    ("12", "Utilidad (10% ajustado)", "123.11"),
    ("13", "PRECIO DE VENTA FINAL", "1,490.00"),
]
explicacion_filete = "El precio del filete refleja el impacto del transporte y la merma del 65% (solo se aprovecha el 35% del pescado). Para obtener 1 kg, la entidad debe adquirir y mover 2.857 kg. El precio de 1,490 CUP garantiza cubrir los altos costos de materia prima, salarios, impuestos y un margen del 10% para reinversión en cadena de frío."
equipos_filete = "Mesas inoxidables, cuchillos de filetear, pinzas, tabla de polietileno, balanza. Normas: Cofia, nasobuco, guantes. Desinfección cada 2 horas. Temperatura de sala ≤ 12 °C."

crear_documento("Expediente_Filete_Pescado.docx", "Filete de Pescado (1 kg)", pasos_filete, tabla_filete, explicacion_filete, equipos_filete)

# ==========================================
# 2. MASA DESHUESADA
# ==========================================
pasos_masa = [
    "Preparación Base: Lavado, eviscerado, descabezado y fileteado.",
    "Deshuesado: Pasar los filetes por separadora de carne o proceso manual para extraer la masa muscular.",
    "Inspección de Calidad: Verificar ausencia de escamas, piel o espinas.",
    "Envasado al Vacío: Obligatorio para evitar oxidación.",
    "Etiquetado: Fecha de producción, vencimiento y peso neto.",
    "Congelación: Almacenar a -18 °C para mantener propiedades."
]
tabla_masa = [
    ("1", "Gasto de Material (3.333 kg x 350)", "1,166.55"),
    ("2", "Salario directo (20.00 x 3.333)", "66.66"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "62.66"),
    ("5", "COSTO TOTAL", "1,315.87"),
    ("6", "Gastos generales y admin. (5%)", "65.79"),
    ("7", "Gastos de distribución/ventas (3%)", "39.48"),
    ("8", "Gastos tributarios (19% de Fila 2)", "12.67"),
    ("9", "SUBTOTAL DE COSTOS Y GASTOS", "1,433.81"),
    ("10", "Impuesto sobre ventas (10%)", "157.72"),
    ("11", "TOTAL DE COSTOS Y GASTOS", "1,591.53"),
    ("12", "Utilidad (10% ajustado)", "143.24"),
    ("13", "PRECIO DE VENTA FINAL", "1,740.00"),
]
explicacion_masa = "La masa deshuesada es el producto de mayor valor agregado, pero también el más costoso de producir. Requiere 3.333 kg de pescado entero (350 CUP/kg con transporte) para generar 1 kg de masa (rendimiento del 30%). El precio de 1,740 CUP cubre los costos operativos, el empaque al vacío obligatorio y garantiza la sostenibilidad del proceso industrial."
equipos_masa = "Máquina deshuesadora de carne, empacadora al vacío, mesas inoxidables, cuchillos. Normas: Temperatura de sala ≤ 12 °C. Procesamiento rápido para evitar pérdida de frescura."

crear_documento("Expediente_Masa_Pescado.docx", "Masa de Pescado Deshuesada (1 kg)", pasos_masa, tabla_masa, explicacion_masa, equipos_masa)

# ==========================================
# 3. ENTERO LIMPIO (H&G)
# ==========================================
pasos_entero = [
    "Recepción y Pesaje: Verificar temperatura y registrar entrada.",
    "Lavado Inicial: Eliminar sangre, mucosidad y suciedad externa.",
    "Eviscerado: Corte en el vientre y extracción de vísceras.",
    "Descabezado: Corte limpio detrás de las agallas.",
    "Enjuague Final: Lavar cavidad abdominal.",
    "Empaque: Bolsas de nailon grado alimenticio y etiquetado.",
    "Refrigeración: Almacenar a 0-4 °C o congelar a -18 °C."
]
tabla_entero = [
    ("1", "Gasto de Material (2.000 kg x 350)", "700.00"),
    ("2", "Salario directo (20.00 x 2.000)", "40.00"),
    ("3", "Otros gastos directos (Empaque/Etiqueta)", "20.00"),
    ("4", "Gastos asociados a producción (5%)", "38.00"),
    ("5", "COSTO TOTAL", "798.00"),
    ("6", "Gastos generales y admin. (5%)", "39.90"),
    ("7", "Gastos de distribución/ventas (3%)", "23.94"),
    ("8", "Gastos tributarios (19% de Fila 2)", "7.60"),
    ("9", "SUBTOTAL DE COSTOS Y GASTOS", "869.44"),
    ("10", "Impuesto sobre ventas (10%)", "95.64"),
    ("11", "TOTAL DE COSTOS Y GASTOS", "965.08"),
    ("12", "Utilidad (10% ajustado)", "86.86"),
    ("13", "PRECIO DE VENTA FINAL", "1,060.00"),
]
explicacion_entero = "El pescado entero limpio es el producto de mayor eficiencia logística (rendimiento del 50%) y el de menor costo para el consumidor final. Solo requiere 2 kg de materia prima para 1 kg de producto terminado. El precio de 1,060 CUP representa la opción más accesible para garantizar la seguridad alimentaria local, manteniendo un margen del 10%."
equipos_entero = "Mesas inoxidables, cuchillos, balanza digital, cámara frigorífica. Normas: Cofia, nasobuco, guantes. Lavado de manos antes y después de cada operación."

crear_documento("Expediente_Entero_Limpio_Pescado.docx", "Pescado Entero Limpio sin Cabeza (1 kg)", pasos_entero, tabla_entero, explicacion_entero, equipos_entero)
