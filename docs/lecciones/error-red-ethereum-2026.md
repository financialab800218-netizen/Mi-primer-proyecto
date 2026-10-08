docs/lecciones/error-red-ethereum-2026.md

# Leccion Aprendida - Error de Red Ethereum

Version: 1.0
Fecha: 6/octubre/2026
Autor: Yosbel Collazo Avila + Socio IA
Uso: Registro de error operativo para prevenir recurrencia
Documentos complementarios:
- analisis-decreto-160-mipyme.md
- plan-escalado-2026-2027.md

---

## 1. Resumen del Error

El 6 de octubre de 2026, durante la conversion de QUSD a USDT,
la red destino seleccionada por error fue Ethereum en lugar de
TRON. Esto bloqueo los fondos en la wallet non-custodial de
QvaPay sin posibilidad de moverlos.

---

## 2. Detalle de la Operacion

Capital inicial: 34.89 USD en saldo QvaPay.

Paso 1 - Swap QUSD a USDT: ejecutado correctamente.
Comision QvaPay: 4.00 USD.
Resultado: 30.89 USDT.

Paso 2 - Red seleccionada por defecto: Ethereum (ERC20).
Red requerida: TRON (TRC20).

Paso 3 - Intento de mover a TRON: FALLIDO.
Razon: la red Ethereum requiere ETH para pagar gas.
El usuario no tenia ETH en la wallet.
El swap interno quedo bloqueado.

---

## 3. Consecuencias

Capital inicial: 34.89 USD
Capital despues del error: 30.89 USDT ERC20 (atrapado)
Perdida operativa: 4.00 USD (comision QvaPay)
Capital realmente usable: 13.96 USDT TRON (proveniente
de un segundo swap menor que si se ejecuto correctamente)

---

## 4. Causa Raiz

1. Falta de verificacion de red en la pantalla final
   antes de confirmar la operacion.
2. QvaPay selecciona Ethereum por defecto sin advertir
   claramente los riesgos del gas.
3. Desconocimiento inicial del funcionamiento del gas
   de red: cada blockchain cobra su comision en su
   propia moneda nativa.

---

## 5. Leccion Aprendida

Las redes blockchain son especificas. No basta decir
USDT. Hay que especificar la red completa.

Cada red cobra gas en su propia moneda:

- Ethereum cobra gas en ETH.
- TRON cobra gas en TRX o Energia.
- BSC cobra gas en BNB.
- Polygon cobra gas en MATIC.
- Solana cobra gas en SOL (casi cero).

Enviar USDT en la red equivocada significa que los
fondos quedan atrapados hasta conseguir la moneda
de gas correspondiente.

---

## 6. Reglas Nuevas para el Ecosistema

Regla 1 - Siempre operar en TRON (TRC20).
Regla 2 - Nunca usar Ethereum (ERC20) para USDT.
Regla 3 - Verificar la red en cada pantalla de
confirmacion antes de aceptar.
Regla 4 - Hacer operacion de prueba con 5 USD antes
de mover montos grandes.
Regla 5 - Documentar red, monto y comision en cada
operacion cripto.
Regla 6 - Hacer operaciones cripto criticas solo en
madrugada (2 a 6 AM) cuando la conexion es estable.

---

## 7. Acciones Tomadas

1. Wallet non-custodial creada con 12 palabras.
2. PIN de bloqueo creado para firmar operaciones.
3. Swap menor ejecutado correctamente a TRON.
4. Documento de leccion creado en el repositorio.
5. Reglas nuevas incorporadas al flujo operativo.

---

## 8. Fondos Pendientes de Recuperar

30.89 USDT ERC20 atrapados en wallet Ethereum.
Recuperables cuando se obtenga acceso a ETH.
Opciones:
- Comprar ETH por P2P cuando haya ofertas.
- Recibir ETH de un contacto externo.
- Dejar quietos hasta tener capital mayor.

No hay prisa. Los fondos estan seguros en la wallet
con la frase de 12 palabras.

---

## 9. Cumplimiento Anexo V

Este documento NO contiene:
- Credenciales
- Frase de 12 palabras
- PIN de bloqueo
- Direcciones de wallet completas

Todo dato sensible permanece en el dispositivo del
usuario y en papel fisico.

---

## 10. Registro de Cambios

Version 1.0 - 6/oct/2026 - Creacion inicial.

---

Documento oficial del Ecosistema Mayabeque - 6/octubre/2026
