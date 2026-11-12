

# Detalles del Chat - Preservacion Total para Traspaso

**Version:** 1.0
**Fecha:** 2/octubre/2026
**Autor:** Yosbel Collazo Avila + Socio IA
**Uso:** Preservar TODO lo discutido que no esta en otros documentos
**Estado:** CRITICO - Complementa al Prompt Maestro

---

## 1. Los 65 Videos de VERSAT

Detalle que NO esta en otros documentos.

### Modulo 01 - Contabilidad 17 videos

Ubicacion: Videos Versat / 01_Contabilidad

Videos:
01_Conf inicial de Contabilidad_clip.mp4 7.87 MB
02_01 Importar Cuentas Fichero Excel.wmv 6.77 MB
02_02 Crear Cuenta.wmv 7.04 MB
02_03 Importar Cuentas Excel.wmv 3.71 MB
02_04 Crear Centro de Costo.wmv 1.69 MB
02_05 Importar Subelementos Excel.wmv 10.93 MB
02_06 Crear un Subelemento.wmv 2.68 MB
02_07 Declarar Cuenta de Gasto.wmv 3.25 MB
02_08 Definir Cuentas de Ing y Egreso_clip.mp4 1.95 MB
03_Crear Comprobante.wmv 3.75 MB
04_Historia de Cuent - Centro y Elemento.wmv 6.9 MB
05_Balance de Comprobacion de Saldo.wmv 2.68 MB
06_Estado de Rendimiento-Ganancia.wmv 5.12 MB
07_Reporte de gasto por elemento.wmv 7.46 MB
08_Generalidades y Reportes.wmv 12.26 MB
09_Cerrar el mes.wmv 2.83 MB
99_CIERRE DEL EJERCICIO O ANO.wmv 6.9 MB

### Modulo 02 - Finanzas 20 videos

Ubicacion: Videos Versat / 02_Finanzas

Videos:
CARGA INICIAL FINANZAS.wmv 17.46 MB
01_Crear Talonario de Cheque.wmv 1.61 MB
02_Emitir Cheque Pagando Factura.wmv 2.77 MB
03_Emitir Cheque de Salario.wmv 2.36 MB
04_Pagos con Transferencias.wmv 2.40 MB
05_CR09 aportes.wmv 1.76 MB
06_Pago de Retenciones.wmv 1.55 MB
07_Estado de Cuenta.wmv 5.42 MB
08_liquidacion de nominapor pagar.wmv 2.20 MB
09_Crear Talon de Recibo de Efectivo.wmv 0.94 MB
10_Deposito de Efectivo.wmv 2.92 MB
11_Crear Obligacion de Cobro.wmv 2.64 MB
12_Reportes Obligaciones de Cobro.wmv 3.10 MB
13_Crear Obligacion de Pago.wmv 3.07 MB
14_Reportes de Obligaciones de Pago.wmv 2.91 MB
15_Cobro de Factura con Cheque.wmv 2.20 MB
16_Cobro de Factura con Transferencia.wmv 2.26 MB
17_Deposito de Cheque de Caja para Banco.wmv 1.33 MB
18_Cancelar un documento o Anular Cancelacion.wmv 0.93 MB
19_Cancelar en Emision.wmv 1.88 MB

### Modulo 03 - Inventario 10 videos

Ubicacion: Videos Versat / 03_Inventario

Videos:
CARGA INICIAL DE INVENTARIO.wmv 19.02 MB
01Compras.wmv 6.84 MB
02_Entrada de Prod Terminada.wmv 2.76 MB
03_Tranferencia Enviada.wmv 4.71 MB
04 Vale de Salida a Gasto.wmv 3.37 MB
05_Devolucion de compra.wmv 2.02 MB
07_Submayor de Producto.wmv 3.87 MB
08_Existencia de Producto.wmv 3.18 MB
09_Inventario 10 o 100.wmv 10.06 MB
10_Cambio de fecha.wmv 3.22 MB

