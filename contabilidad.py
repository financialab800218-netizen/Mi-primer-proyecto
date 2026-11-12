from supabase import create_client, Client
import os

# ⚠️ AQUÍ ESTÁ LA MAGIA: Las llaves puestas directamente para que no fallen
SUPABASE_URL = "https://ktdpxyqpghipmsftepgl.supabase.co"
# Usamos la llave secreta (service_role) para que Python pueda hacer todo
# (Como es un script interno en tu VPS, es seguro usarla aquí)

# Creamos el cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def registrar_asiento(fecha, cuenta_debito, cuenta_credito, monto, descripcion):
    # Función de ejemplo para mantener la compatibilidad con los otros scripts
    try:
        data = [
            {"fecha": fecha, "cuenta_debito": cuenta_debito, "cuenta_credito": None, "monto": monto, "descripcion": descripcion},
            {"fecha": fecha, "cuenta_debito": None, "cuenta_credito": cuenta_credito, "monto": monto, "descripcion": descripcion}
        ]
        supabase.table('asientos_contables').insert(data).execute()
        return True
    except Exception as e:
        return str(e)

print("✅ Módulo de contabilidad cargado correctamente.")
