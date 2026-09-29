📘 ANEXO V: REGLA DE SEGURIDAD DEL PROYECTO

Fecha: 28 septiembre 2026
Tipo: Regla permanente de manejo de credenciales
Aplica a: Todos los documentos, repositorios, respaldos y comunicaciones del proyecto.

---

PRINCIPIO RECTOR

Las credenciales NUNCA se documentan.
Las credenciales SOLO viven en lugares seguros y locales.
El Libro Maestro es público y NO contiene secretos.

---

PARTE I: QUE ES UNA CREDENCIAL

Se consideran credenciales (y NO se documentan):

1. Contrasenas de cualquier servicio
2. API Keys (DeepSeek, OpenAI, Gemini, Groq, Anthropic)
3. Tokens de acceso (GitHub, Telegram, Supabase)
4. Secret keys (Supabase, Stripe, otros)
5. PINs (tarjetas, vouchers, dispositivos)
6. Datos de tarjetas (numero, CVV, vencimiento)
7. Codigos de recuperacion (2FA, backup codes)
8. URLs con credenciales embebidas
9. Certificados digitales privados
10. Claves SSH privadas

---

PARTE II: DONDE SI VAN LAS CREDENCIALES

1. Archivo .env del proyecto
   - Ubicacion: backend/app/.env
   - Protegido por: .gitignore
   - NUNCA se sube a GitHub

2. Gestor de contrasenas (opcional)
   - Bitwarden, 1Password, KeePass
   - Recomendado para multiples credenciales

3. Papel fisico en lugar seguro
   - Para credenciales criticas
   - Guardar en caja fuerte o lugar privado

4. Notas de Keep (Google)
   - Protegidas por cuenta Google
   - Cifrado de extremo a extremo

---

PARTE III: DONDE NO VAN LAS CREDENCIALES

PROHIBIDO guardar credenciales en:

1. Libro Maestro (docs/ en GitHub)
2. Repositorio publico o privado
3. Documentos compartidos (Google Docs)
4. Chat con la IA
5. Capturas de pantalla
6. WhatsApp / Telegram
7. Correo electronico
8. Papeleria sin proteccion
9. Notas sin cifrado
10. Cualquier lugar que pueda ser visto por terceros

---

PARTE IV: FORMATO PARA DOCUMENTAR

Cuando sea necesario referirse a una credencial en un documento,
usar SIEMPRE placeholders:

- [GITHUB_TOKEN] en lugar del token real
- [DEEPSEEK_KEY] en lugar de la API key
- [SUPABASE_SECRET] en lugar del secret
- [SUPABASE_PUBLISHABLE] en lugar de la key publica
- [TELEGRAM_TOKEN] en lugar del token del bot
- [CARDCENTRAL_PASSWORD] en lugar de la contrasena
- [VISA_PIN] en lugar del PIN
- [CREDENCIAL_ROTADA] cuando ya se roto

---

PARTE V: PROCESO CUANDO SE EXPONE UNA CREDENCIAL

Si una credencial queda expuesta accidentalmente:

PASO 1: Reconocer
- Identificar la credencial expuesta
- Identificar donde quedo expuesta
- Evaluar el riesgo (publica, privada, critica)

PASO 2: Rotar inmediatamente
- Ir al servicio correspondiente
- Generar nueva credencial
- Revocar la antigua
- Actualizar el .env con la nueva

PASO 3: Limpiar
- Eliminar la credencial de todos los documentos
- Reemplazar por [CREDENCIAL_ROTADA]
- Hacer commit del cambio

PASO 4: Documentar
- Anotar el incidente en el Anexo R
- Fecha, credencial, accion tomada
- Sin exponer la nueva credencial

---

PARTE VI: RESPONSABILIDADES

YOSBEL (Representante):
- Guardar credenciales en .env
- No compartir credenciales en chat
- Rotar cuando sea necesario
- Verificar antes de subir a GitHub

IA (Socio estrategico):
- Generar documentos con placeholders
- Nunca solicitar credenciales reales
- Alertar si detecta credenciales en docs
- Recordar la regla periodicamente

---

PARTE VII: AUDITORIA PERIODICA

Frecuencia: mensual

Procedimiento:
1. Ejecutar comando de verificacion:
   grep -rn -E "ghp_|sk-|sb_secret_|password|token" docs/

2. Si aparece algo, limpiar y rotar

3. Actualizar este anexo con nuevos patrones a buscar

4. Documentar la auditoria en el Anexo R

---

PARTE VIII: CREDENCIALES CONOCIDAS Y SU ESTADO

Esta seccion NO contiene valores reales, solo referencia:

| Servicio | Tipo | Estado |
|----------|------|--------|
| GitHub | Token clasico | Activo |
| Supabase | Secret key | Activo |
| Supabase | Publishable key | Activo |
| DeepSeek | API Key | PENDIENTE (falta fondear) |
| Telegram Bot | Token | Activo |
| CardCentral | Password | Activo |

Cuando una credencial se rota, actualizar el estado aqui.

---

PARTE IX: LECCIONES APRENDIDAS

Incidente 1: 28 sep 2026
- Credenciales en maestro-v2.0.md
- Accion: limpiar el documento
- Estado: PENDIENTE de rotar en el servicio

Incidente 2: 28 sep 2026
- Credenciales en anexo-r-error-401-resuelto.md
- Accion: limpiar el documento
- Commit: 7adec3f
- Estado: RESUELTO

Leccion: Revisar antes de hacer commit.

---

PARTE X: CONSECUENCIAS DE INCUMPLIMIENTO

Riesgos de exponer credenciales:

1. Acceso no autorizado a servicios
2. Robo de informacion
3. Uso indebido en nombre del proyecto
4. Costos economicos imprevistos
5. Perdida de confianza de socios
6. Sanciones legales

Recomendacion: Tratar cada credencial como si fuera dinero en efectivo.

---

PARTE XI: HERRAMIENTAS DE VERIFICACION

Comando de auditoria rapida:

grep -rn -E "ghp_|sk-[A-Za-z0-9]{20}|sb_secret_|sb_publishable_|password|token|api_key" docs/ backend/ bot.py

Comando de auditoria del .env (sin mostrar valores):

cat backend/app/.env | sed 's/=.*/=[OCULTO]/'

Verificar que .env esta protegido:

git check-ignore backend/app/.env

---

PARTE XII: COMPROMISO

Este anexo es un COMPROMISO del proyecto.

Todo miembro del equipo (Yosbel + IA) se compromete a:

1. No documentar credenciales
2. No compartir credenciales en chat
3. Usar placeholders en documentos
4. Rotar cuando se expongan
5. Auditar periodicamente
6. Ensenar esta regla a futuros colaboradores

---

FIN DEL ANEXO V
