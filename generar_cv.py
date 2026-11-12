from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

def crear_cv():
    doc = Document()

    # Configurar márgenes (1 pulgada)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Estilo de fuente global
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(10.5)

    # --- ENCABEZADO ---
    titulo = doc.add_paragraph()
    run = titulo.add_run('YUDELVIS ROJAS VIERA')
    run.bold = True
    run.font.size = Pt(18)
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    subtitulo = doc.add_paragraph()
    run_sub = subtitulo.add_run('Operador y Mecánico de Equipo Pesado | Líder de Brigada')
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = None # Color negro por defecto
    subtitulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

    contacto = doc.add_paragraph()
    contacto.alignment = WD_ALIGN_PARAGRAPH.CENTER
    contacto.add_run('📍 Quinta Umpa Beach, Villa Elisa, Paraguay | 📞 +595 976 644 288\n')
    contacto.add_run('🪪 Nacionalidad: Cubana | Pasaporte vigente (CUB) | 🚜 Licencia Clase C vigente')
    
    doc.add_paragraph('_' * 80) # Línea separadora

    # --- RESUMEN PROFESIONAL ---
    doc.add_heading('RESUMEN PROFESIONAL', level=1)
    resumen = doc.add_paragraph(
        "Operador-mecánico de equipo pesado con más de 20 años de experiencia en proyectos agrícolas, "
        "de construcción y recuperación de caminos. Recientemente radicado en Paraguay, con toda la "
        "documentación en regla y Licencia Clase C vigente para operar de inmediato.\n\n"
        "Fundador y líder de la Mipyme Tierra Roja en Cuba (2020 - 2026), donde dirigí una brigada con "
        "flota propia de 6 equipos. Perfil híbrido poco común: operador experto y mecánico capaz de "
        "mantener la flota funcionando de forma autónoma, reduciendo tiempos muertos por averías y "
        "dependencia de talleres externos."
    )

    # --- EXPERIENCIA LABORAL ---
    doc.add_heading('EXPERIENCIA LABORAL', level=1)
    
    p = doc.add_paragraph()
    p.add_run('Fundador, Líder de Brigada y Operador-Mecánico\n').bold = True
    p.add_run('Mipyme Tierra Roja — Cuba | 2020 – 2026').italic = True
    
    viñetas = [
        "Fundé y dirigí una brigada de equipos pesados con flota propia: 1 cargador frontal, 1 retroexcavadora, 1 equipo multipropósito, 1 motoniveladora, 1 cilindro compactador y 2 camiones de volteo.",
        "Operé directamente los equipos en servicios de reparación y recuperación de caminos, preparación de obras y recogida de desechos sólidos.",
        "Ejecuté mantenimiento preventivo y correctivo integral de toda la flota: diagnóstico de fallas, reparación de sistemas hidráulicos, reconstrucción de componentes mecánicos y motores.",
        "Reduje tiempos muertos por averías al realizar reparaciones en sitio, manteniendo la continuidad operativa de los proyectos.",
        "Planifiqué y supervisé tareas del personal, coordinando la asignación de equipos, rutas de trabajo y cumplimiento de plazos.",
        "Gestioné clientes y proyectos de principio a fin: presupuestos, coordinación logística y entrega de obras."
    ]
    for v in viñetas:
        doc.add_paragraph(v, style='List Bullet')

    p2 = doc.add_paragraph()
    p2.add_run('\nExperiencia específica como Operador de Equipo Pesado\n').bold = True
    p2.add_run('Cuba | 2000 – 2020').italic = True

    viñetas2 = [
        "Operador de Equipo Pesado Agrícola (5 años): Operación de tractores y maquinaria agrícola.",
        "Operador de Cargador Frontal (4 años): Movimiento de suelos, carga de materiales, nivelación.",
        "Operador de Retroexcavadora (3 años): Excavación, zanjeo, demolición y trabajos de infraestructura.",
        "Operador de Equipo Multipropósito (4 años): Operación combinada para obras viales y de construcción.",
        "Operador de Motoniveladora y Cilindro Compactador: Nivelación de caminos y compactación de suelos."
    ]
    for v in viñetas2:
        doc.add_paragraph(v, style='List Bullet')

    # --- HABILIDADES TÉCNICAS ---
    doc.add_heading('HABILIDADES TÉCNICAS', level=1)
    
    doc.add_paragraph('Operación de maquinaria:', style='List Bullet').runs[0].bold = True
    doc.add_paragraph('Cargador frontal, Retroexcavadora, Equipo multipropósito, Motoniveladora, Cilindro compactador, Tractor agrícola, Camión de volteo.', style='List Bullet 2')
    
    doc.add_paragraph('Mecánica y mantenimiento:', style='List Bullet').runs[0].bold = True
    doc.add_paragraph('Diagnóstico y reparación de sistemas hidráulicos, Reconstrucción de motores, Mantenimiento de flota, Reparaciones en sitio.', style='List Bullet 2')
    
    doc.add_paragraph('Gestión y liderazgo:', style='List Bullet').runs[0].bold = True
    doc.add_paragraph('Dirección de brigada, Planificación de tareas, Gestión de clientes y presupuestos.', style='List Bullet 2')

    # --- COMPETENCIAS PERSONALES ---
    doc.add_heading('COMPETENCIAS PERSONALES', level=1)
    doc.add_paragraph('Autonomía y resolución de problemas, Liderazgo, Compromiso con la seguridad, Adaptabilidad. Documentación en regla y disponibilidad inmediata.')

    # --- IDIOMAS ---
    doc.add_heading('IDIOMAS', level=1)
    doc.add_paragraph('Español: Nativo')

    # Guardar
    os.makedirs('/root/Mi-primer-proyecto/backend/app/static/docs', exist_ok=True)
    ruta = '/root/Mi-primer-proyecto/backend/app/static/docs/CV_Yudelvis_Rojas.docx'
    doc.save(ruta)
    print("CV generado con éxito en:", ruta)

crear_cv()
