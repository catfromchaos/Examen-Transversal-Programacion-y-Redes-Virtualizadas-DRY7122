from flask import Flask, render_template_string, request
import sqlite3
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key = "clave_secreta_examen"

DB_NAME = 'usuarios_examen.db'


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()S
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            fecha_registro TEXT
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_integrantes():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    integrantes = [
        ("Amanda Gajardo", "Examen123"),
    ]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for nombre, password in integrantes:
        password_hash = hash_password(password)
        cursor.execute("INSERT OR REPLACE INTO usuarios (nombre, password_hash, fecha_registro) VALUES (?, ?, ?)",
                       (nombre, password_hash, fecha))
        print(f"Usuario registrado: {nombre}")

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return """
    <h1>Sistema de Autenticación - Examen Transversal</h1>
    <p><a href="/login">Iniciar Sesión</a></p>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        password_hash = hash_password(password)

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM usuarios WHERE nombre = ? AND password_hash = ?", 
                      (usuario, password_hash))
        result = cursor.fetchone()
        conn.close()

        if result:
            return f"<h2>¡Acceso Correcto! Bienvenido/a, {usuario}</h2><p><a href='/'>Volver</a></p>"
        else:
            return "<h3>Usuario o contraseña incorrecta</h3><a href='/login'>Volver</a>"

    return '''
        <h2>Iniciar Sesión</h2>
        <form method="post">
            Usuario: <input type="text" name="usuario" required><br><br>
            Contraseña: <input type="password" name="password" required><br><br>
            <input type="submit" value="Ingresar">
        </form>
    '''

if __name__ == '__main__':
    registrar_integrantes()
    print("Base de datos creada y usuarios registrados.")
    print("Servidor web disponible en: http://127.0.0.1:5800")
    app.run(port=5800, debug=True)