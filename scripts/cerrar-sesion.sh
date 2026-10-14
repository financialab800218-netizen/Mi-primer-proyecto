#!/bin/bash
# Cierre de sesión automático
echo "=== CERRANDO SESION ==="
date
echo ""

echo "=== 1. Regenerar inventario ==="
cd /root/Mi-primer-proyecto
find docs -name "*.md" -type f | sort | sed 's|^docs/||' > docs/INVENTARIO.md
echo "OK: $(wc -l < docs/INVENTARIO.md) documentos listados"
echo ""

echo "=== 2. Estado servicios ==="
systemctl is-active tutoria-bot.service tutoria-backend.service tutoria-tunnel.service
echo ""

echo "=== 3. Git status ==="
git status --short
echo ""

echo "=== 4. Commit + push ==="
git add -A
git commit -m "auto: cierre de sesion $(date +%d-%b-%Y)" || echo "Sin cambios"
git push origin main
echo ""

echo "=== SESION CERRADA ==="
