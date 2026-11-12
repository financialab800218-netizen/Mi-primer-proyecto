from contabilidad import supabase

print("🏗️ Creando la tabla de 'profesores' en Supabase...")

# Nota: Supabase no permite crear tablas por código Python directamente por seguridad,
# así que ejecutaremos una consulta SQL vía RPC o usaremos el cliente.
# Para este caso, asumimos que ejecutaremos un SQL en el panel de Supabase.
# Pero te dejo el código de cómo se insertaría un profesor de prueba.

profesor_prueba = {
    "nombre": "Yosbel Collazo",
    "email": "yosbel@tutoria.cu",
    "telefono": "+5353755025",
    "especialidad": "Matemáticas y Contabilidad",
    "saldo_cup": 0.00,
    "nivel": "Bronce" # El nivel que desbloquea QvaPay será "Diamante"
}

try:
    # Intentamos insertar en una tabla (si ya existe)
    response = supabase.table('profesores').insert(profesor_prueba).execute()
    print("✅ Profesor de prueba insertado con éxito.")
except Exception as e:
    print("⚠️ La tabla 'profesores' no existe o hay un error.")
    print("👉 ACCIÓN REQUERIDA: Ve a tu panel de Supabase -> SQL Editor y ejecuta esto:")
    print("""
    CREATE TABLE profesores (
        id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT,
        especialidad TEXT,
        saldo_cup NUMERIC DEFAULT 0.00,
        nivel TEXT DEFAULT 'Bronce',
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    """)
