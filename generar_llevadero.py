import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime

# DATOS DEL PROYECTO EL LLEVADERO (Corregido)
CAPEX = {
    "Limpieza con Buldócer (30 días)": 18915000,
    "Excavación y Tapado Muro (Retro 3 días)": 1891500,
    "Materiales (Tubo 15\", Válvula, Cemento)": 2500000,
    "Mano de Obra Especializada (Cirugía)": 180000
}
TOTAL_CAPEX = sum(CAPEX.values())

# PRODUCCIÓN (8 ha)
SIEMBRA = 40000
SUPERVIVENCIA = 0.50
PRODUCCION_KG = (SIEMBRA * SUPERVIVENCIA) * 1.2
PRODUCCION_LB = PRODUCCION_KG * 2.20462
PRECIO_LB = 130
INGRESOS = PRODUCCION_LB * PRECIO_LB

# OPEX
OPEX = {
    "Fertilizante (Estiércol)": 800000,
    "Alevines (40,000)": 400000,
    "Personal y Seguridad": 1500000,
    "Mantenimiento": 500000
}
TOTAL_OPEX = sum(OPEX.values())

UTILIDAD = INGRESOS - TOTAL_OPEX
PAYBACK = TOTAL_CAPEX / UTILIDAD

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

ws2 = wb.create_sheet("2. Proyección CEM")
ws2.append(["Parámetro", "Valor"])
ws2.append(["Área del Embalse", "8 ha"])
ws2.append(["Siembra", f"{SIEMBRA:,} alevines"])
ws2.append(["Supervivencia", f"{SUPERVIVENCIA*100}%"])
ws2.append(["Producción Total (kg)", f"{PRODUCCION_KG:,.2f} kg"])
ws2.append(["Producción Total (libras)", f"{PRODUCCION_LB:,.2f} lbs"])
apply_style(ws2)
ws2.column_dimensions['A'].width = 40
ws2.column_dimensions['B'].width = 25

ws3 = wb.create_sheet("3. Análisis Financiero")
ws3.append(["Concepto", "Monto (CUP)"])
ws3.append(["Precio de Venta", f"{PRECIO_LB} CUP/lb"])
ws3.append(["Ingresos Anuales", INGRESOS])
ws3.append(["Costos Operativos (OPEX)", TOTAL_OPEX])
ws3.append(["UTILIDAD NETA ANUAL", UTILIDAD])
ws3.append(["Payback (Años)", round(PAYBACK, 2)])
apply_style(ws3)
ws3.column_dimensions['A'].width = 40
ws3.column_dimensions['B'].width = 20
for row in ws3.iter_rows(min_row=2):
    for cell in row[1:]:
        cell.number_format = '#,##0.00'

filename = f"Proyecto_Llevadero_Corregido_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
