from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def crear_convenio_ganado_final():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    title = doc.add_heading('CONVENIO DE PRODUCCIÓN COOPERADA - GANADO MAYOR (LECHE Y CEBA)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph('En el municipio de Quivicán, a los ___ días del mes de _______ de 2026, se reúnen por una parte la CPA 17 de Mayo, representada por su Presidente, y por la otra el PDL AQUAPÓNICA, representado por Yosbel Collazo Avila, bajo las siguientes cláusulas:')

    doc.add_heading('I. OBJETO DEL CONVENIO', level=2)
    doc.add_paragraph('1.1. Establecer un encadenamiento productivo para la producción de leche y la ceba de toros, con el objetivo de generar flujos de caja que permitan saldar la deuda de 5,000,000 CUP del PDL Aquapónica con el Banco Popular de Ahorro (BPA) y crear un polo productivo rentable y sostenible.')

    doc.add_heading('II. OBLIGACIONES DE LAS PARTES', level=2)
    doc.add_paragraph('2.1. LA CPA: Aportar las tierras para pastoreo, el ganado base inicial (11 terneros y 3 añojos) y el 50% del capital de trabajo inicial.')
    doc.add_paragraph('2.2. EL PDL: Aportar la infraestructura (establo, comederos, paneles solares), la gestión técnica, el agua, la atención veterinaria y la organización de la fuerza de trabajo.')
    doc.add_paragraph('2.3. FUERZA DE TRABAJO: Se establece una plantilla de 6 trabajadores (1 Mayoral, 3 Vaqueros, 1 Boyero, 1 Guardia). El salario será de 500 CUP/día en el Año 1, subiendo a 750 en el Año 2 y 1,000 en el Año 3, más el 19% de impuestos.')

    doc.add_heading('III. PLAN DE INVERSIÓN Y AUTOFINANCIAMIENTO', level=2)
    doc.add_paragraph('3.1. Las partes acuerdan NO solicitar nuevos créditos bancarios para la ceba. El crecimiento del rebaño se hará mediante el autofinanciamiento generado por las ganancias de la leche y las ventas escalonadas de carne.')
    doc.add_paragraph('3.2. La producción de leche se mantendrá de forma lineal en 3 litros/vaca/día. La carne se venderá en pie a 750 CUP/kg, con un peso final de 480 kg por animal.')

    doc.add_heading('IV. DISTRIBUCIÓN DE INGRESOS Y PAGO DE DEUDA', level=2)
    doc.add_paragraph('4.1. Los ingresos cubrirán primero la nómina y los gastos operativos. Las utilidades netas se destinarán a la compra de nuevos añojos para la ceba.')
    doc.add_paragraph('4.2. El excedente de efectivo se aplicará estrictamente al pago de la deuda del PDL Aquapónica con el BPA. El pago se realizará mediante amortizaciones anuales de 1,000,000 CUP de capital, más los intereses del 4% sobre el saldo pendiente, iniciando en el Año 1.')

    doc.add_heading('V. CIRCUNSTANCIAS EXIMENTES (FUERZA MAYOR)', level=2)
    doc.add_paragraph('5.1. Las partes no serán responsables por incumplimientos derivados de fenómenos naturales (huracanes, sequías prolongadas) o falta de insumos ajenos a su control, previa certificación de la autoridad competente.')

    doc.add_heading('VI. PENALIDADES', level=2)
    doc.add_paragraph('6.1. En caso de mora, se aplicará la penalidad escalonada del 0.05% al 0.12% según los días de atraso, con un tope del 4% del valor total.')

    doc.add_heading('VII. VIGENCIA Y FIRMAS', level=2)
    doc.add_paragraph('7.1. El presente convenio tiene una vigencia de 5 años y se firma por duplicado a los ___ días del mes de _______ de 2026.')
    
    doc.add_paragraph('\n\n___________________________\nPresidente CPA 17 de Mayo')
    doc.add_paragraph('___________________________\nYosbel Collazo Avila\nPDL AQUAPÓNICA')

    # --- ANEXO 1 ---
    doc.add_page_break()
    doc.add_heading('ANEXO No. 1: ESTUDIO DE FACTIBILIDAD (PROYECCIÓN CONSERVADORA A 5 AÑOS)', level=1)
    doc.add_paragraph('Proyección financiera del modelo de Leche (3 Lts lineales) y Ceba Autofinanciada (4-5 toros anuales), con pago de deuda desde el Año 1.')
    
    table = doc.add_table(rows=1, cols=5)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Concepto'
    hdr_cells[1].text = 'Año 1'
    hdr_cells[2].text = 'Año 2'
    hdr_cells[3].text = 'Año 3'
    hdr_cells[4].text = 'Año 4/5'

    rows = [
        ("Ingresos Leche (3 Lts)", "3,285,000", "3,285,000", "3,285,000", "3,285,000"),
        ("Ingresos Carne (4-5 toros)", "1,440,000", "1,620,000", "1,800,000", "1,800,000"),
        ("Total Ingresos", "4,725,000", "4,905,000", "5,085,000", "5,085,000"),
        ("Gastos Operativos", "(1,653,050)", "(2,304,575)", "(2,956,100)", "(2,956,100)"),
        ("Utilidad Bruta", "3,071,950", "2,600,425", "2,128,900", "2,128,900"),
        ("Pago al Banco (Cap. + Int.)", "(1,200,000)", "(1,160,000)", "(1,120,000)", "(1,060,000)"),
        ("UTILIDAD NETA", "1,871,950", "1,440,425", "1,008,900", "1,068,900"),
        ("Reinversión (Compra Ganado)", "(500,000)", "(800,000)", "(800,000)", "(800,000)"),
        ("EFECTIVO LIBRE", "+1,371,950", "+640,425", "+208,900", "+268,900")
    ]

    for r in rows:
        row_cells = table.add_row().cells
        row_cells[0].text = r[0]
        row_cells[1].text = r[1]
        row_cells[2].text = r[2]
        row_cells[3].text = r[3]
        row_cells[4].text = r[4]
        
    doc.add_paragraph('\nConclusión del Estudio: El proyecto demuestra una viabilidad financiera ajustada y realista. La producción de leche cubre la totalidad de los costos operativos (nómina y gastos), mientras que la ceba genera el flujo necesario para amortizar 1 Millón de CUP anuales al Banco, garantizando la solvencia del PDL Aquapónica sin comprometer el capital de trabajo.')

    filename = "2_Convenio_Ganado_Final_Anexo.docx"
    filepath = f"/root/Mi-primer-proyecto/backend/app/static/{filename}"
    doc.save(filepath)
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

crear_convenio_ganado_final()
