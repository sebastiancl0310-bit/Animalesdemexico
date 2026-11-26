import sqlite3
import hashlib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Función para inicializar la base de datos SQLite
def init_db():
    conn = sqlite3.connect('selva.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            edad INTEGER NOT NULL,
            animal_favorito TEXT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Ruta principal: Carga el formulario HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para procesar el registro (recibe los datos del formulario)
@app.route('/registrar', methods=['POST'])
def registrar():
    # Obtenemos los datos enviados por FormData desde JavaScript
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    edad = request.form.get('edad')
    animal = request.form.get('animal')

    # Encriptar la contraseña por seguridad (Hash SHA-256)
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        conn = sqlite3.connect('selva.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nombre, email, password, edad, animal_favorito)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, email, password_hash, edad, animal))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success", "mensaje": "¡Registro guardado con éxito!"})
    
    except sqlite3.IntegrityError:
        return jsonify({"status": "error", "mensaje": "El correo electrónico ya está registrado."}), 400

if __name__ == '__main__':
    init_db()  # Creamos la BD al arrancar
    app.run(debug=True)