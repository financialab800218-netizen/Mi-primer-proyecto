"""Maneja la logica de video con menu de opciones."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def enviar_respuesta_inteligente(update, respuesta, firma, user_id):
    """Envia la respuesta normal o el menu de video segun corresponda."""
    if respuesta and "[MENU_VIDEO]" in respuesta:
        prompt_video = respuesta.replace("[MENU_VIDEO]", "").strip()
        from estado import videos_pendientes
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
    from estado import videos_pendientes
    
    if query.data == "vid_cancel":
        videos_pendientes.pop(user_id, None)
        await query.edit_message_text("Video cancelado. En que mas te puedo ayudar?")
        return
    
    prompt = videos_pendientes.get(user_id, "")
    if not prompt:
        await query.edit_message_text("No encontre el prompt del video. Intenta de nuevo.")
        return
    
    if query.data == "vid_gratis":
        await query.edit_message_text(
            "Video en cola (gratis).\n\n"
            "Demora estimada: 5-10 minutos.\n"
            "Te avisare aqui cuando este listo.\n\n"
            "(Funcion de cola en desarrollo)"
        )
        videos_pendientes.pop(user_id, None)
    
    elif query.data == "vid_pago":
        await query.edit_message_text(
            "Video premium solicitado.\n\n"
            "Se descontaran 200 CUP de tu billetera.\n\n"
            "(Funcion de pago en desarrollo)"
        )
        videos_pendientes.pop(user_id, None)
