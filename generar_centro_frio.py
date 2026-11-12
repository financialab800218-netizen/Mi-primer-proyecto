import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime

# ==========================================
# DATOS COMPLETOS DEL CENTRO DE FRÍO Y PROCESAMIENTO
# ==========================================
CAPEX = {
    "Inversor Híbrido 10kW Baja Frecuencia": 2550000,
    "Baterías de Litio (60 kWh)": 10200000,
    "Paneles Solares (15 kWp) + Estructura": 5100000,
    "Cableado y Protecciones Eléctricas": 1275000,
    "Acondicionamiento Plazoleta y Anclaje": 2125000,
    "Mano de Obra Instalación Solar": 1000000,
    "Redes de Pesca y Neveras Isotérmicas": 2550000,
    "Máquina de Hielo (1 Ton/día)": 3400000,
    "Mesas Inox, Empacadora al Vacío y Utensilios": 2975000,
    "Camión Isotérmico de Transporte": 15300000
}
TOTAL_CAPEX = sum(CAPEX.values())

# Variables de Producción
KG_MASA_ANUAL = 100000
COSTO_HG_KG = 260 
RENDIMIENTO_MASA = 0.45 
COSTO_MP_MASA = (1 / RENDIMIENTO_MASA) * COSTO_HG_KG 
COSTO_PROCESO_MASA = 150 
COSTO_TOTAL_MASA = COSTO_MP_MASA + COSTO_PROCESO_MASA 

# Ingresos y Utilidad
PRECIO_VENTA_MASA = 1000 
INGRESOS_ANUALES = KG_MASA_ANUAL * PRECIO_VENTA_MASA
COSTO_ANUAL_MP = KG_MASA_ANUAL * COSTO_MP_MASA
COSTO_ANUAL_PROCESO = KG_MASA_ANUAL * COSTO_PROCESO_MASA

# Gastos operativos del camión y mantenimiento general
OPEX_ADICIONAL = 2000000 # Diésel, mantenimiento camión, hielo, etc.

UTILIDAD_NETA_ANUAL = INGRESOS_ANUALES - (COSTO_ANUAL_MP + COSTO_ANUAL_PROCESO + OPEX_ADICIONAL)
PAYBACK = TOTAL_CAPEX / UTILIDAD_NETA_ANUAL

wb = Workbook()
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

def apply_style(ws):
    for row in ws.iter_rows():
        for cell in row:
            cell.border = border
            if cell.row == 1:
                cell.font = header_font
                cell.fill = header_fill
                cell.alignment = Alignment(horizontal="center")

ws1 = wb.active
ws1.title = "1. Inversión (CAPEX)"
ws1.append(["Concepto", "Monto (CUP)"])
for k, v in CAPEX.items():
    ws1.append([k, v])
ws1.append(["INVERSIÓN TOTAL", TOTAL_CAPEX])
apply_style(ws1)
ws1.column_dimensions['A'].width = 55
ws1.column_dimensions['B'].width = 20

ws2 = wb.create_sheet("2. Costos de Proceso")
ws2.append(["Concepto", "Valor"])
ws2.append(["Precio H&G (sin cabeza/vísceras)", f"{COSTO_HG_KG} CUP/kg"])
ws2.append(["Rendimiento a Masa", f"{RENDIMIENTO_MASA*100}%"])
ws2.append(["Costo MP para 1kg de Masa", f"{COSTO_MP_MASA:.2f} CUP"])
ws2.append(["Costo de Proceso (Mano obra, empaque)", f"{COSTO_PROCESO_MASA:.2f} CUP"])
ws2.append(["COSTO TOTAL POR KG DE MASA", f"{COSTO_TOTAL_MASA:.2f} CUP"])
apply_style(ws2)
ws2.column_dimensions['A'].width = 50
ws2.column_dimensions['B'].width = 25

ws3 = wb.create_sheet("3. Análisis Financiero")
ws3.append(["Concepto", "Monto (CUP)"])
ws3.append(["Producción Anual Estimada", f"{KG_MASA_ANUAL:,} kg de masa"])
ws3.append(["Precio de Venta Promedio", f"{PRECIO_VENTA_MASA} CUP/kg"])
ws3.append(["Ingresos Anuales Totales", INGRESOS_ANUALES])
ws3.append(["Costo Anual de Materia Prima (H&G)", COSTO_ANUAL_MP])
ws3.append(["Costo Anual de Procesamiento", COSTO_ANUAL_PROCESO])
ws3.append(["Gastos Operativos Camión/Mantenimiento", OPEX_ADICIONAL])
ws3.append(["UTILIDAD NETA ANUAL", UTILIDAD_NETA_ANUAL])
ws3.append(["Payback (Años)", round(PAYBACK, 2)])
apply_style(ws3)
ws3.column_dimensions['A'].width = 45
ws3.column_dimensions['B'].width = 20
for row in ws3.iter_rows(min_row=2):
    for cell in row[1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '#,##0.00'

filename = f"Proyecto_Centro_Frio_Integral_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
