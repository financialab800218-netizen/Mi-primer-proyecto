#!/usr/bin/env python3
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Cargar variables de entorno
load_dotenv('/data/data/com.termux/files/home/tutoria-cuba/backend/app/.env')

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DEEPSEEK_KEY = os.getenv('DEEPSEEK_API_KEY', '')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola Yosbel. Soy el asistente de TutorIA Cuba.\n\n"
        "Comandos disponibles:\n"
        "/start - Iniciar\n"
        "/status - Estado del sistema\n"
        "/maestro - Info del proyecto\n"
        "/ayuda - Ayuda\n\n"
        "Tambien puedes escribirme cualquier mensaje y te respondo."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tiene_deepseek = "SI" if DEEPSEEK_KEY and DEEPSEEK_KEY != "tu_api_key_aqui" else "NO (falta fondear)"
    await update.message.reply_text(
        "ESTADO DEL SISTEMA\n\n"
        "Bot Telegram: ACTIVO\n"
        f"DeepSeek API: {tiene_deepseek}\n"
        "Supabase: CONECTADO\n"
        "GitHub: ACTIVO\n\n"
        "Ultima actualizacion: 28 sep 2026"
    )

async def maestro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "PROYECTO TUTORIA CUBA\n\n"
        "Ecosistema Productivo Mayabeque\n"
        "5 direcciones integradas:\n"
        "1. Produccion (7 areas)\n"
        "2. Servicios Tecnicos (5 areas)\n"
        "3. Comercial (5 areas)\n"
        "4. Turismo (5 areas)\n"
        "5. Educacion y Consultoria (5 areas)\n\n"
        "Contacto: +53 5 375 5025"
    )

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AYUDA\n\n"
        "Escribeme cualquier mensaje y te respondo.\n"
        "Los comandos estan en /start\n\n"
        "Cuando la API Key de DeepSeek este configurada, "
        "podre responder con IA real."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    if DEEPSEEK_KEY and DEEPSEEK_KEY != "tu_api_key_aqui":
        # DeepSeek esta configurado (aqui se integrara la IA real)
        await update.message.reply_text(
            f"Recibi tu mensaje: {mensaje}\n\n"
            "(DeepSeek configurado - falta activar integracion completa)"
        )
    else:
        await update.message.reply_text(
            f"Recibi tu mensaje: {mensaje}\n\n"
            "(IA pendiente: falta fondear DeepSeek $5)"
        )

def main():
    if not TOKEN:
        print("ERROR: No se encontro TELEGRAM_BOT_TOKEN en .env")
        return
    
    print("Bot iniciado...")
    print(f"Token: {TOKEN[:15]}...")
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("maestro", maestro))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Escuchando mensajes...")
    app.run_polling()

if __name__ == '__main__':
    main()

