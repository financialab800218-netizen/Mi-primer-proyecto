"""Maneja la logica de video con menu de opciones y worker asincrono real."""
import asyncio
import os
import time
import httpx
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from estado import videos_pendientes
from video_router import generar_video_multi

# ... (las funciones enviar_respuesta_inteligente y handle_video_callback se quedan igual)
async def enviar_respuesta_inteligente(update, respuesta, firma, user_id):
    if respuesta and "[MENU_VIDEO]" in respuesta:
        prompt_video = respuesta.replace("[MENU_VIDEO]", "").strip()
        videos_pendientes[user_id] = prompt_video
        menu = InlineKeyboardMarkup([
            [InlineKeyboardButton("Gratis (5-10 min)", callback_data="vid_gratis")],
            [InlineKeyboardButton("Premium (200 CUP)", callback_data="vid_pago")],
            [InlineKeyboardButton("Cancelar", callback_data="vid_cancel")]
        ])
        texto = "Escena: " + prompt_video + "\n\nComo deseas generarlo?\n\nGratis: Demora 5-10 mins.\nPremium: Demora 1 min (200 CUP)."
        await update.message.reply_text(texto, reply_markup=menu)
    else:
        await update.message.reply_text((respuesta or "[Sin respuesta]") + firma)

async def handle_video_callback(update, context):
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
        asyncio.create_task(generar_video_bg(update, context, prompt, es_premium=False))
    
    elif query.data == "vid_pago":
        await query.edit_message_text("🐇 Video premium solicitado.\n\nSe descontaran 200 CUP.\nGenerando en alta calidad...")
        videos_pendientes.pop(user_id, None)
        asyncio.create_task(generar_video_bg(update, context, prompt, es_premium=True))

async def generar_video_bg(update, context, prompt, es_premium):
    """Worker asincrono que usa el Router Multi-Proveedor."""
    chat_id = update.callback_query.message.chat_id
    
    try:
        # LLAMAMOS AL ROUTER
        url_video = await generar_video_multi(prompt, es_premium)
        
        # Descargar y enviar
        nombre_archivo = f"vid_{update.effective_user.id}_{int(time.time())}.mp4"
        carpeta = "/root/Mi-primer-proyecto/backend/app/static/img/videos"
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, nombre_archivo)

        async with httpx.AsyncClient() as client:
            vid_resp = await client.get(url_video, timeout=120.0)
            with open(ruta, "wb") as f:
                f.write(vid_resp.content)

        tipo = "Premium" if es_premium else "Gratis"
        with open(ruta, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=chat_id,
                video=video_file,
                caption=f"✅ Video {tipo} generado.\nPrompt: {prompt}"
            )

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"❌ {str(e)}")