### Modulo 04 - Activo Fijo 9 videos

Ubicacion: Videos Versat / 04_Activo Fijo

Videos:
CARGA INICIAL DE AFT.wmv 11.47 MB
01_Compra y o Alta de AFT.wmv 3.62 MB
02_Traslado de Area.wmv 3.25 MB
03_Modificar Propiedades.wmv 3.56 MB
04_Baja de AFT.wmv 0.87 MB
05_Hoja de Inventario.wmv 1.29 MB
06_Activos por area y Submayor de activo.wmv 2.63 MB
07_Realizar la Amortizacion.wmv 0.81 MB
08_Cerrar Periodo.wmv 1.31 MB

### Modulo 05 - Facturacion 9 videos

Ubicacion: Videos Versat / 05_Facturacion

Videos:
001_Subsistema de Configuracion.mp4 10.59 MB
002_Codificadores de Facturacion.mp4 14 MB
003_Configuracion de Facturacion.mp4 16.33 MB
004_Conceptos de Facturacion.mp4 8.06 MB
005_Crear Talon.mp4 6.26 MB
006_Precio y Expre_Calidad.mp4 9.6 MB
007_Oferta.mp4 15.15 MB
008_crear Facturas.mp4 8.18 MB
009_Crear factura recargo en precio.mp4 7.21 MB

TOTAL: 65 videos aproximadamente 339 MB

Uso previsto: Transcribir con Gemini o IA cuando haya conexion. Guardar en docs/agentes/ernesto/formacion/videos/

---

## 2. Detalles del Bot Multi-Agente

### Estructura de comandos implementados

Comandos basicos:
/start - Bienvenida y menu
/ayuda - Lista de comandos
/quien - Con quien estoy hablando
/salir - Volver a Pablo

Comandos por agente:
/pablo - Activar Pablo Director Adjunto
/ernesto - Activar Ernesto Contador
/marta - Activar Marta Legal
/camilo - Activar Camilo Agricola
/celia - Activar Celia Educativa
/julian - Activar Julian Comercial
/ruben - Activar Ruben Tecnico

Aliases:
/director - Pablo
/adjunto - Pablo
/eco - Ernesto
/contabilidad - Ernesto
/legal - Marta
/abogada - Marta
/agro - Camilo
/campo - Camilo
/edu - Celia
/tutoria - Celia
/comercial - Julian
/ventas - Julian
/tecnico - Ruben
/mantenimiento - Ruben

### Formato de respuestas

Cada agente firma con:
- Nombre, Cargo

Ejemplo:
- Ernesto, Agente Economico

### Deteccion automatica

El bot detecta si hay IA activa con:
tiene_llm() retorna True si hay DEEPSEEK_API_KEY o NVIDIA_API_KEY

Si no hay IA: modo placeholder
Si hay IA: respuesta real del agente

---

## 3. Detalles del Correo de Ernesto

Email: ernesto.asist.econ@outlook.com
Tipo: Outlook
Estado: Activo y funcionando
Proposito: Correo institucional del agente Ernesto
Password: Guardado en .env local
Reenvio: Configurado a collazoavila345@gmail.com

---

## 4. Detalles del Sistema Solar

### Inversor PowMr

Modelo: POW-LVM5K-48V-N
Potencia: 5000 VA continuos / 10000 W pico
Entrada bateria: 48 VDC rango 40 a 60 VDC
Salida AC: 120 VAC
Entrada AC: 90 a 140 VAC
Entrada PV maxima: 5500 W
MPPT rango: 120 a 450 VDC
Estado: Operativo

### Panel solar (triciclo azul)

Ubicacion: Triciclo azul del PDL DESSPEZ
Funcion: Carga baterias del triciclo y respaldo freezer
Potencia: Por confirmar
Estado: Funcionando
Uso actual: Respaldo para freezer cuando no hay corriente

---

## 5. Detalles de la Camara de Frio

