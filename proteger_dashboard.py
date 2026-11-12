ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'
with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inyectar el script de protección justo antes de </body>
script_proteccion = '''
<script>
    const usuario = JSON.parse(localStorage.getItem('usuario_tutoria'));
    if (!usuario) {
        window.location.href = 'login.html'; // Si no hay sesión, lo manda al login
    } else {
        // Si hay sesión, actualizamos el nombre y el saldo en la página
        document.querySelector('.saldo').innerText = `$${usuario.saldo_cup.toFixed(2)} CUP`;
        const saludo = document.querySelector('.card p');
        if(saludo) saludo.innerHTML = `Hola, <strong>${usuario.nombre}</strong>`;
    }
</script>
</body>
'''
html = html.replace('</body>', script_proteccion)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ Dashboard protegido y dinámico.")
