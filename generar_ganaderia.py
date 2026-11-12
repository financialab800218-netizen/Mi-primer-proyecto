import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime

# DATOS DEL PROYECTO (Ganadería)
CAPEX = {
    "Construcción Establo (Materiales)": 9780000,
    "Mano de Obra (Construcción)": 1926500,
    "Compra de 27 Toros (250kg a 1500 CUP/kg)": 10125000,
    "Compra de 10 Vacas Lecheras (Est.)": 5000000
}
TOTAL_CAPEX = sum(CAPEX.values())

CEBA_CANT = 27
CEBA_PESO_FINAL = 450 
PRECIO_VENTA_KG = 700
INGRESO_CEBA = CEBA_CANT * CEBA_PESO_FINAL * PRECIO_VENTA_KG

VACAS_LECHE = 10
LITROS_DIA = 8
LITROS_ANUAL = VACAS_LECHE * LITROS_DIA * 365
PRECIO_LECHE = 150
INGRESO_LECHE = LITROS_ANUAL * PRECIO_LECHE

INGRESOS_TOTALES = INGRESO_CEBA + INGRESO_LECHE

OPEX = {
    "Alimento/Pienso y Pastos": 3500000,
    "Salarios (3 Obreros + 1 Veterinario)": 1800000,
    "Mantenimiento, Combustible y Sanidad": 1200000
}
TOTAL_OPEX = sum(OPEX.values())

UTILIDAD_NETA = INGRESOS_TOTALES - TOTAL_OPEX
PAYBACK = TOTAL_CAPEX / UTILIDAD_NETA

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
ws1.column_dimensions['A'].width = 50
ws1.column_dimensions['B'].width = 20

ws2 = wb.create_sheet("2. Proyección Producción")
ws2.append(["Concepto", "Valor"])
ws2.append(["Toros para Ceba", CEBA_CANT])
ws2.append(["Peso Final Promedio (kg)", CEBA_PESO_FINAL])
ws2.append(["Precio Venta Carne (CUP/kg)", PRECIO_VENTA_KG])
ws2.append(["Ingreso Anual Ceba", INGRESO_CEBA])
ws2.append(["Vacas Lecheras", VACAS_LECHE])
ws2.append(["Producción Diaria Leche (L)", VACAS_LECHE * LITROS_DIA])
ws2.append(["Producción Anual Leche (L)", LITROS_ANUAL])
ws2.append(["Precio Venta Leche (CUP/L)", PRECIO_LECHE])
ws2.append(["Ingreso Anual Leche", INGRESO_LECHE])
apply_style(ws2)
ws2.column_dimensions['A'].width = 40
ws2.column_dimensions['B'].width = 25
for row in ws2.iter_rows(min_row=2):
    for cell in row[1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '#,##0.00'

ws3 = wb.create_sheet("3. Análisis Financiero")
ws3.append(["Concepto", "Monto (CUP)"])
ws3.append(["INGRESOS TOTALES (Carne + Leche)", INGRESOS_TOTALES])
ws3.append(["Costos Operativos (OPEX)", TOTAL_OPEX])
ws3.append(["UTILIDAD NETA ANUAL", UTILIDAD_NETA])
ws3.append(["Payback (Años)", round(PAYBACK, 2)])
apply_style(ws3)
ws3.column_dimensions['A'].width = 45
ws3.column_dimensions['B'].width = 20
for row in ws3.iter_rows(min_row=2):
    for cell in row[1:]:
        cell.number_format = '#,##0.00'

filename = f"Proyecto_Ganaderia_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