### Camara KLEZ-030S

Aplicacion: -30 grados C a 0 grados C
Refrigerante: R404A
Alimentacion: 220V 60Hz MONOFASICO
Dimensiones: 955 x 365 x 800 mm
Fecha fabricacion: abril 2024

### Compresor Copeland Scroll

Modelo: ZB21KQE
Voltaje: 220 a 240V
Fases: 1 monofasico
Corriente maxima: 16.42 A
Corriente arranque: 75 a 82 A

### Estado actual

Desarmada y fuera del remolque
Razon: Convenio con TCP no se concreto
Ubicacion propuesta: BIOCEN biotecnologia Bejucal
Necesita: Espacio con 220V 24 horas
Problema: Inversor PowMr entrega 120V no 220V

### Solucion pendiente

Opcion A: Transformador elevador 120 a 220V mas arrancador suave
Opcion B: Inversor 220V nuevo
Opcion C: Alimentar solo con red 220V y usar solar como respaldo

---

## 6. Detalles del Triciclo Azul y Blanco

### Triciclo Blanco

Uso: Traslado personal de Yosbel
Ruta: Quivican a Bejucal 16 km
Distancia diaria: 32 a 50 km
Baterias: Gel 2 anos de uso
Estado: Baterias malas
Funcion extra: Tiene caja refrigerada
Bateria refrigerado: Independiente de las baterias del triciclo, tambien malas

### Triciclo Azul

Uso: Carga de insumos al proyecto
Sistema solar: Tiene paneles propios
Funcion extra: Respaldo para freezer cuando no hay corriente
Baterias: Limitadas
Estado: Operativo con limitaciones

---

## 7. Detalles del Convenio con Empresa 19 de Abril

Tipo: Convenio operativo
Que se movio: Molino de martillo, desmenuzadora, procesadora de pescado
Razon: Problemas de corriente en sede original
Beneficio: Acceso a corriente trifasica y espacio industrial
Estado: Operando
Implicacion: El pienso se produce alli

---

## 8. Detalles del Combustible

Precio informal actual: 2500 CUP/litro
Precio anterior 2024: 150 CUP/litro
Incremento: 1566 por ciento

Impacto: El combustible se come cualquier margen. Solucion: maximizar uso de triciclos electricos.

---

## 9. Detalles de los Clientes Actuales

### Sector Salud Bejucal

Tipo: Hogar de ancianos, hogar materno, policlinico
Producto: Filete de pescado
Cantidad: 60 kg/semana aproximadamente 240 kg/mes
Precio: 700 CUP/kg
Ingreso mensual: 168000 CUP
Estado: Activo y estable

### SIMAGT

Tipo: Empresa de pienso
Producto: Pienso criollo
Cantidad: 1 tonelada/mes
Precio: 292500 CUP/tonelada
Ingreso mensual: 292500 CUP
Estado: Activo y estable

### Cliente potencial proximo

Sector Educacion Bejucal
Proyeccion: 200 kg/mes
Estado: En negociacion

---

## 10. Detalles de las Proyecciones de Escalado

### Filete de pescado

Etapa actual: 240 kg/mes
Etapa 1: Educacion Bejucal mas 200 kg igual 440 kg/mes
Etapa 2: Salud Quivican mas 250 kg igual 690 kg/mes
Etapa 3: Educacion Quivican mas 250 kg igual 940 kg/mes
Etapa 4: Salud San Jose de las Lajas mas 500 kg igual 1440 kg/mes

### Pienso

Actual: 1 tonelada/mes
Proyeccion: 2 a 3 toneladas/mes
Ingreso potencial: 585000 a 877500 CUP/mes

---

## 11. Detalles de las Fichas de Costos

### Ficha original del filete

Precio pescado entero: 220 CUP/kg
Rendimiento filete: 35 por ciento
Salario diario: 1000 CUP
Costo total ficha: 911 CUP/kg
Precio venta ficha: 1000 CUP/kg

