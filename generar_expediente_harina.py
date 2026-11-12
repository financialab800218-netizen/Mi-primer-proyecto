from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from datetime import datetime
import os

def crear_expediente_harina():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    # --- PORTADA ---
    title = doc.add_heading('EXPEDIENTE TÉCNICO: HARINA DE PESCADO CONDIMENTADA', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'\nEntidad: PDL DESSPEZ / PDL AQUAPÓNICA\nFecha: {datetime.now().strftime("%d/%m/%Y")}\nDocumento Oficial para la Comisión de Precios')
    run.font.size = Pt(10)
    run.italic = True
    
    # --- 1. CARTA TECNOLÓGICA ---
    doc.add_heading('1. CARTA TECNOLÓGICA Y PROCESO OPERATIVO', level=1)
    doc.add_paragraph('A continuación se detallan los pasos técnicos para la elaboración de 1 kg de Harina de Pescado Condimentada, garantizando la inocuidad y calidad del producto:')
    
    pasos = [
        "Recepción y Lavado: Recibir el pescado fresco, verificar su estado organoléptico y lavarlo con agua potable para eliminar sangre y suciedad.",
        "Cocción: Someter el pescado a cocción por vapor o agua caliente para coagular las proteínas y facilitar la separación de la grasa.",
        "Prensado: Separar el líquido (agua y aceite) de la masa sólida utilizando una prensa mecánica.",
        "Secado: Extender la masa y secarla al sol (en secaderos solares) o en horno a baja temperatura hasta alcanzar una humedad menor al 10%.",
        "Molienda: Triturar el pescado seco en un molino hasta obtener un polvo fino y homogéneo (harina base).",
        "Mezclado (Adición de Sazón): Incorporar el sazón completo en una proporción exacta del 5% (50 gramos de sazón por cada 1 kg de harina base). Mezclar hasta lograr una distribución uniforme del color y sabor.",
        "Empaque: Envasar en bolsas herméticas de alta densidad o pomos de plástico sellados para evitar la humedad.",
        "Etiquetado: Colocar la etiqueta con fecha de producción, fecha de vencimiento (6 meses), peso neto y registro sanitario."
    ]
    
    for paso in pasos:
        doc.add_paragraph(paso, style='List Number')
        
    doc.add_heading('Equipos y Normas de Higiene:', level=2)
    doc.add_paragraph('Equipos: Mesas inoxidables, cocina industrial o caldera, prensa, secadero solar/horno, molino de martillo, balanza digital, mezcladora.\nNormas: Uso obligatorio de cofia, nasobuco, guantes y delantal. Lavado de manos antes y después de cada operación. Desinfección de utensilios y superficies cada 2 horas. Temperatura de sala de proceso ≤ 12 °C durante la manipulación de materia prima.')
    
    # --- 2. FICHA DE COSTOS ---
    doc.add_heading('2. FICHA DE COSTOS Y TARIFAS', level=1)
    doc.add_paragraph('Cálculo basado en la Resolución 148/2023 del MFP, incluyendo materia prima (pescado entero a 250 CUP + transporte 100 CUP) y adición de sazón al 5%.')
    
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fila'
    hdr_cells[1].text = 'Conceptos'
    hdr_cells[2].text = 'Importe (CUP)'
    
    datos = [
        ("1", "Gasto de Material (Pescado 4kg x 350 CUP + Sazón 50g x 12,500 CUP)", "2,025.00"),
        ("2", "Salario directo (20.00 x 7.0 min)", "140.00"),
        ("3", "Otros gastos directos (Empaque hermético + Etiqueta)", "30.00"),
        ("4", "Gastos asociados a producción (5%)", "109.75"),
        ("5", "COSTO TOTAL", "2,304.75"),
        ("6", "Gastos generales y admin. (5%)", "115.24"),
        ("7", "Gastos de distribución/ventas (3%)", "69.14"),
        ("8", "Gastos financieros", "0.00"),
        ("9", "Gastos tributarios (19% de Fila 2)", "26.60"),
        ("10", "SUBTOTAL DE COSTOS Y GASTOS", "2,515.73"),
        ("11", "Impuesto sobre ventas (10% final)", "279.53"),
        ("12", "TOTAL DE COSTOS Y GASTOS", "2,795.26"),
        ("13", "Utilidad (10% ajustado)", "251.57"),
        ("14", "PRECIO DE VENTA FINAL", "3,050.00"),
    ]
    
    for fila, concepto, importe in datos:
        row_cells = table.add_row().cells
        row_cells[0].text = fila
        row_cells[1].text = concepto
        row_cells[2].text = importe
        
    # --- 3. EXPLICACIÓN ---
    doc.add_heading('3. EXPLICACIÓN Y JUSTIFICACIÓN PARA LA COMISIÓN', level=1)
    doc.add_paragraph('La Harina de Pescado Condimentada es un producto de alto valor agregado que resuelve dos problemas fundamentales en la economía cubana: la necesidad de proteína animal y la falta de cadena de frío. Al eliminar el agua del pescado (reduciendo su peso en un 75%), obtenemos un producto que se conserva por meses a temperatura ambiente sin necesidad de electricidad.')
    doc.add_paragraph('El precio final de 3,050 CUP por kilogramo está estrictamente calculado. El sazón representa el 22% del costo de material (625 CUP), pero es lo que le da el valor de mercado y la aceptación popular. Si el PDL logra utilizar los desechos del fileteado (espinas, piel, cabezas) en lugar de pescado entero, el costo de la materia prima cae drásticamente, permitiendo ofrecer un precio aún más competitivo a la población sin perder rentabilidad.')
    
    filename = "Expediente_Harina_Pescado.docx"
    filepath = f"/root/Mi-primer-proyecto/backend/app/static/{filename}"
    doc.save(filepath)
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

crear_expediente_harina()
