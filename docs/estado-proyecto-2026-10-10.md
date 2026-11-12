# Estado del Proyecto - 10 octubre 2026

## Infraestructura

- VPS EQVPS activo 24/7 (Alemania, 3 USD/mes)
- Bot Telegram @tutoria_cuba_bot operativo
- NVIDIA NIM como motor principal (openai/gpt-oss-20b)
- Groq como respaldo automatico (openai/gpt-oss-120b)
- Router multi-proveedor (llm_router.py) funcionando
- Auto-push a GitHub operativo
- Arranque automatico con systemd

## Componentes activos

### Herramientas (7)
1. leer_archivo
2. listar_archivos
3. buscar_texto
4. escribir_archivo (con auto-push a GitHub)
5. crear_carpeta
6. git_status
7. git_commit_push

### Agentes (7)
- Pablo: Director Adjunto - Clasifica y deriva
- Ernesto: Contador Jefe Digital
- Marta: Asesora Legal - Ejecuta archivos
- Camilo: Ingeniero Agronomo
- Celia: Coordinadora Academica
- Julian: Director Comercial
- Ruben: Jefe de Mantenimiento

## Base de datos
- Memoria persistente: SQLite (memoria.db)
- Historial de conversaciones: funcional

## Documentos en el repositorio

- 45+ archivos en docs/
- 12 en docs/legales/
- 10 en docs/estrategia/

## Logros del dia 10 octubre

1. Cuenta Groq creada y configurada
2. API Key guardada en .env
3. llm_router.py creado y funcionando
4. Modelo Groq actualizado a openai/gpt-oss-120b
5. Bot modificado para usar el router
6. Prueba de Marta en Telegram exitosa
7. Costos operativos: 3 USD/mes total

## Pendientes priorizados

### Corto plazo (esta semana)
- Arreglar prompt de Pablo (reconocer a Yosbel como dueño)
- Documentar todos los anexos recientes
- Probar fallback de Groq en produccion
- Reforzar prompts por agente