### Ficha actualizada con hielo

Hielo: 250 CUP/kg
Ratio hielo pescado: 1.5 a 1
Costo hielo por kg filete: 1071 CUP
Costo total actualizado: 2145 CUP/kg
Precio venta actual: 700 CUP/kg
Perdida real: 1445 CUP/kg

### Ficha actualizada del carbon

Precio carbon en campo: 1000 CUP
Precio saco: 100 CUP
Transporte: 3500 CUP por 15 sacos
Salario: 1000 CUP por 30 sacos
Costo total actualizado: 1903 CUP/saco
Precio venta actualizado: 2103 CUP/saco

---

## 12. Detalles del Proyecto NUTRIVIDA

Programa: Programa Mundial de Alimentos PMA
Tipo: Sistema fotovoltaico para produccion agropecuaria
Estado: Pendiente de confirmacion
Beneficio esperado: Energia 24 horas

Datos a confirmar:
1. Cuantos kW de potencia
2. Tiene baterias
3. Cuando llega
4. Incluye fabricador de hielo
5. Incluye freezers
6. Incluye instalacion
7. Requiere contraparte
8. Es para PDL o personal

---

## 13. Detalles de la Alianza con BIOCEN

Tipo: Empresa de biotecnologia en Bejucal
Ubicacion: Bejucal Mayabeque
Energia: 24 horas con plantas industriales
Personal: Decenas de trabajadores
Comedor: Tiene comedor obrero

### Estrategia de abordaje

Enfoque: Encontrar el talon de Aquiles
Problema de BIOCEN: Comedor desabastecido, trabajadores desmotivados
Nuestra oferta: Pescado fresco mas pago por Transfermovil
Nuestra peticion: Espacio para camara mas corriente 220V

### Frase clave para la reunion

Director, no vengo a pedirle un favor. Vengo a proponerle una alianza donde los dos ganamos.

---

## 14. Detalles de la Doble Linea Telefonica

Linea 1: Personal mas clientes mas WhatsApp normal
Linea 2: Sistema bot Telegram alertas WhatsApp Business
Equipo principal: Telefono personal de Yosbel
Unico operador: Yosbel

---

## 15. Detalles del Sistema de Inteligencia de Mercado

### Fuentes a monitorear

Facebook 100 por ciento accesible:
Grupos de precios locales
Grupos de insumos
Grupos de compra venta
Paginas oficiales MINAG AZCUBA MEP
Cubadebate Granma

WhatsApp 100 por ciento accesible:
Grupos de proveedores
Clientes directos

Telegram 50 por ciento accesible:
Alertas del sistema
Canales especializados

Twitter X: NO aplica bloqueado en Cuba

### Productos a monitorear

Pollo, aceite, arroz, cafe, azucar, sal, leche, carne de res, carne de cerdo, pescado, combustible.

### Rutina diaria

Manana 10 minutos: grupos de precios
Mediodia 10 minutos: WhatsApp mas Telegram
Tarde 10 minutos: envio al chat analisis

---

## 16. Detalles de las Cuentas y Correos

### Correo principal personal
collazoavila345@gmail.com

### Correo de Ernesto agente economico
ernesto.asist.econ@outlook.com

### QvaPay
Cuenta: yosbelcmgx80
Saldo: 34.89 USD disponibles
Tipo: QvaPay mas wallet non-custodial
Version: 3.2.0

### VISA CardCentral
Estado: Bloqueada por verificacion
Saldo: 5.03 USD
Problema: Correo de verificacion no llega

### GitHub
Usuario: financialab800218-netizen
Repo: Mi-primer-proyecto
Rama: main

---

## 17. Detalles del Anexo V - Seguridad

### Regla principal

NUNCA guardar en documentos ni chat:
Contrasenas
API Keys
Tokens
PINs
Datos de tarjetas
Datos de terceros

### Solo van en .env

