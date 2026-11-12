import os
import subprocess
from contabilidad import supabase

def check_status(service_name):
    try:
        res = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
        return "✅ ACTIVO" if res.stdout.strip() == "active" else "❌ CAÍDO"
    except:
        return "❌ ERROR"

print("🩺 INICIANDO AUDITORÍA GENERAL DE TUTORIA CUBA...\n")

# 1. Verificar Servicios
print("--- 1. ESTADO DE LOS SERVICIOS EN LA VPS ---")
print(f"Bot de Telegram (tutoria-bot.service): {check_status('tutoria-bot.service')}")
print(f"Servidor Web (tutoria-backend.service): {check_status('tutoria-backend.service')}\n")

# 2. Verificar Base de Datos (Contabilidad)
print("--- 2. ESTADO DE LA BASE DE DATOS (SUPABASE) ---")
try:
    # Revisamos la contabilidad
    res_asientos = supabase.table('asientos_contables').select('id', count='exact').execute()
    print(f"Contabilidad: ✅ {res_asientos.count} asientos registrados en total.")
    
    # Revisamos el balance del banco
    from reporte_contable import obtener_balance_general
    balance = obtener_balance_general()
    if "BALANCE" in balance:
        print("Reporte de Balance: ✅ Se genera correctamente.")
    else:
        print("Reporte de Balance: ⚠️ Puede tener errores de formato.")
        
    # Revisamos los profesores
    res_profes = supabase.table('profesores').select('id', count='exact').execute()
    print(f"Tabla Profesores: ✅ {res_profes.count} profesores registrados.")

except Exception as e:
    print(f"❌ Error en Base de Datos: {e}")

print("\n--- 3. VERIFICACIÓN DE ARCHIVOS WEB (PWA) ---")
rutas = [
    '/root/Mi-primer-proyecto/backend/app/static/login.html',
    '/root/Mi-primer-proyecto/backend/app/static/index.html',
    '/root/Mi-primer-proyecto/backend/app/static/recarga.html'
]
for ruta in rutas:
    if os.path.exists(ruta):
        print(f"✅ Archivo encontrado: {os.path.basename(ruta)}")
    else:
        print(f"❌ Falta el archivo: {os.path.basename(ruta)}")

print("\n✅ Auditoría finalizada.")
