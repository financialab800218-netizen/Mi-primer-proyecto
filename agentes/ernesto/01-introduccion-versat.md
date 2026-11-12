# Módulo 01 — Introducción a VERSAT Sarasolo

**Agente:** Ernesto (Contador Jefe Digital)
**Nivel:** N1 — Aprendiz de Contador
**Módulo:** 01 — Fundamentos de VERSAT Sarasolo
**Duración estimada:** 2 semanas
**Fuente oficial:** Manual de Usuario VERSAT Sarasola Producción v2-9 (DATAZUAR / AZCUBA)
**Asesor humano:** [Especialista VERSAT]
**Fecha:** 2/octubre/2026

---

## 1. ¿Qué es VERSAT Sarasolo?

VERSAT Sarasolo es el sistema contable automatizado de uso obligatorio en las entidades cubanas, desarrollado por la División DATAZUAR de AZCUBA.

Es el software oficial que implementa el Nomenclador de Cuentas definido en la Resolución 360/2013 y las proformas de Estados Financieros de la Resolución 369/2013.

---

## 2. Arquitectura general

VERSAT Sarasolo se organiza en módulos independientes que comparten una base de datos común:

| Módulo | Función |
|--------|---------|
| Contabilidad | Registro de operaciones y comprobantes |
| Finanzas | Tesorería, cheques, transferencias, obligaciones |
| Inventario | Control de existencias y movimientos |
| Activo Fijo | Gestión de AFT, amortización, baja |
| Facturación | Emisión y control de facturas |
| Nóminas | Cálculo y pago de salarios |

---

## 3. Estructura básica de datos

VERSAT maneja tres niveles de clasificación:

1. **Cuenta** — Según el Nomenclador (ej. 101 Efectivo en Caja)
2. **Centro de Costo** — Área que genera el gasto (ej. Acuicultura)
3. **Subelemento** — Detalle específico (ej. Alimento para peces)

---

## 4. Configuración inicial (obligatoria antes de operar)

Antes de registrar cualquier operación, se debe:

1. Configurar la contabilidad general
2. Importar el plan de cuentas (desde Excel)
3. Crear los centros de costo
4. Crear o importar los subelementos
5. Declarar las cuentas de gasto
6. Definir las cuentas de ingreso y egreso

Sin esta configuración, el sistema no permite operar.

---

## 5. Operaciones diarias

Las operaciones se registran mediante **comprobantes**. Cada comprobante:

- Registra un hecho económico
- Afecta dos o más cuentas
- Respeta el principio de partida doble
- Queda vinculado a un centro de costo y subelemento

---

## 6. Reportes principales

| Reporte | Función |
|---------|---------|
| Balance de Comprobación | Verifica equilibrio de saldos |
| Estado de Rendimiento | Utilidad o pérdida del período |
| Gasto por Elemento | Desglose de gastos por tipo |
| Estados Financieros | Salida oficial para MFP y ONAT |

---

## 7. Cierres

VERSAT maneja dos tipos de cierre:

- **Cierre mensual** — Al final de cada mes
- **Cierre anual** — Al final del ejercicio fiscal

Ambos son obligatorios para generar los estados financieros oficiales.

---

## 8. Ejercicios de práctica — Nivel 1

### Ejercicio 1 — Identificar módulos

¿Qué módulo de VERSAT usarías para registrar...?

1. La compra de alimento para peces → Inventario
2. El pago de un cheque → Finanzas
3. La depreciación de un equipo → Activo Fijo
4. La venta de un producto → Facturación

### Ejercicio 2 — Configuración inicial

Ordena correctamente los pasos para configurar VERSAT:

1. Importar plan de cuentas desde Excel
2. Crear centro de costo
3. Crear o importar subelementos
4. Configurar contabilidad general

**Orden correcto:** 4 → 1 → 2 → 3

### Ejercicio 3 — Comprobantes

Un comprobante correcto debe:

- Afectar al menos 2 cuentas
- Mantener la partida doble (débito = crédito)
- Estar vinculado a un centro de costo
- Estar vinculado a un subelemento

---

## 9. Relación con los videos de formación

El módulo 01 de VERSAT se compone de **17 videos** que se agrupan así:

| Sub-módulo | Videos | Tema |
|------------|--------|------|
| 1A | 4 | Instalación y setup inicial |
| 1B | 5 | Configuración avanzada |
| 1C | 3 | Operaciones diarias |
| 1D | 5 | Reportes y cierres |

Los audios de cada video se transcribirán y servirán como material complementario.

---

## 10. Evaluación N1

### Criterios de evaluación

| # | Criterio | Peso |
|---|----------|------|
| 1 | Identifica los módulos de VERSAT | 15% |
| 2 | Conoce la estructura Cuenta-CENTRO-Subelemento | 20% |
| 3 | Domina la configuración inicial | 20% |
| 4 | Registra comprobantes correctamente | 25% |
| 5 | Genera reportes básicos | 20% |

**Mínimo para aprobar:** 4/5 en cada criterio.

---

## 11. Recursos complementarios

- Manual de Usuario VERSAT Sarasola Producción v2-9
- Resolución 360/2013 (Nomenclador)
- Resolución 369/2013 (Proformas)
- 17 videos del módulo Contabilidad (por transcribir)
- Asesor humano: Especialista VERSAT

---

## 12. Registro de avance

| Fecha | Tema | Estado | Asesor |
|-------|------|--------|--------|
| 2/oct/2026 | Módulo 01 creado | Completado | — |
| — | Configuración inicial | Pendiente | — |
| — | Operaciones diarias | Pendiente | — |
| — | Reportes | Pendiente | — |
| — | Evaluación N1 | Pendiente | — |

---

Documento oficial de formación de ERNESTO — 2/octubre/2026
