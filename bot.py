#!/usr/bin/env python3
import os
import time
import logging
import httpx
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

load_dotenv('/data/data/com.termux/files/home/tutoria-cuba/backend/app/.env')

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DEEPSEEK_KEY = os.getenv('DEEPSEEK_API_KEY', '')
DEEPSEEK_URL = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

def tiene_deepseek():
    return DEEPSEEK_KEY and DEEPSEEK_KEY != 'tu_api_key_aqui' and len(DEEPSEEK_KEY) > 20

async def consultar_deepseek(mensaje, sistema=None):
    if not tiene_deepseek():
        return None
    try:
        headers = {
            'Authorization': f'Bearer {DEEPSEEK_KEY}',
            'Content-Type': 'application/json'
        }
        messages = []
        if sistema:
            messages.append({'role': 'system', 'content': sistema})
        messages.append({'role': 'user', 'content': mensaje})
        payload = {
            'model': 'deepseek-chat',
            'messages': messages,
            'max_tokens': 800,
            'temperature': 0.7
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(f'{DEEPSEEK_URL}/chat/completions', headers=headers, json=payload)
            if r.status_code == 200:
                data = r.json()
                return data['choices'][0]['message']['content']
            else:
                return f'[Error DeepSeek {r.status_code}]'
    except Exception as e:
        return f'[Error conexion: {str(e)[:80]}]'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ia_estado = 'ACTIVA' if tiene_deepseek() else 'PENDIENTE (falta fondear)'
    await update.message.reply_text(
        "Hola Yosbel. Soy el asistente de TutorIA Cuba.\n\n"
        f"IA DeepSeek: {ia_estado}\n\n"
        "Comandos:\n"
        "/start /status /maestro /ia /ayuda\n\n"
        "Escribeme cualquier mensaje y te respondo."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ia = 'ACTIVA' if tiene_deepseek() else 'PENDIENTE (falta fondear $5)'
    await update.message.reply_text(
        "ESTADO DEL SISTEMA\n\n"
        "Bot Telegram: ACTIVO\n"
        f"DeepSeek IA: {ia}\n"
        "Supabase: CONECTADO\n"
        "GitHub: ACTIVO\n"
        "Tmux: ACTIVO\n"
        "Wakelock: ACTIVO\n\n"
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

async def ia_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if tiene_deepseek():
        await update.message.reply_text(
            "IA DEEPSEEK: ACTIVA\n\n"
            "Prueba enviando: /chat hola que puedes hacer"
        )
    else:
        await update.message.reply_text(
            "IA DEEPSEEK: PENDIENTE\n\n"
            "Para activarla:\n"
            "1. Fondear $5 en platform.deepseek.com\n"
            "2. Generar API Key\n"
            "3. Actualizar DEEPSEEK_API_KEY en .env\n"
            "4. Reiniciar el bot\n\n"
            "Mientras tanto, uso modo placeholder."
        )
async def chat_deepseek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not tiene_deepseek():
        await update.message.reply_text("IA no activa. Fondear DeepSeek primero con /ia")
        return
    if not context.args:
        await update.message.reply_text("Uso: /chat tu pregunta")
        return
    mensaje = ' '.join(context.args)
    await update.message.reply_text("Pensando...")
    sistema = "Eres el asistente de Yosbel Collazo. Responde breve y util."
    respuesta = await consultar_deepseek(mensaje, sistema)
    await update.message.reply_text(respuesta or "[Sin respuesta]")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AYUDA\n\n/start /status /maestro /ia /ayuda\n/chat tu pregunta"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    if tiene_deepseek():
        sistema = "Eres el asistente de Yosbel Collazo. Responde breve y util."
        respuesta = await consultar_deepseek(mensaje, sistema)
        await update.message.reply_text(respuesta or "[Sin respuesta de IA]")
    else:
        await update.message.reply_text(
            f"Recibi: {mensaje}\n\n(IA pendiente: fondear DeepSeek $5)\nPrueba /ia."
        )

def crear_app():
    request = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0
    )
    app = (
        Application.builder()
        .token(TOKEN)
        .request(request)
        .get_updates_request(request)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("maestro", maestro))
    app.add_handler(CommandHandler("ia", ia_status))
    app.add_handler(CommandHandler("chat", chat_deepseek))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    return app

def main():
    if not TOKEN:
        print("ERROR: falta TELEGRAM_BOT_TOKEN")
        return
    print("Bot iniciado (modo resiliente)")
    print(f"Token: {TOKEN[:15]}...")
    print(f"DeepSeek: {'ACTIVO' if tiene_deepseek() else 'PENDIENTE'}")
    while True:
        try:
            print("Conectando con Telegram...")
            app = crear_app()
            print("Escuchando mensajes...")
            app.run_polling(drop_pending_updates=True, close_loop=False)
        except KeyboardInterrupt:
            print("Detenido manualmente")
            break
        except Exception as e:
            print(f"Error: {str(e)[:100]}")
            print("Reintentando en 10 segundos...")
            time.sleep(10)

if __name__ == '__main__':
    main()
