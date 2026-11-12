import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import os
from datetime import datetime

# ==========================================
# DATOS DE LAS ETAPAS
# ==========================================

# --- FASE 1 (Arranque) ---
CAPEX_F1 = {
    "Centro de Frío (Solar, Camión, Equipos)": 46730000,
    "Marquito (30 ha - Limpieza y CEM)": 31525000,
    "Ceibabo (12 ha - Vivero y CEM)": 6305000
}
INVERSION_F1 = sum(CAPEX_F1.values())

INGRESO_F1_FRIO = 29700 * 1000 # 29,700 kg de masa a 1,000 CUP
GANANCIA_F1_FRIO = 6085000 # Calculado previamente restando costos de compra y proceso
GANANCIA_F1_MARQUITO = 14704080 # Venta de pescado H&G al Centro
GANANCIA_F1_CEIBABO = 5257940 # Venta de pescado H&G al Centro
UTILIDAD_F1 = GANANCIA_F1_FRIO + GANANCIA_F1_MARQUITO + GANANCIA_F1_CEIBABO
PAYBACK_F1 = INVERSION_F1 / UTILIDAD_F1

# --- FASE 2 (Expansión) ---
CAPEX_F2 = {
    "Ganadería (Ceba y Leche)": 26706500,
    "Embalses Restantes (La 16, La 15, Mosquito, Llevadero, Arrosay)": 84361000
}
INVERSION_F2 = sum(CAPEX_F2.values())

# Al sumar más embalses, el Centro de Frío procesa el doble (60,000 kg)
INGRESO_F2_FRIO = 60000 * 1000
GANANCIA_F2_FRIO = 15000000 # Sube por economías de escala
GANANCIA_F2_GANADERIA = 5825000
GANANCIA_F2_OTROS_EMBALSES = 27000000
UTILIDAD_F2 = GANANCIA_F2_FRIO + GANANCIA_F2_GANADERIA + GANANCIA_F2_OTROS_EMBALSES
PAYBACK_F2 = INVERSION_F2 / UTILIDAD_F2

# ==========================================
# CREAR EXCEL
# ==========================================
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

# HOJA 1: FASE 1
ws1 = wb.active
ws1.title = "1. FASE 1 (Arranque)"
ws1.append(["Proyecto / Concepto", "Inversión (CAPEX)", "Ganancia Neta Anual"])
for k, v in CAPEX_F1.items():
    ganancia = GANANCIA_F1_FRIO if "Frío" in k else (GANANCIA_F1_MARQUITO if "Marquito" in k else GANANCIA_F1_CEIBABO)
    ws1.append([k, v, ganancia])
ws1.append(["TOTALES FASE 1", INVERSION_F1, UTILIDAD_F1])
ws1.append(["Payback Fase 1 (Años)", round(PAYBACK_F1, 2), "---"])
apply_style(ws1)
ws1.column_dimensions['A'].width = 50
ws1.column_dimensions['B'].width = 20
ws1.column_dimensions['C'].width = 20
for row in ws1.iter_rows(min_row=2):
    for cell in row[1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '#,##0.00'

# HOJA 2: FASE 2
ws2 = wb.create_sheet("2. FASE 2 (Expansión)")
ws2.append(["Proyecto / Concepto", "Inversión (CAPEX)", "Ganancia Neta Anual"])
for k, v in CAPEX_F2.items():
    ganancia = GANANCIA_F2_GANADERIA if "Ganadería" in k else GANANCIA_F2_OTROS_EMBALSES
    ws2.append([k, v, ganancia])
ws2.append(["TOTALES FASE 2", INVERSION_F2, UTILIDAD_F2])
ws2.append(["Payback Fase 2 (Años)", round(PAYBACK_F2, 2), "---"])
ws2.append([])
ws2.append(["--- IMPACTO TOTAL DEL PDL (FASE 1 + FASE 2) ---", "", ""])
ws2.append(["Inversión Total Acumulada", INVERSION_F1 + INVERSION_F2, ""])
ws2.append(["Ganancia Total Anual (Madurez)", "", UTILIDAD_F1 + UTILIDAD_F2])
apply_style(ws2)
ws2.column_dimensions['A'].width = 55
ws2.column_dimensions['B'].width = 20
ws2.column_dimensions['C'].width = 20
for row in ws2.iter_rows(min_row=2):
    for cell in row[1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '#,##0.00'

# Marcar la fila de totales en negrita
for ws in [ws1, ws2]:
    for row in ws.iter_rows():
        if "TOTALES" in str(row[0].value):
            for cell in row:
                cell.font = Font(bold=True)

filename = f"Proyecto_PDL_Etapas_{datetime.now().strftime('%Y%m%d')}.xlsx"
filepath = f"/tmp/{filename}"
wb.save(filepath)
print(f"✅ Archivo Excel generado: {filepath}")

os.system(f"cp {filepath} /root/Mi-primer-proyecto/backend/app/static/")
print(f"✅ Archivo copiado a la carpeta estática.")
print(f"🔗 Descárgalo aquí: https://lens-portside-masses.ngrok-free.dev/{filename}")
