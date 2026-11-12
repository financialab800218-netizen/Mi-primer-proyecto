# Anexo AP - Integracion de Supabase

Fecha: 10 octubre 2026

## Objetivo

Integrar Supabase como base de datos persistente para TutorIA Cuba, guardando usuarios, perfiles TCP y contenido.

## Componentes implementados

### 1. Proyecto Supabase
- Nombre: tutoria ia cuba
- URL: https://ktdpxyqpghipmsftepgl.supabase.co
- Plan: Free (gratuito)
- Region: US East

### 2. Tablas creadas

usuarios:
- id (UUID, primary key)
- telegram_id (TEXT unico)
- nombre (TEXT)
- email (TEXT unico)
- rol (TEXT, default alumno)
- created_at, updated_at (TIMESTAMPTZ)

tcp_perfiles:
- id (UUID, primary key)
- usuario_id (UUID, referencia a usuarios)
- codigo_tcp (TEXT unico)
- cedula (TEXT)
- especialidad (TEXT)
- categoria (TEXT, default bronce)
- validado (BOOLEAN)
- created_at (TIMESTAMPTZ)

contenido:
- id (UUID, primary key)
- creador_id (TEXT)
- creador_tipo (TEXT)
- titulo (TEXT)
- descripcion (TEXT)
- tipo (TEXT)
- url (TEXT)
- tamaño_bytes (BIGINT)
- materia (TEXT)
- nivel (TEXT)
- idioma (TEXT, default es)
- estado (TEXT, default borrador)
- validado_ia (BOOLEAN)
- validado_admin (BOOLEAN)
- created_at (TIMESTAMPTZ)

### 3. Cliente Python

Archivo: supabase_helper.py

Funciones:
- crear_usuario(telegram_id, nombre, email, rol)
- obtener_usuario(telegram_id)
- guardar_contenido(creador_id, creador_tipo, titulo, tipo, url, ...)

### 4. Configuracion

Variables en backend/app/.env:
- SUPABASE_URL=https://ktdpxyqpghipmsftepgl.supabase.co
- SUPABASE_KEY=sb_publishable_xxx

## Pruebas realizadas

1. Conexion desde VPS: Exitosa
2. Consulta tabla usuarios: Status 200, respuesta []
3. Creacion de usuario test: Status 201
4. Verificacion en dashboard: Datos visibles

## RLS (Row Level Security)

Estado: DESACTIVADO en las 3 tablas

Motivo: Para desarrollo, permitir al bot leer y escribir sin politicas complejas.

Pendiente: Activar RLS con politicas especificas cuando el proyecto tenga usuarios reales.

## Proximos pasos

1. Ejecutar script integrar_supabase.py para conectar el bot
2. Probar registro automatico desde Telegram
3. Activar RLS en produccion
4. Implementar politicas por rol