Protegido por .gitignore
Nunca subir a GitHub

### En documentos usar

Placeholders como:
CREDENCIAL_ROTADA
API_KEY_AQUI
PASSWORD_AQUI

---

## 18. Detalles de los Principios Rectores

### Formula de responsabilidad legal

Yosbel mas Agentes IA mas Decision Yosbel igual Accion legal

No es IA haciendo cosas. Es Yosbel usando IA para hacer mejor las cosas.

### Formula de formacion progresiva

Agentes empiezan en N0
Progresan por niveles N1 a N5
Cada nivel requiere:
Formacion completa
Examen teorico
Examen practico
Aval del asesor humano
Analisis de factibilidad
Analisis de impacto
Definicion de limites
Aprobacion de Yosbel

---

## 19. Detalles de los Limites de los Agentes

### Lo que NINGUN agente puede hacer

Firmar contratos
Hacer compromisos economicos
Dar datos de terceros
Violar Anexo V
Actuar sin trazabilidad
Operar fuera del marco legal
Publicar en nombre de Yosbel sin firma
Tomar decisiones estrategicas
Acceder a credenciales sensibles
Actuar autonomamente sin auditoria

---

## 20. Detalles del Estado del Bot

### Bot actual

Nombre: tutoria_cuba_bot
Estado: Parado voluntariamente esperando IA
Razon: No tiene sentido correr sin IA activa
Cuando arranca: Al fondear DeepSeek o NVIDIA

### Codigo listo

bot.py - Version original
bot.py.backup - Respaldo
bot_multiagent.py - Nueva version multi-agente
llm_client.py - Capa abstraccion de IA
agents.py - Definicion de 7 agentes

### Variables en .env

LLM_PROVIDER igual deepseek
DEEPSEEK_API_KEY igual placeholder
NVIDIA_API_KEY igual placeholder
NVIDIA_BASE_URL igual https://integrate.api.nvidia.com/v1
NVIDIA_MODEL igual deepseek-ai/deepseek-r1

---

## 21. Detalles de los Documentos Subidos

Total subidos: 28 mas

### Legal 7
anexo-ad-politica-reincorporacion-profesores.md
anexo-af-fundamento-legal-tutoria-herramienta.md
anexo-ag-modelo-consultoria-internacional.md
anexo-ak-constitucion-mipyme.md
anexo-al-ley-185-tierra-agropecuaria.md
decreto-ley-76-2023-cooperativas.md
ley-113-sistema-tributario.md

### Indices 2
indice-autorizaciones.md
prompt-maestro-traspaso.md

### Analisis integral 1
anexo-aa-analisis-integral-proyecto.md

### Perfiles agentes 7
agentes/pablo/perfil.md
agentes/marta/perfil.md
agentes/camilo/perfil.md
agentes/celia/perfil.md
agentes/julian/perfil.md
agentes/ruben/perfil.md
agentes/ernesto/perfil.md

### Formacion Ernesto 2
00-nomenclador-cuentas.md
01-introduccion-versat.md

### Principios 2
principio-responsabilidad-legal.md
principio-formacion-progresiva.md

### Analisis tecnicos 4
analisis-tecnico-camara-frio.md
actualizacion-fichas-costos-2026.md
inventario-equipos-reales-v2.md
analisis-cadena-frio-hielo-acuicultura.md

### Estrategia 4
estrategia-alianza-biocen.md
sistema-inteligencia-mercado.md
plan-financiero-consolidado-12-meses.md
dossier-lobato.md

---

## 22. Detalles de los Documentos Pendientes

Alta prioridad:
1. Guia solicitud usufructo mipyme
2. Analisis Decreto 175 reglamento
3. Anexo AE operacion bajo PDL Aquaponica
4. Anexo W Central Manuel Fajardo
5. Analisis local Bejucal licitacion
6. Guion llamadas academicas
7. Plan escalado 2026-2027
8. Estrategia asesoria legal 2026

