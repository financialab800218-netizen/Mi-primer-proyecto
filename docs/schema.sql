-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    telegram_id TEXT UNIQUE,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE,
    rol TEXT NOT NULL DEFAULT 'alumno',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla de TCP
CREATE TABLE IF NOT EXISTS tcp_perfiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id UUID REFERENCES usuarios(id),
    codigo_tcp TEXT UNIQUE NOT NULL,
    cedula TEXT NOT NULL,
    especialidad TEXT,
    categoria TEXT DEFAULT 'bronce',
    validado BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla de contenido
CREATE TABLE IF NOT EXISTS contenido (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    creador_id TEXT NOT NULL,
    creador_tipo TEXT NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    tipo TEXT NOT NULL,
    url TEXT NOT NULL,
    tamaño_bytes BIGINT,
    materia TEXT,
    nivel TEXT,
    idioma TEXT DEFAULT 'es',
    estado TEXT DEFAULT 'borrador',
    validado_ia BOOLEAN DEFAULT FALSE,
    validado_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);