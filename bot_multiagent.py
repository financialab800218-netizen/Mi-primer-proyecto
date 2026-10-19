import os
from dotenv import load_dotenv
load_dotenv("/root/Mi-primer-proyecto/.env")

"""
bot_multiagent.py - Bot Telegram Multi-Agente
Ecosistema Mayabeque + TutorIA Cuba
Autor: Yosbel Collazo Avila + Socio IA
Fecha: 30/sept/2026
Version: 1.0
"""

import os
import time
import logging
import httpx
from dotenv import load_dotenv

from telegram import Update
import supabase_helper as sb
from onboarding import (
    menu_agentes_inline,
    es_usuario_nuevo, registrar_usuario, enviar_bienvenida,
    handle_onboarding_callback, marcar_completado,
)
from video_handler import enviar_respuesta_inteligente, handle_video_callback
from telegram.ext import (
    CallbackQueryHandler,
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from agents import COMANDOS, get_agent_by_command, get_agent_info, listar_agentes
from llm_client import consultar_llm, tiene_llm, info_proveedor
from llm_router import consultar_llm_router


# Cargar .env (ruta absoluta)
ENV_PATH = "/root/Mi-primer-proyecto/backend/app/.env"
load_dotenv(ENV_PATH)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Estado: {user_id: "ernesto"}
from estado import user_agents


def tiene_llm():
    return DEEPSEEK_KEY and DEEPSEEK_KEY != "tu_api_key_aqui" and len(DEEPSEEK_KEY) > 20


async def consultar_llm(system_prompt, mensaje):
    if not tiene_llm():
        return None
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": mensaje},
            ],
            "max_tokens": 800,
            "temperature": 0.7,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(
                f"{DEEPSEEK_URL}/chat/completions",
                headers=headers,
                json=payload,
            )
            if r.status_code == 200:
                data = r.json()
                return data["choices"][0]["message"]["content"]
            else:
                return f"[Error DeepSeek {r.status_code}]"
    except Exception as e:
        return f"[Error conexion: {str(e)[:80]}]"


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    user_agents[user_id] = "pablo"

    if es_usuario_nuevo(user_id):
        registrar_usuario(user_id, user.first_name or "amigo", user.username)
        await enviar_bienvenida(update)
        return

    estado_ia = "ACTIVA" if tiene_llm() else "PENDIENTE"
    nombre = user.first_name or "amigo"
    lineas = [
        "Hola " + nombre + ". Bienvenido al Ecosistema Mayabeque.",
        "",
        "IA: " + estado_ia,
        "",
        "Soy Pablo, Director Adjunto.",
        "Agentes disponibles:",
    ]
    for key, agente in listar_agentes():
        lineas.append("  /" + key + " - " + agente["cargo"])
    lineas.extend([
        "",
        "Otros comandos:",
        "  /ayuda  - Ver esta lista",
        "  /quien  - Con quien hablo",
        "  /salir  - Volver a Pablo",
    ])
    await update.message.reply_text(chr(10).join(lineas), reply_markup=menu_agentes_inline())

async def cmd_ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, context)


async def cmd_quien(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    agente_key = user_agents.get(user_id, "pablo")
    agente = get_agent_info(agente_key)
    await update.message.reply_text(
        f"Estas hablando con {agente['nombre']}\n"
        f"{agente['cargo']}\n\n{agente['descripcion']}"
    )


async def cmd_salir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_agents[user_id] = "pablo"
    await update.message.reply_text("Volviste con Pablo, Director Adjunto.")


def crear_handler_agente(agente_key):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        user_agents[user_id] = agente_key
        agente = get_agent_info(agente_key)
        await update.message.reply_text(
            f"Ahora hablas con {agente['nombre']}\n"
            f"{agente['cargo']}\n\n{agente['descripcion']}\n\n"
            "En que te puedo ayudar?"
        )
    return handler


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    mensaje = update.message.text

    agente_key = get_agent_by_command(mensaje)
    if agente_key:
        user_agents[user_id] = agente_key
        agente = get_agent_info(agente_key)
        await update.message.reply_text(
            f"Ahora hablas con {agente['nombre']} ({agente['cargo']})"
        )
        return

    agente_key = user_agents.get(user_id, "pablo")
    agente = get_agent_info(agente_key)

    await update.message.chat.send_action(action="typing")

    if tiene_llm():
        respuesta = await consultar_llm_router(agente["system_prompt"], mensaje)
        firma = f"\n\n- {agente['nombre']}, {agente['cargo']}"
        await enviar_respuesta_inteligente(update, respuesta, firma, update.effective_user.id)
    else:
        await update.message.reply_text(
            f"Recibi tu mensaje: {mensaje}\n\n"
            f"Estas hablando con {agente['nombre']} ({agente['cargo']}).\n\n"
            "IA pendiente: fondear DeepSeek $5."
        )


def crear_app():
    request = httpx.AsyncClient(timeout=30.0)
    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("ayuda", cmd_ayuda))
    app.add_handler(CommandHandler("help", cmd_ayuda))
    app.add_handler(CommandHandler("quien", cmd_quien))
    app.add_handler(CommandHandler("salir", cmd_salir))

    for agente_key, comandos in COMANDOS.items():
        handler = crear_handler_agente(agente_key)
        for cmd in comandos:
            app.add_handler(CommandHandler(cmd.replace("/", ""), handler))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_onboarding_callback, pattern="^onb:"))
    app.add_handler(CallbackQueryHandler(handle_video_callback, pattern="^vid_"))

    return app


def main():
    if not TOKEN:
        print("ERROR: falta TELEGRAM_BOT_TOKEN")
        return
    print("Bot multi-agente iniciado")
    print(f"DeepSeek: {'ACTIVO' if tiene_llm() else 'PENDIENTE'}")
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


if __name__ == "__main__":
    main()
