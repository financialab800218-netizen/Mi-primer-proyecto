from telegram import InlineKeyboardButton, InlineKeyboardMarkup
"""Onboarding de usuarios nuevos en TutorIA Cuba."""
import supabase_helper as sb


def es_usuario_nuevo(telegram_id):
    return sb.obtener_usuario(str(telegram_id)) is None


def registrar_usuario(telegram_id, nombre, username=None):
    return sb.crear_usuario(telegram_id, nombre)


def marcar_completado(telegram_id):
    pass


def menu_agentes_inline():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Pablo", callback_data="onb:pablo"),
         InlineKeyboardButton("💰 Ernesto", callback_data="onb:ernesto")],
        [InlineKeyboardButton("⚖️ Marta", callback_data="onb:marta"),
         InlineKeyboardButton("🌾 Camilo", callback_data="onb:camilo")],
        [InlineKeyboardButton("📚 Celia", callback_data="onb:celia"),
         InlineKeyboardButton("💼 Julián", callback_data="onb:julian")],
        [InlineKeyboardButton("🔧 Rubén", callback_data="onb:ruben")],
        [InlineKeyboardButton("✅ Empezar con Pablo", callback_data="onb:empezar")],
    ])


async def enviar_bienvenida(update):
    user = update.effective_user
    nombre = user.first_name or "amigo"
    texto = BIENVENIDA.format(nombre=nombre)
    await update.message.reply_text(texto, reply_markup=menu_agentes_inline())


async def handle_onboarding_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data or ""

    if not data.startswith("onb:"):
        return

    accion = data.split(":", 1)[1]

    if accion == "empezar":
        marcar_completado(query.from_user.id)
        await query.edit_message_text(
            "Perfecto. Escribeme lo que necesites.\n\n"
            "Comandos utiles:\n"
            "  /ayuda  - Ver lista de agentes\n"
            "  /quien  - Con quien hablo\n"
            "  /salir  - Volver a Pablo\n"
            "  /pablo /marta /camilo  - Cambiar de agente"
        )
        return

    # Cambio a un agente especifico
    from bot_multiagent import user_agents
    user_agents[query.from_user.id] = accion
    marcar_completado(query.from_user.id)

    nombres = {
        "pablo": "Pablo (Director Adjunto)",
        "ernesto": "Ernesto (Contador Jefe)",
        "marta": "Marta (Asesora Legal)",
        "camilo": "Camilo (Ingeniero Agrónomo)",
        "celia": "Celia (Coordinadora Académica)",
        "julian": "Julián (Director Comercial)",
        "ruben": "Rubén (Jefe de Mantenimiento)",
    }
    await query.edit_message_text(
        f"Perfecto. Ahora hablas con {nombres.get(accion, accion)}.\n\n"
        "Escribeme lo que necesites."
    )

