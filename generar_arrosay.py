import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

CAPEX = {
    "Ranchón Rústico": 1000000,
    "Cabañas (5 x 400k)": 2000000,
    "Camino y Plazoleta": 2000000,
    "Equipamiento Cabañas": 6162500,
    "Equipamiento Restaurante": 2890000,
    "Pasarela (50m)": 6375000,
    "Lanchas de remo (4)": 2040000,
    "Sistema Fotovoltaico 12kW": 10200000,
    "Letrero, Paisajismo, Muelle": 4590000,
    "Sistema Bombeo/Séptico": 4250000,
    "Recepción y Planta Respaldo": 3910000,
    "Triciclo Eléctrico": 1700000
}
TOTAL_CAPEX = sum(CAPEX.values())
IMPREVISTOS = TOTAL_CAPEX * 0.10
INVERSION_TOTAL = TOTAL_CAPEX + IMPREVISTOS

NOMINA = 690000
ALIMENTOS = 1584000
BEBIDAS = 675000
GASTOS_GENERALES = 250000
RESERVA = (NOMINA + ALIMENTOS + BEBIDAS + GASTOS_GENERALES) * 0.10
TOTAL_OPEX_MENSUAL = NOMINA + ALIMENTOS + BEBIDAS + GASTOS_GENERALES + RESERVA
INGRESOS_MENSUALES = 6030000
UTILIDAD_NETA_MENSUAL = INGRESOS_MENSUALES - TOTAL_OPEX_MENSUAL

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
ws1.append(["TOTAL OBRAS Y EQUIPOS", TOTAL_CAPEX])
ws1.append(["Imprevistos (10%)", IMPREVISTOS])
ws1.append(["INVERSIÓN TOTAL", INVERSION_TOTAL])
apply_style(ws1)
ws1.column_dimensions['A'].width = 40

ws2 = wb.create_sheet("2. Costos (OPEX)")
ws2.append(["Concepto", "Monto Mensual (CUP)"])
ws2.append(["Nómina (23 trabajadores)", NOMINA])
ws2.append(["Alimentos (22 pax/día)", ALIMENTOS])
ws2.append(["Bebidas (45% ventas)", BEBIDAS])
ws2.append(["Gastos Generales / Mantenimiento", GASTOS_GENERALES])
ws2.append(["Reserva de Contingencia (10%)", RESERVA])
ws2.append(["TOTAL OPEX MENSUAL", TOTAL_OPEX_MENSUAL])
apply_style(ws2)
ws2.column_dimensions['A'].width = 40

ws3 = wb.create_sheet("3. Flujo de Caja 10 Años")
headers = ["Año", "Ingresos Anuales", "Costos Anuales", "Utilidad Bruta", "Pago Crédito (Est.)", "Flujo Neto", "Flujo Acumulado"]
ws3.append(headers)

flujo_acumulado = -INVERSION_TOTAL
for año in range(1, 11):
    ingresos = INGRESOS_MENSUALES * 12 * (1.03 ** (año - 1))
    costos = TOTAL_OPEX_MENSUAL * 12 * (1.05 ** (año - 1))
    utilidad = ingresos - costos
    pago_credito = 0 if año <= 2 else 6000000
    flujo_neto = utilidad - pago_credito
    flujo_acumulado += flujo_neto
    ws3.append([f"Año {año}", ingresos, costos, utilidad, pago_credito, flujo_neto, flujo_acumulado])

apply_style(ws3)
for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    ws3.column_dimensions[col].width = 18
for row in ws3.iter_rows(min_row=2):
    for cell in row[1:]:
        cell.number_format = '#,##0.00'

ws4 = wb.create_sheet("4. Indicadores")
ws4.append(["Indicador", "Valor"])
ws4.append(["Inversión Total", INVERSION_TOTAL])
ws4.append(["Payback Simple (Años)", round(INVERSION_TOTAL / (UTILIDAD_NETA_MENSUAL * 12), 2)])
ws4.append(["Utilidad Neta Mensual", UTILIDAD_NETA_MENSUAL])
ws4.append(["Utilidad Neta Anual (Año 1)", UTILIDAD_NETA_MENSUAL * 12])
apply_style(ws4)
ws4.column_dimensions['A'].width = 30

filename = f"Proyecto_Arrosay_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado localmente: {filepath}")

try:
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    with open(filepath, 'rb') as f:
        supabase.storage.from_("Documentos").upload(
            path=filename,
            file=f,
            file_options={"content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}
        )
    url = supabase.storage.from_("Documentos").get_public_url(filename)
    print(f"🚀 ARCHIVO SUBIDO A SUPABASE EXITOSAMENTE.")
    print(f"🔗 Enlace de descarga: {url}")
except Exception as e:
    print(f"❌ Error al subir a Supabase: {e}")
    print("El archivo quedó guardado localmente en /tmp/")
