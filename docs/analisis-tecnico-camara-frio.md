

# Analisis Tecnico de la Camara de Frio KLEZ-030S

**Version:** 1.0
**Fecha:** 2/octubre/2026
**Autor:** Yosbel Collazo Avila + Socio IA
**Estado:** Oficial - Analisis tecnico
**Equipo:** Camara de frio movil KLEZ-030S + Compresor Copeland ZB21KQE

---

## 1. Objetivo

Documentar las especificaciones tecnicas de la camara de frio del PDL DESSPEZ, analizar su compatibilidad con el inversor solar PowMr actual, y proponer soluciones al problema de compatibilidad electrica.

---

## 2. Especificaciones de la Unidad Condensadora

### 2.1. Datos de placa

| Parametro | Valor |
|-----------|-------|
| Modelo | KLEZ-030S |
| Aplicacion | -30 grados C a 0 grados C |
| Refrigerante | R404A |
| Alimentacion | 220V 60Hz MONOFASICO |
| Ventilador | 1 unidad de 80W |
| Flujo de aire | 3500 m3/h |
| Dimensiones | 955 x 365 x 800 mm |

### 2.2. Capacidad de frio (a 45 grados C ambiente)

| Temperatura evaporacion | Capacidad |
|-------------------------|-----------|
| 0 grados C | 6770 W |
| -5 grados C | 5690 W |
| -10 grados C | 4760 W |
| -15 grados C | 3950 W |
| -30 grados C | 2070 W |

**Interpretacion:** El equipo tiene capacidad sobrada para la operacion actual de 240 kg/mes de filete.

---

## 3. Especificaciones del Compresor

### 3.1. Datos de placa

| Parametro | Valor |
|-----------|-------|
| Modelo | Copeland Scroll ZB21KQE |
| Voltaje | 220-240V |
| Fases | 1 (monofasico) |
| Corriente maxima | 16.42 A |
| Corriente de arranque | 75-82 A |
| Refrigerante | R404A |

### 3.2. Analisis de corriente

| Aspecto | Valor |
|---------|-------|
| Corriente operativa | 16.42 A |
| Corriente de arranque | 75-82 A |
| Pico de potencia operativa | 3600 W |
| Pico de potencia de arranque | 16000-18000 W |

**El arranque del compresor es el punto critico.**

---

## 4. Compatibilidad con el Inversor PowMr

### 4.1. Inversor actual

| Parametro | Valor |
|-----------|-------|
| Modelo | POW-LVM5K-48V-N |
| Potencia continua | 5000 VA |
| Potencia pico | 10000 W |
| Voltaje de salida | 120 VAC |
| Entrada bateria | 48 VDC |
| Entrada PV maxima | 5500 W |
| MPPT rango | 120-450 VDC |

### 4.2. Problemas detectados

| # | Problema | Impacto |
|---|----------|---------|
| 1 | Inversor entrega 120V, camara necesita 220V | No funciona directamente |
| 2 | Corriente de arranque del compresor 80A | Pico de 16kW supera la capacidad del inversor |
| 3 | Consumo sostenido de 3.6kW | Al limite del inversor |

**Conclusion:** El inversor PowMr no puede alimentar la camara directamente.

---

## 5. Soluciones Propuestas

### 5.1. Opcion A. Transformador + Arrancador suave (RECOMENDADA)

| Componente | Costo estimado |
|------------|----------------|
| Transformador elevador 120V a 220V (5kVA) | $200-400 |
| Arrancador suave (soft starter) | $200-400 |
| Instalacion | $50-100 |
| **Total** | **$450-900** |

**Ventaja:** Resuelve ambos problemas (voltaje y pico de arranque).

### 5.2. Opcion B. Inversor 220V nuevo

| Componente | Costo estimado |
|------------|----------------|
| Inversor 5-8kW 220V monofasico | $1200-2500 |
| Instalacion | $100-200 |
| **Total** | **$1300-2700** |

**Ventaja:** Solucion completa y permanente.
**Desventaja:** Costo alto.

### 5.3. Opcion C. Alimentar solo con red electrica

| Concepto | Costo |
|----------|-------|
| Reconectar camara a red de 220V | $0 |
| Usar inversor solo como respaldo | $0 |
| **Total** | **$0** |

**Ventaja:** Funciona inmediatamente con la red.
**Desventaja:** Depende de la red y del ciclo de 4 horas.

---

## 6. Analisis de Consumo

### 6.1. Consumo diario estimado

| Escenario | Consumo promedio | kWh/dia |
|-----------|------------------|---------|
| Frio minimo (producto ya congelado) | 700 W | 17 kWh |
| Trabajo normal | 1500 W | 36 kWh |
| Congelando producto fresco | 2500 W | 60 kWh |

### 6.2. Referencia

Un hogar cubano promedio consume 5-10 kWh/dia.
La camara consume 3-6 veces mas que un hogar.

---

## 7. Capacidad Practica de la Camara

| Funcion | Capacidad |
|---------|-----------|
| Mantener 500 kg de pescado a -18 grados C | Sin problema |
| Congelar 100 kg de pescado fresco | En 4-6 horas |
| Almacenar 1 tonelada a 0 grados C | Si |
| Servir como punto de frio movil | Excelente |

**Para operacion actual de 240 kg/mes:** Capacidad sobrada.

---

## 8. Estado Actual del Equipo

| Aspecto | Estado |
|---------|--------|
| Camara | Desarmada, fuera del remolque |
| Razon | Convenio con TCP no se concreto |
| Ubicacion propuesta | Instalaciones de BIOCEN |
| Necesidad | Espacio con corriente 220V 24/7 |

---

## 9. Plan de Accion

### 9.1. Accion inmediata (esta semana)

| # | Accion |
|---|--------|
| 1 | Cotizar transformador 120V a 220V |
| 2 | Cotizar arrancador suave para compresor |
| 3 | Buscar alternativa de instalacion con BIOCEN |
| 4 | Verificar consumo real medido de la camara |

### 9.2. Accion a mediano plazo

| # | Accion |
|---|--------|
| 5 | Instalar transformador + arrancador |
| 6 | Reconectar camara al sistema solar |
| 7 | Ampliar paneles solares si es necesario |
| 8 | Documentar operacion real |

---

## 10. Valor Economico del Activo

| Concepto | Valor estimado |
|----------|----------------|
| Camara KLEZ-030S nueva | $5000-8000 USD |
| Compresor Copeland | Incluido |
| Estado actual | Operativo |
| Valor de uso | $200-500/mes en alquiler |

---

## 11. Registro de Cambios

| Version | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2/oct/2026 | Creacion inicial |

---

Documento oficial del Ecosistema Mayabeque - 2/octubre/2026
