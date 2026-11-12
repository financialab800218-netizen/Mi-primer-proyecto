📘 LIBRO MAESTRO — TUTORIA CUBA (SUPABASE)

Fecha: 28 septiembre 2026
Estado: Backend configurado, frontend pendiente
Proyecto Supabase: Tutoria IA Cuba

---

PARTE 1: VISIÓN GENERAL

Nombre: Tutor IA Cuba
Tipo: Aplicación móvil educativa para tutorías con IA
Público: Estudiantes de Cuba
Estado: Backend configurado en Supabase. Frontend pendiente de conectar.

---

PARTE 2: INFRAESTRUCTURA SUPABASE

DATOS DEL PROYECTO:
- Organización: Tutori IA Cuba
- Plan: Gratuito NANO
- Proyecto Activo: Tutoria IA Cuba
- URL del Proyecto: https://ktdpxyqpghipmsftepgl.supabase.co
- Estado: Saludable

---

PARTE 3: BASE DE DATOS

Esquema public:
Tabla creada: profiles

Estructura:
- id (uuid, primary key, referencia auth.users con on delete cascade)
- full_name (text)
- role (text, default 'estudiante')
- created_at (timestamptz, default timezone('utc', now()))

---

PARTE 4: SEGURIDAD (Row Level Security)

RLS activado en tabla profiles.

3 políticas creadas:
1. Select: usuarios ven su propio perfil
2. Update: usuarios actualizan su propio perfil
3. Insert: usuarios insertan su propio perfil

---

PARTE 5: AUTOMATIZACIÓN (Trigger)

Función creada: public.handle_new_user()
Trigger: on_auth_user_created

Funcionamiento:
Cada vez que un usuario se registra en Supabase Auth, se inserta automáticamente una fila en profiles con:
- id del usuario
- nombre completo (de metadatos)
- rol por defecto 'estudiante'

---

PARTE 6: ERRORES Y SOLUCIONES

Problema 1: Chrome traducía SQL al español
Solución: Desactivar traducción automática en Supabase

Problema 2: Error de sintaxis por paréntesis suelto
Solución: Limpiar editor SQL antes de pegar

Problema 3: Página de autenticación se cierra por VPN + traductor
Solución: Pendiente de configurar

---

PARTE 7: CREDENCIALES

IMPORTANTE: NO incluir credenciales en este documento.
Las credenciales se guardan por separado en:
- .env del proyecto
- Notas de Keep (respaldo)

---

PARTE 8: PRÓXIMOS PASOS

1. Configurar Authentication en Supabase
   - Activar proveedor Email
   - Desactivar confirmación por correo para pruebas

2. Conectar Lovable con Supabase
   - Actualizar Lovable con credenciales de Supabase
   - Actualmente usa Lovable Cloud

3. Diseñar Dashboard del Estudiante
   - Materias
   - Tutorías pendientes
   - Botón Pedir Tutoría

4. Publicar App
   - Botón Publish de Lovable
   - Generar enlace web o app instalable

5. Pruebas en dispositivos
   - Registro y login reales
   - Verificar con Supabase

---

PARTE 9: INTEGRACIÓN CON EMPRESA ÚNICA

TutorIA es Dirección 5 (Educación y Consultoría) de Ecosistema Mayabeque S.R.L.

Integración con FinanciaLab:
- Modelo A: referencia comercial
- Ver Anexo O

---

FIN DEL LIBRO TUTORIA SUPABASE

