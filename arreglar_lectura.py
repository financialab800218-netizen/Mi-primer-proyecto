import re

with open('bot_multiagent.py', 'r') as f:
    code = f.read()

# 1. Inyectar la funcion para manejar documentos (antes de crear_app)
funcion_doc = '''
async def handle_document(update, context):
    """Descarga el archivo que envia el usuario y lo guarda en el servidor."""
    doc = update.message.document
    if not doc:
        return
    
    # Validar tamaño (max 15 MB para no llenar el VPS)
    if doc.file_size > 15 * 1024 * 1024:
        await update.message.reply_text("El archivo es demasiado grande. Maximo 15 MB.")
        return

    try:
        file = await context.bot.get_file(doc.file_id)
        nombre_archivo = doc.file_name
        ruta_local = f"/root/Mi-primer-proyecto/backend/app/static/docs/{nombre_archivo}"
        
        # Descargar el archivo
        await file.download_to_drive(ruta_local)
        
        await update.message.reply_text(
            f"✅ Archivo recibido: {nombre_archivo}\\n"
            f"Ya puedes pedirme que lo lea. Por ejemplo: 'Marta, lee el archivo {nombre_archivo}'"
        )
    except Exception as e:
        await update.message.reply_text(f"Error al descargar el archivo: {e}")

'''

if 'async def handle_document' not in code:
    # Lo insertamos antes de la definicion de crear_app
    match = re.search(r'def crear_app\(', code)
    if match:
        code = code[:match.start()] + funcion_doc + code[match.start():]

# 2. Registrar el handler en crear_app
if 'MessageHandler(filters.Document.ALL' not in code:
    target = 'app.add_handler(CallbackQueryHandler'
    if target in code:
        # Necesitamos importar MessageHandler y filters si no estan
        if 'from telegram.ext import filters' not in code:
            code = code.replace('from telegram.ext import', 'from telegram.ext import filters, MessageHandler,', 1)
        
        # Insertar el handler
        code = code.replace(target, 'app.add_handler(MessageHandler(filters.Document.ALL, handle_document))\n    ' + target, 1)

with open('bot_multiagent.py', 'w') as f:
    f.write(code)
print("OK: Manejador de documentos inyectado.")
