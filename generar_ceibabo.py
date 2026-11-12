import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

# DATOS DEL PROYECTO CEIBABO
INVERSION = {
    "Combustible Retro (2400 L x 1900)": 4560000,
    "Aceite (96 L x 2500)": 240000,
    "Salario Operario (10 días x 5000)": 50000,
    "Alquiler Equipo (30% de la obra)": 1455000
}
TOTAL_INVERSION = sum(INVERSION.values())

# PRODUCCIÓN CONSERVADORA
SIEMBRA = 60000
SUPERVIVENCIA = 0.50
COSECHA_PECES = SIEMBRA * SUPERVIVENCIA
PESO_KG = 1.2
PRODUCCION_KG = COSECHA_PECES * PESO_KG
PRODUCCION_LB = PRODUCCION_KG * 2.20462

PRECIO_LB = 130
INGRESOS_ANUALES = PRODUCCION_LB * PRECIO_LB
OPEX_ANUAL = 4000000
UTILIDAD_NETA = INGRESOS_ANUALES - OPEX_ANUAL

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

# HOJA 1: INVERSION
ws1 = wb.active
ws1.title = "1. Inversión Vivero"
ws1.append(["Concepto", "Monto (CUP)"])
for k, v in INVERSION.items():
    ws1.append([k, v])
ws1.append(["INVERSIÓN TOTAL", TOTAL_INVERSION])
apply_style(ws1)
ws1.column_dimensions['A'].width = 45
ws1.column_dimensions['B'].width = 20

# HOJA 2: PRODUCCION
ws2 = wb.create_sheet("2. Proyección CEM")
ws2.append(["Parámetro", "Valor"])
ws2.append(["Densidad de Siembra (12 ha)", f"{SIEMBRA:,} alevines"])
ws2.append(["Supervivencia (Escenario Pesimista)", f"{SUPERVIVENCIA*100}%"])
ws2.append(["Peces Cosechados", f"{COSECHA_PECES:,.0f} peces"])
ws2.append(["Peso Promedio", f"{PESO_KG} kg"])
ws2.append(["Producción Total (kg)", f"{PRODUCCION_KG:,.2f} kg"])
ws2.append(["Producción Total (libras)", f"{PRODUCCION_LB:,.2f} lbs"])
apply_style(ws2)
ws2.column_dimensions['A'].width = 40
ws2.column_dimensions['B'].width = 25

# HOJA 3: FINANZAS
ws3 = wb.create_sheet("3. Análisis Financiero")
ws3.append(["Concepto", "Monto (CUP)"])
ws3.append(["Precio de Venta (mayorista)", f"{PRECIO_LB} CUP/lb"])
ws3.append(["Ingresos Anuales", INGRESOS_ANUALES])
ws3.append(["Costos Operativos Anuales (OPEX)", OPEX_ANUAL])
ws3.append(["UTILIDAD NETA ANUAL", UTILIDAD_NETA])
ws3.append(["Payback (Años)", round(TOTAL_INVERSION / UTILIDAD_NETA, 2)])
apply_style(ws3)
ws3.column_dimensions['A'].width = 40
ws3.column_dimensions['B'].width = 20
for row in ws3.iter_rows(min_row=2):
    for cell in row[1:]:
        cell.number_format = '#,##0.00'

# HOJA 4: SINERGIA
ws4 = wb.create_sheet("4. Sinergia Ganadera")
ws4.append(["Estrategia de Economía Circular"])
ws4.append(["1. El ganado (ceba/leche) produce estiércol."])
ws4.append(["2. El estiércol se usa para fertilizar las 12 ha del embalse."])
ws4.append(["3. Esto genera plancton natural (comida gratis para los peces)."])
ws4.append(["4. Se reduce el OPEX a solo mantenimiento y nómina."])
apply_style(ws4)
ws4.column_dimensions['A'].width = 65

# GUARDAR
filename = f"Proyecto_Ceibabo_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

# COPIAR A STATIC PARA DESCARGA
os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
