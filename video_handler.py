"""Maneja la logica de video con menu de opciones y worker asincrono."""
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from estado import videos_pendientes

async def enviar_respuesta_inteligente(update, respuesta, firma, user_id):
    """Envia la respuesta normal o el menu de video segun corresponda."""
    if respuesta and "[MENU_VIDEO]" in respuesta:
        prompt_video = respuesta.replace("[MENU_VIDEO]", "").strip()
        videos_pendientes[user_id] = prompt_video
        
        menu = InlineKeyboardMarkup([
            [InlineKeyboardButton("Gratis (5-10 min)", callback_data="vid_gratis")],
            [InlineKeyboardButton("Premium (200 CUP)", callback_data="vid_pago")],
            [InlineKeyboardButton("Cancelar", callback_data="vid_cancel")]
        ])
        
        texto = (
            "Escena: " + prompt_video + "\n\n"
            "Como deseas generarlo?\n\n"
            "Gratis: Demora 5-10 mins.\n"
            "Premium: Demora 1 min (200 CUP)."
        )
        await update.message.reply_text(texto, reply_markup=menu)
    else:
        await update.message.reply_text((respuesta or "[Sin respuesta]") + firma)

async def handle_video_callback(update, context):
    """Maneja los botones de video."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    if query.data == "vid_cancel":
        videos_pendientes.pop(user_id, None)
        await query.edit_message_text("Video cancelado. En que mas te puedo ayudar?")
        return
    
    prompt = videos_pendientes.get(user_id, "")
    if not prompt:
        await query.edit_message_text("No encontre el prompt del video. Intenta de nuevo.")
        return
    
    if query.data == "vid_gratis":
        await query.edit_message_text("🐢 Video en cola (gratis).\n\nDemora estimada: 5-10 minutos.\nTe avisare por aqui cuando este listo. Puedes seguir chateando mientras tanto.")
        videos_pendientes.pop(user_id, None)
        # Lanzamos el worker en segundo plano
        context.application.create_task(generar_video_bg(update, context, prompt, es_premium=False))
    
    elif query.data == "vid_pago":
        await query.edit_message_text("🐇 Video premium solicitado.\n\nSe descontaran 200 CUP.\nGenerando en alta calidad...")
        videos_pendientes.pop(user_id, None)
        # Lanzamos el worker en segundo plano
        context.application.create_task(generar_video_bg(update, context, prompt, es_premium=True))

async def generar_video_bg(update, context, prompt, es_premium):
    """Worker asincrono que genera el video sin bloquear el chat."""
    chat_id = update.callback_query.message.chat_id
    
    # --- AQUI IRA LA LLAMADA REAL A AGNES EN EL FUTURO ---
    # Por ahora, simulamos el tiempo de espera para probar la asincronia.
    # El video gratuito tarda mas (15s) que el premium (5s) en esta simulacion.
    await asyncio.sleep(5 if es_premium else 15)
    
    try:
        # En el futuro, aqui usaremos: await context.bot.send_video(chat_id=chat_id, video=open(ruta, 'rb'))
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"✅ [SIMULACION DE WORKER] Tu video {'Premium' if es_premium else 'Gratis'} esta listo.\n\nPrompt: {prompt}\n\n(El proceso asincrono funciono sin bloquear el bot)."
        )
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error en el worker: {e}")
