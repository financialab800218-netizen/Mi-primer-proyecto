import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Reemplazar la imagen del logo vacío por un ícono de libro real
# Buscamos la etiqueta <img> y le ponemos una URL de un libro azul
patron_img = r'<img src="[^"]*" alt="TutorIA Cuba Logo"[^>]*>'
nuevo_img = '<img src="https://cdn-icons-png.flaticon.com/512/3389/3389081.png" alt="TutorIA Cuba Logo" style="width: 80px; height: 80px; background: white; padding: 10px; border-radius: 50%; object-fit: contain;">'

html = re.sub(patron_img, nuevo_img, html)

# 2. Cambiar los datos de prueba para que parezcan reales
# Por ahora dejamos el nombre de Yosbel, pero cambiaremos el saldo a $ 15,000.00 para probar
html = html.replace('$0.00 CUP', '$15,000.00 CUP')

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Fachada actualizada con Logo y Saldo de prueba.")
