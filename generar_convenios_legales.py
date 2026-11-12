from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

def crear_convenio_cana():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    title = doc.add_heading('CONVENIO DE PRODUCCIÓN COOPERADA (CAÑA)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph('En el municipio de Quivicán, a los ___ días del mes de _______ de 2026, se reúnen por una parte la CPA 17 de Mayo, representada por su Presidente, y por la otra el PDL AQUAPÓNICA, representado por Yosbel Collazo Avila, bajo las siguientes cláusulas:')

    doc.add_heading('I. OBJETO DEL CONVENIO', level=2)
    doc.add_paragraph('1.1. Prorrogar el encadenamiento productivo y reestructurar la deuda existente, reconociendo que la CPA no ha podido saldar los 4,000,000 CUP por causas de fuerza mayor (sequía, falta de combustible) y que el PDL Aquapónica asumió el crédito bancario.')
    doc.add_paragraph('1.2. Establecer que el pago se realizará mediante la cesión de derechos de cobro de la Zafra 2026-2027, con cierre el 30 de junio de 2027.')

    doc.add_heading('II. OBLIGACIONES DE LAS PARTES', level=2)
    doc.add_paragraph('2.1. LA CPA: Garantizar la siembra, el corte y el tiro de la caña hacia el central azucarero. Mantener informado al PDL sobre los rendimientos.')
    doc.add_paragraph('2.2. EL PDL: Aportar la gestión técnica, los insumos y servir de enlace con el Banco para la reestructuración de la deuda.')
    doc.add_paragraph('2.3. CESIÓN DE COBRO: LA CPA autoriza irrevocablemente a AZCUBA a transferir los fondos de la liquidación de la zafra directamente a la cuenta del PDL AQUAPÓNICA (Cuenta No. 1221730000388010 en el BPA). El PDL actuará como agente recaudador para pagar al banco.')

    doc.add_heading('III. PLAZOS PARA EL CUMPLIMIENTO', level=2)
    doc.add_paragraph('3.1. Las partes acuerdan que el pago total de la deuda se realizará en un plazo máximo de 12 meses posteriores al cierre de la zafra (30 de junio de 2027).')

    doc.add_heading('IV. CIRCUNSTANCIAS EXIMENTES (FUERZA MAYOR)', level=2)
    doc.add_paragraph('4.1. Si la zafra 2026-2027 no se realizara por causas climáticas o de otra índole, el plazo se extiende automáticamente hasta la próxima zafra, sin penalización para las partes, previa certificación de la autoridad competente.')

    doc.add_heading('V. PENALIDADES', level=2)
    doc.add_paragraph('5.1. En caso de mora, se aplicará una penalidad del 0.05% durante los primeros 30 días, 0.08% hasta 60 días y 0.12% por más de 90 días, calculado sobre el valor de la factura.')

    doc.add_heading('VI. VIGENCIA Y FIRMAS', level=2)
    doc.add_paragraph('6.1. El presente convenio tiene una vigencia de 5 años y se firma por duplicado a los ___ días del mes de _______ de 2026.')
    
    doc.add_paragraph('\n\n___________________________\nPresidente CPA 17 de Mayo')
    doc.add_paragraph('___________________________\nYosbel Collazo Avila\nPDL AQUAPÓNICA')

    filename = "1_Convenio_Cana_Oficial.docx"
    doc.save(f"/root/Mi-primer-proyecto/backend/app/static/{filename}")
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

def crear_convenio_ganado():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    title = doc.add_heading('CONVENIO DE PRODUCCIÓN COOPERADA - GANADO MAYOR (LECHE Y CEBA)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph('En el municipio de Quivicán, a los ___ días del mes de _______ de 2026, se reúnen por una parte la CPA 17 de Mayo, representada por su Presidente, y por la otra el PDL AQUAPÓNICA, representado por Yosbel Collazo Avila, bajo las siguientes cláusulas:')

    doc.add_heading('I. OBJETO DEL CONVENIO', level=2)
    doc.add_paragraph('1.1. Establecer un nuevo encadenamiento productivo para la producción de leche y la ceba de toros, con el objetivo de generar flujos de caja que permitan saldar la deuda del PDL Aquapónica con el BPA y crear un polo productivo rentable.')

    doc.add_heading('II. OBLIGACIONES DE LAS PARTES', level=2)
    doc.add_paragraph('2.1. LA CPA: Aportar las tierras para pastoreo y el ganado base inicial (11 terneros y 3 añojos).')
    doc.add_paragraph('2.2. EL PDL: Aportar la infraestructura (establo, comederos, paneles solares), la gestión técnica, el agua, la atención veterinaria y la organización de la fuerza de trabajo.')
    doc.add_paragraph('2.3. FUERZA DE TRABAJO: Se establece una plantilla de 6 trabajadores (1 Mayoral, 3 Vaqueros, 1 Boyero, 1 Guardia). El salario será de 500 CUP/día en el Año 1, subiendo a 750 en el Año 2 y 1,000 en el Año 3, más el 19% de impuestos.')

    doc.add_heading('III. PLAN DE INVERSIÓN Y AUTOFINANCIAMIENTO', level=2)
    doc.add_paragraph('3.1. Las partes acuerdan NO solicitar nuevos créditos bancarios para la ceba. El crecimiento del rebaño se hará mediante el autofinanciamiento generado por las ganancias de la leche y las ventas escalonadas de carne.')
    doc.add_paragraph('3.2. La producción de leche iniciará con 3 litros/vaca/día y escalará a 4 litros en el Año 3. La carne se venderá en pie a 750 CUP/kg.')

    doc.add_heading('IV. DISTRIBUCIÓN DE INGRESOS', level=2)
    doc.add_paragraph('4.1. Los ingresos cubrirán primero la nómina y los gastos operativos. Las utilidades netas se destinarán a la compra de nuevos añojos para la ceba.')
    doc.add_paragraph('4.2. El excedente de efectivo (Año 2 y 3) se aplicará al pago de la deuda del PDL Aquapónica con el BPA, actuando este convenio como garantía de solvencia.')

    doc.add_heading('V. CIRCUNSTANCIAS EXIMENTES (FUERZA MAYOR)', level=2)
    doc.add_paragraph('5.1. Las partes no serán responsables por incumplimientos derivados de fenómenos naturales (huracanes, sequías prolongadas) o falta de insumos ajenos a su control.')

    doc.add_heading('VI. PENALIDADES', level=2)
    doc.add_paragraph('6.1. En caso de mora, se aplicará la penalidad escalonada del 0.05% al 0.12% según los días de atraso, con un tope del 4% del valor total.')

    doc.add_heading('VII. VIGENCIA Y FIRMAS', level=2)
    doc.add_paragraph('7.1. El presente convenio tiene una vigencia de 5 años y se firma por duplicado a los ___ días del mes de _______ de 2026.')
    
    doc.add_paragraph('\n\n___________________________\nPresidente CPA 17 de Mayo')
    doc.add_paragraph('___________________________\nYosbel Collazo Avila\nPDL AQUAPÓNICA')

    # --- ANEXO 1 ---
    doc.add_page_break()
    doc.add_heading('ANEXO No. 1: ESTUDIO DE FACTIBILIDAD (PROYECCIÓN A 4 AÑOS)', level=1)
    doc.add_paragraph('Proyección financiera del modelo de Leche y Ceba Autofinanciada (6 trabajadores).')
    
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Concepto'
    hdr_cells[1].text = 'Año 1'
    hdr_cells[2].text = 'Año 2'
    hdr_cells[3].text = 'Año 3'

    # Add rows (Simplified for the document)
    rows = [
        ("Ingresos Leche", "3,285,000", "3,832,500", "4,380,000"),
        ("Ingresos Carne", "1,012,500", "2,160,000", "5,400,000"),
        ("Total Ingresos", "4,297,500", "5,992,500", "9,780,000"),
        ("Gastos Operativos", "(1,653,050)", "(2,304,575)", "(2,956,100)"),
        ("Utilidad Bruta", "2,644,450", "3,687,925", "6,823,900"),
        ("Reinversión (Compra Ganado)", "(1,500,000)", "(2,000,000)", "0"),
        ("GANANCIA LÍQUIDA", "1,144,450", "1,687,925", "6,823,900"),
        ("Rebaño al final del año", "23", "33", "18")
    ]

    for r in rows:
        row_cells = table.add_row().cells
        row_cells[0].text = r[0]
        row_cells[1].text = r[1]
        row_cells[2].text = r[2]
        row_cells[3].text = r[3]
        
    doc.add_paragraph('\nConclusión del Estudio: El proyecto demuestra una viabilidad financiera total, generando más de 9.6 Millones de CUP de ganancia líquida en 3 años sin requerir nuevos créditos bancarios, lo que garantiza la solvencia del PDL Aquapónica para honrar sus compromisos con el BPA.')

    filename = "2_Convenio_Ganado_Oficial_Anexo.docx"
    doc.save(f"/root/Mi-primer-proyecto/backend/app/static/{filename}")
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

crear_convenio_cana()
crear_convenio_ganado()
