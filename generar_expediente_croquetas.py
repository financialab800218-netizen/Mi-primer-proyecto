from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from datetime import datetime

def crear_expediente_croquetas():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    # --- PORTADA ---
    title = doc.add_heading('EXPEDIENTE TECNICO: CROQUETAS DE CALDO DE PESCADO', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'\nEntidad: PDL DESSPEZ / PDL AQUAPONICA\nFecha: {datetime.now().strftime("%d/%m/%Y")}\nDocumento Oficial para la Comision de Precios')
    run.font.size = Pt(10)
    run.italic = True
    
    # --- 1. CARTA TECNOLOGICA ---
    doc.add_heading('1. CARTA TECNOLOGICA Y PROCESO OPERATIVO', level=1)
    doc.add_paragraph('A continuacion se detallan los pasos tecnicos para la elaboracion de 1 kg de masa de croquetas de caldo de pescado:')
    
    pasos = [
        "Preparacion del caldo: Colar bien el caldo resultante de la coccion del pescado.",
        "Mezclado: En caliente, incorporar la harina de trigo poco a poco al caldo, removiendo constantemente para evitar grumos.",
        "Sazonado: Anadir el sazon completo en una proporcion del 1% (10 gramos por cada 1 kg de masa).",
        "Coccion: Cocinar a fuego lento hasta que la masa espese y se despegue del fondo.",
        "Enfriado: Extender en bandejas y dejar enfriar en camara.",
        "Moldeado y Empaque: Formar las croquetas y empacar en bandejas de foam con film plastico.",
        "Refrigeracion/Congelacion: Mantener a 0-4 C para consumo en 48 horas, o congelar a -18 C."
    ]
    
    for paso in pasos:
        doc.add_paragraph(paso, style='List Number')
        
    doc.add_heading('Equipos y Normas de Higiene:', level=2)
    doc.add_paragraph('Equipos: Mesas inoxidables, olla industrial, cuchara de madera o paleta, bandejas, camara de refrigeracion.\nNormas: Uso obligatorio de cofia, nasobuco, guantes y delantal. Lavado de manos antes y despues de cada operacion.')

    # --- 2. FICHA DE COSTOS ---
    doc.add_heading('2. FICHA DE COSTOS Y TARIFAS', level=1)
    doc.add_paragraph('Calculo basado en la Resolucion 148/2023 del MFP, con harina de trigo a 800 CUP/kg y sazon al 1%.')
    
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fila'
    hdr_cells[1].text = 'Conceptos'
    hdr_cells[2].text = 'Importe (CUP)'
    
    datos = [
        ("1", "Gasto de Material (Caldo 0.4kg + Harina 0.4kg + Sazon 10g)", "465.00"),
        ("2", "Salario directo (20.00 x 7.5 min)", "150.00"),
        ("3", "Otros gastos directos (Empaque + Etiqueta)", "30.00"),
        ("4", "Gastos asociados a produccion (5%)", "32.25"),
        ("5", "COSTO TOTAL", "677.25"),
        ("6", "Gastos generales y admin. (5%)", "33.86"),
        ("7", "Gastos de distribucion/ventas (3%)", "20.32"),
        ("8", "Gastos financieros", "0.00"),
        ("9", "Gastos tributarios (19%)", "28.50"),
        ("10", "SUBTOTAL DE COSTOS Y GASTOS", "759.93"),
        ("11", "Impuesto sobre ventas (10%)", "84.44"),
        ("12", "TOTAL DE COSTOS Y GASTOS", "844.37"),
        ("13", "Utilidad (10% ajustado)", "75.99"),
        ("14", "PRECIO DE VENTA FINAL (por kg)", "920.00"),
    ]
    
    for fila, concepto, importe in datos:
        row_cells = table.add_row().cells
        row_cells[0].text = fila
        row_cells[1].text = concepto
        row_cells[2].text = importe

    # --- 3. EXPLICACION ---
    doc.add_heading('3. EXPLICACION Y JUSTIFICACION PARA LA COMISION', level=1)
    doc.add_paragraph('La masa de croquetas de caldo de pescado es un producto de alto valor social y economico. Se elabora a partir del caldo resultante de la coccion del pescado (un subproducto que antes se desechaba), lo que reduce drasticamente el costo de la materia prima y aprovecha al maximo el recurso pesquero.')
    doc.add_paragraph('El precio final de 920 CUP/kg es altamente competitivo y accesible para la poblacion. Al utilizar solo un 1% de sazon completo, se logra un sabor agradable y uniforme sin encarecer el producto con condimentos frescos (cuya disponibilidad y precio son volatiles en el mercado). Es un alimento rendidor, de facil preparacion y con un excelente aporte proteico.')

    filename = "Expediente_Croquetas_Pescado.docx"
    filepath = f"/root/Mi-primer-proyecto/backend/app/static/{filename}"
    doc.save(filepath)
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

crear_expediente_croquetas()
