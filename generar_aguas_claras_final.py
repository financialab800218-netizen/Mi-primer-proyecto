import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime

# ==========================================
# DATOS DEL MACROPROYECTO AGUAS CLARAS
# ==========================================
CAPEX_TOTAL = 134900000
OPEX_TOTAL = 21200000
INGRESOS_TOTALES = 56200000
UTILIDAD_NETA = 35000000
PAYBACK = 3.8

wb = Workbook()
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
title_font = Font(bold=True, size=14, color="1F4E78")
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

def apply_style(ws):
    for row in ws.iter_rows():
        for cell in row:
            cell.border = border
            if cell.row == 1:
                cell.font = header_font
                cell.fill = header_fill
                cell.alignment = Alignment(horizontal="center")

def format_money(ws, col='B'):
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            if isinstance(cell.value, (int, float)) and not isinstance(cell.value, bool):
                cell.number_format = '#,##0.00'

# ==========================================
# HOJA 1: RESUMEN GLOBAL
# ==========================================
ws1 = wb.active
ws1.title = "1. Resumen Global"
ws1.append(["Macroproyecto Aguas Claras", "Monto (CUP)"])
ws1.append(["Inversión Total (CAPEX)", CAPEX_TOTAL])
ws1.append(["Ingresos Anuales (Agua + Masa)", INGRESOS_TOTALES])
ws1.append(["Costos Operativos (OPEX)", OPEX_TOTAL])
ws1.append(["UTILIDAD NETA ANUAL", UTILIDAD_NETA])
ws1.append(["Payback Global (Años)", PAYBACK])
apply_style(ws1)
format_money(ws1)
ws1.column_dimensions['A'].width = 45
ws1.column_dimensions['B'].width = 20
for row in ws1.iter_rows(min_row=5):
    for cell in row:
        cell.font = Font(bold=True)

# ==========================================
# HOJA 2: NODO INDUSTRIAL
# ==========================================
ws2 = wb.create_sheet("2. Nodo Industrial")
ws2.append(["Concepto", "Monto (CUP)"])
ws2.append(["INVERSIÓN", ""])
ws2.append(["Sistema Solar (25 kWp + 80kWh Baterías)", 25500000])
ws2.append(["Procesadora y Cámara de Frío", 15000000])
ws2.append(["Acondicionamiento Vivero y Pienso", 2000000])
ws2.append(["Total Inversión Nodo", 42500000])
ws2.append(["", ""])
ws2.append(["INGRESOS Y OPERACIÓN", ""])
ws2.append(["Ingreso por Venta de Masa (33,750 kg)", 33700000])
ws2.append(["Costo Compra Pescado al Embalse (Interno)", 19344000])
ws2.append(["Costo Pienso Criollo (Maíz/Soya)", 2250000])
ws2.append(["Mantenimiento Planta y Nómina", 6000000])
ws2.append(["Ganancia Neta Nodo", 6106000])
apply_style(ws2)
format_money(ws2)
ws2.column_dimensions['A'].width = 50
ws2.column_dimensions['B'].width = 20
for row in ws2.iter_rows():
    if "INVERSIÓN" in str(row[0].value) or "INGRESOS" in str(row[0].value) or "Total" in str(row[0].value) or "Ganancia" in str(row[0].value):
        for cell in row:
            cell.font = Font(bold=True)

# ==========================================
# HOJA 3: SISTEMA HIDRÁULICO (AGUA)
# ==========================================
ws3 = wb.create_sheet("3. Sistema de Agua")
ws3.append(["Concepto", "Monto (CUP)"])
ws3.append(["INVERSIÓN", ""])
ws3.append(["Limpieza Canal 14km y Tractor", 10000000])
ws3.append(["Reparación Planchas de Hormigón", 15000000])
ws3.append(["Mini-Hidroeléctrica (Salida Presa)", 4250000])
ws3.append(["Reparación Compuertas y Muro 700m", 11500000])
ws3.append(["Total Inversión Agua", 40750000])
ws3.append(["", ""])
ws3.append(["INGRESOS Y OPERACIÓN", ""])
ws3.append(["Ingreso por Servicio de Agua (1,500 ha)", 22500000])
ws3.append(["Mantenimiento Canal, Nómina y Materiales", 6000000])
ws3.append(["Ganancia Neta Sistema de Agua", 16500000])
apply_style(ws3)
format_money(ws3)
ws3.column_dimensions['A'].width = 50
ws3.column_dimensions['B'].width = 20
for row in ws3.iter_rows():
    if "INVERSIÓN" in str(row[0].value) or "INGRESOS" in str(row[0].value) or "Total" in str(row[0].value) or "Ganancia" in str(row[0].value):
        for cell in row:
            cell.font = Font(bold=True)

# ==========================================
# HOJA 4: EMBALSE Y CEM
# ==========================================
ws4 = wb.create_sheet("4. Embalse y CEM")
ws4.append(["Concepto", "Valor"])
ws4.append(["Área del Embalse", "124.56 ha"])
ws4.append(["Limpieza Perimetral (Buldócer 90 días)", 56700000])
ws4.append(["Siembra de Alevines (Producidos en Nodo)", "150,000 unidades"])
ws4.append(["Supervivencia en Embalse", "75%"])
ws4.append(["Cosecha Esperada", "112,500 peces"])
ws4.append(["Peso Promedio", "1.2 kg"])
ws4.append(["Producción Total", "135,000 kg (297,600 lbs)"])
ws4.append(["Ingreso por Venta Interna (H&G a 65 CUP/lb)", 19344000])
apply_style(ws4)
ws4.column_dimensions['A'].width = 50
ws4.column_dimensions['B'].width = 25
for row in ws4.iter_rows(min_row=3):
    for cell in row[1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '#,##0.00'

# ==========================================
# HOJA 5: MANEJO DE AGUA
# ==========================================
ws5 = wb.create_sheet("5. Manejo de Agua")
ws5.append(["Etapa / Temporada", "Caudal (L/s)", "Equivalencia en Tubería"])
ws5.append(["Máximo (Junio-Septiembre)", 500, "32 pulgadas (80 cm diámetro)"])
ws5.append(["Controlado (Octubre-Diciembre)", 200, "20 pulgadas (50 cm diámetro)"])
ws5.append(["Sequía (Enero-Mayo)", 50, "10 pulgadas (25 cm diámetro)"])
ws5.append(["", "", ""])
ws5.append(["Nota:", "Se mantiene una reserva de 1.5m", "de profundidad para proteger los peces."])
apply_style(ws5)
ws5.column_dimensions['A'].width = 35
ws5.column_dimensions['B'].width = 15
ws5.column_dimensions['C'].width = 35

filename = f"Proyecto_AguasClaras_Final_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
