📘 LIBRO MAESTRO — AUTOMATIZACIÓN FINANCIALAB CON N8N Y DEEPSEEK

Fecha: 28 septiembre 2026
Objetivo: Flujo automatizado que recibe clientes, genera respuestas con IA, guarda datos y notifica.

---

PARTE 1: ARQUITECTURA DEL FLUJO

Orden de nodos en n8n:
1. Webhook (disparador) — recibe datos del formulario
2. Guardar en Google Sheets — almacena en hoja FinanciaLab
3. Modelo de chat DeepSeek — genera respuesta IA
4. Enviar Gmail — notifica al dueño
5. Responder al Cliente — devuelve la respuesta al cliente

---

PARTE 2: CREDENCIALES

API DeepSeek:
- Proveedor: DeepSeek (nube)
- API Key: platform.deepseek.com (sk-...)
- NO compartir la API Key
- Base URL: https://api.deepseek.com
- Modelos: deepseek-v4-flash o deepseek-v4-pro

Google (Sheets + Gmail):
- Autorizar la misma cuenta de Google en ambos nodos
- Si n8n no encuentra hoja, usar opción Compartir en Drive

---

PARTE 3: CONFIGURACIÓN DE NODOS

Nodo 1: Webhook
- Función: recibe datos
- Al publicar: copiar Production URL
- Pegar URL en formulario web de FinanciaLab

Nodo 2: Guardar en Google Sheets
- Documento: hoja FinanciaLab
- Columnas: fecha, nombre, email, mensaje
- Mapeo:
  - fecha = {{ $now.toISO() }}
  - nombre = {{ $json.body.name }}
  - email = {{ $json.body.email }}
  - mensaje = {{ $json.body.message }}

Nodo 3: DeepSeek Chat
- Credencial: API Key
- Prompt del Sistema:
  Actúa como un asistente de atención al cliente de FinanciaLab.
  Responde amable, clara, profesional.
  Usa el nombre del cliente si se proporciona.
  Agradece su mensaje y responde dudas o indica que un asesor 
  se pondrá en contacto.

Nodo 4: Enviar Gmail
- Credencial: cuenta Google
- Para: correo del dueño
- Asunto: Nuevo cliente en FinanciaLab: {{ $json.name }}
- Mensaje: Nombre, Email, Mensaje del cliente

Nodo 5: Responder al Cliente
- Función: envía respuesta de DeepSeek al Webhook original
- Cliente ve la respuesta en pantalla

---

PARTE 4: SOLUCIÓN DE PROBLEMAS

Error de login DeepSeek:
No usar números de identificación como contraseña.
Usar Log in with Google.

Error al seleccionar hoja en n8n:
Cambiar de From List a By ID.
Pegar el código largo de la URL de Google Drive.

Triángulo rojo en nodos:
Significa credencial faltante o campo obligatorio.
Hacer clic en el nodo y revisar.

Confusión con Chatbot:
La opción Construye con IA crea chatbot interactivo.
Para flujos de formularios usar nodos manuales.

---

PARTE 5: ACTIVACIÓN

1. Probar: pulsar Ejecutar flujo de trabajo
   Verificar que llegue correo y se actualice Sheets.

2. Publicar: pulsar Publicar en n8n
   Esto enciende el flujo 24/7.

3. Copiar URL: hacer clic en nodo Webhook
   Copiar Production URL.

4. Integrar: pegar URL en formulario web de FinanciaLab.

---

PARTE 6: COSTOS Y ESTADO

Costos operativos:
- n8n Cloud: 26 USD por mes (prueba vencida)
- DeepSeek API: 5-10 USD por mes
- Google Workspace: gratis
- Total: 31-36 USD por mes

Estado actual:
- n8n prueba vencida (descargar flujos antes 20 dic 2026)
- DeepSeek sin saldo
- Google Sheets configurado
- Gmail configurado

---

PARTE 7: INTEGRACIÓN CON EMPRESA ÚNICA

n8n + DeepSeek sirven a FinanciaLab, que es Dirección 5 de 
Ecosistema Mayabeque S.R.L.

Futura integración: mismo motor para TutorIA y otras direcciones.

---

FIN DEL LIBRO N8N DEEPSEEK
