"""Memoria persistente del agente usando SQLite."""
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("/data/data/com.termux/files/home/tutoria-cuba/memoria.db")

def _conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def inicializar():
    with _conn() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS conversaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                agente TEXT NOT NULL,
                rol TEXT NOT NULL,
                mensaje TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        con.execute("""
            CREATE INDEX IF NOT EXISTS idx_user_agente
            ON conversaciones(user_id, agente, created_at DESC)
        """)
        con.commit()

def guardar(user_id, agente, rol, mensaje):
    inicializar()
    with _conn() as con:
        con.execute(
            "INSERT INTO conversaciones (user_id, agente, rol, mensaje) VALUES (?, ?, ?, ?)",
            (user_id, agente, rol, mensaje)
        )
        con.commit()

def historial(user_id, agente, limite=10):
    inicializar()
    with _conn() as con:
        rows = con.execute(
            """SELECT rol, mensaje, created_at FROM conversaciones
               WHERE user_id = ? AND agente = ?
               ORDER BY id DESC LIMIT ?""",
            (user_id, agente, limite)
        ).fetchall()
    return [dict(r) for r in reversed(rows)]

def borrar_historial(user_id, agente):
    inicializar()
    with _conn() as con:
        con.execute(
            "DELETE FROM conversaciones WHERE user_id = ? AND agente = ?",
            (user_id, agente)
        )
        con.commit()

def stats():
    inicializar()
    with _conn() as con:
        total = con.execute("SELECT COUNT(*) FROM conversaciones").fetchone()[0]
        usuarios = con.execute("SELECT COUNT(DISTINCT user_id) FROM conversaciones").fetchone()[0]
    return {"total_mensajes": total, "usuarios": usuarios}