Medio plazo:
9. Anexo AH modelo FinanciaLab TutorIA
10. Anexo AB malla curricular
11. Anexo AC onboarding profesores
12. Anexo X sistema autonomo
13. Anexo Y formacion agentes
14. Anexo Z herramientas agentes
15. Analisis Decreto 160
16. Analisis Ley 176
17. Modulos 02 a 05 de Ernesto
18. 5 cursos TutorIA sobre Ley 185

---

## 23. Detalles de las Instituciones Aliadas

Escuela de Oficio - Quivican
Politecnico Agricola - Quivican
Sede Universitaria - Quivican
Centro Nacional Capacitacion AZCUBA 1 - Nacional
Centro Nacional Capacitacion AZCUBA 2 - Nacional

---

## 24. Detalles de los Contactos Pendientes

Llamadas academicas pendientes:
Javier INICA
Georgina Liliana Dimitrova
Olga Lidia Quivican

Todos esperan por nosotros.

---

## 25. Detalles de la Reunion con Lobato

Estado: Pospuesta hasta nuevo aviso
Razon: Problemas personales de Lobato
Continuacion: Seguimos preparando dossier para mejor presentacion

---

## 26. Detalles del Local en Bejucal

Tipo: Local propuesto por gobierno en coordinacion con comercio y gastronomia
Proceso: Licitacion
Ubicacion: Centrico en Bejucal
Corriente: 220V monofasico
Futuro: Posible trifasico
Situacion electrica: Bejucal trabaja con dos fases alternas
Local: A una cuadra de la division de las dos fases
Ventaja: Posibilidad de coordinar con gobierno tener las dos fases
Estado: En proceso de licitacion

---

## 27. Detalles de los Centros de Ciencias

Estado: Esperan por nosotros
Nosotros somos el cuello de botella

---

## 28. Detalles del Mensaje Sugerido para Nuevo Chat

Hola, soy Yosbel Collazo Avila. Vengo del chat anterior donde construimos el Ecosistema Mayabeque mas TutorIA Cuba. Te paso el contexto completo del proyecto para que continuemos donde quedamos.

Tengo en GitHub docs 28 documentos que documentan todo el sistema. Los principales son:

principio-responsabilidad-legal.md
principio-formacion-progresiva.md
anexo-aa-analisis-integral-proyecto.md
dossier-lobato.md
plan-financiero-consolidado-12-meses.md

Estado actual: 28 documentos subidos, 8 pendientes de alta prioridad.

Los 9 proyectos del ecosistema estan documentados. Los 7 agentes IA tienen perfil.

Necesito continuar con:
1. Documentos pendientes alta prioridad
2. Alianza con BIOCEN para camara de frio
3. Fondear IA DeepSeek o NVIDIA
4. Constitucion Mipyme

Confirma que entiendes el contexto y seguimos.

---

## 29. Detalles Sobre Imagenes del Chat

Las imagenes importantes que se compartieron en el chat fueron:

1. Fotos de la camara KLEZ-030S con placas de datos
2. Fotos del compresor Copeland ZB21KQE
3. Fotos de la linea Prodel molino y mezcladora
4. Fotos de la deshidratadora industrial
5. Fotos de los triciclos electricos
6. Fotos de los estanques y microembalses
7. Fotos del inversor PowMr
8. Capturas de QvaPay con saldo
9. Capturas de la camara en el remolque
10. Documentos Gaceta Oficial
11. Documento objeto social PDL Aquaponica
12. Documento Resolucion 369 y 360
13. Documento Decreto-Ley 76 2023
14. Documento Ley 113 tributaria
15. Documento Ley 185 2026

Todas las imagenes importantes fueron descritas en los documentos del inventario y los analisis.

---

## 30. Registro de Cambios

Version 1.0 - 2/oct/2026 - Creacion inicial con detalles del chat completo

---

Documento oficial del Ecosistema Mayabeque - 2/octubre/2026
