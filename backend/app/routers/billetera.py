from fastapi import APIRouter
from pydantic import BaseModel
import sys
import os
from datetime import datetime

# Conectamos con el archivo contabilidad.py de la raiz
sys.path.append('/root/Mi-primer-proyecto')
from contabilidad import registrar_asiento

router = APIRouter()

class RecargaRequest(BaseModel):
    telegram_id: str
    monto: float

@router.post("/recargar")
async def recargar_billetera(data: RecargaRequest):
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    
    # Llamamos a la contabilidad (Banco e Ingresos)
    resultado = registrar_asiento(
        fecha=fecha_hoy,
        cuenta_debito="110",   # Entra dinero al banco
        cuenta_credito="900",  # Se registra como ingreso
        monto=data.monto,
        descripcion=f"Recarga PWA - User ID: {data.telegram_id}"
    )
    
    return {"status": "ok", "mensaje": resultado}
