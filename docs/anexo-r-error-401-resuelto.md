📘 ANEXO R: ERROR 401 SUPABASE RESUELTO

Fecha: 28 septiembre 2026
Estado: RESUELTO

---

PROBLEMA:
Backend FastAPI no podía conectarse a Supabase. Error 401 persistente.

CAUSA REAL (dos problemas):

1. La URL de Supabase tenía un error tipográfico:
   - Incorrecto: cxvgzpsnebvvphgvhdic
   - Correcto: cxvgzpsnebvvphgvhdic
   (Corregido previamente)

2. La API KEY usada era la "publishable" (pública):
   - sb_publishable_...
   - Esta key solo sirve para frontend
   - NO tiene permisos para operaciones de backend

SOLUCIÓN:
Cambiar la key de "publishable" a "service_role":
- SUPABASE_KEY=sb_secret_...
- Esta key tiene permisos completos de backend

VERIFICACIÓN:
Comando: python -c "from services.supabase_client import supabase_client; print(supabase_client.health_check())"
Resultado: {'status': 'conectado', 'url': 'https://cxvgzpsnebvvphgvhdic.supabase.co'}

---

LECCIÓN APRENDIDA:
- publishable = solo frontend
- service_role = backend
- Nunca confundir las dos

NOTA DE SEGURIDAD:
La key service_role quedó expuesta en chat.
Acción pendiente: rotar la key en Supabase.

---

FIN DEL ANEXO R
