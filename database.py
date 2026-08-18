import sqlite3

def conectar():
    return sqlite3.connect("data/memory.db")

def crear_tabla():
    conexion = conectar()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            importance TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

from datetime import datetime

def guardar_recuerdo(content, importance):
    conexion = conectar()

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conexion.execute(
        """
        INSERT INTO memories (content, importance, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """,
        (content, importance, fecha_actual, fecha_actual)
    )

    conexion.commit()
    conexion.close()

def obtener_recuerdos():
    conexion = conectar()

    cursor = conexion.execute(
        """
        SELECT id, content, importance, created_at, updated_at
        FROM memories
        """
    )

    recuerdos = cursor.fetchall()

    conexion.close()

    return recuerdos

def buscar_recuerdos(termino):
    conexion = conectar()

    cursor = conexion.execute(
        """
        SELECT content
        FROM memories
        WHERE content LIKE ?
        """,
        (f"%{termino}%",)
    )

    recuerdos = cursor.fetchall()

    conexion.close()

    return recuerdos