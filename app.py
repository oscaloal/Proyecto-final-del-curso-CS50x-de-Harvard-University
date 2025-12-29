import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from helpers import apology, login_required
# Configure application
app = Flask(__name__)

#Cambiar a una clave larga y random para seguridad cuando vaya a publicarla
app.secret_key = "clave_secreta"

#Base de datos
db = SQL("sqlite:///usuarios.db")

#Primera página, la inicial.
@app.route("/")
def index():
    return render_template("index.html")

#Segunda página, para los eventos.
@app.route("/eventos")
def eventos():

    lista_eventos = db.execute("""
        SELECT eventos.*, usuarios.usuario
        FROM eventos
        JOIN usuarios ON eventos.usuario_id = usuarios.id
        ORDER BY fecha DESC
    """)

    hoy = datetime.now()
    dias_semana = [
        "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"
    ]
    meses =[
        "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]

    dia_semana = dias_semana[hoy.weekday()]
    dia = hoy.day
    mes = meses[hoy.month - 1]
    año = hoy.year

    fecha_hoy = f"{dia_semana}, {dia} de {mes} de {año}"
    return render_template(
        "eventos.html",
        hoy =fecha_hoy,
        eventos =lista_eventos
    )

#Para Log In, imitado de Finance
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Debe añadir usuario", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Debe añadir contraseña", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM usuarios WHERE usuario = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password_hash"], request.form.get("password")
        ):
            return apology("Usuario y/o Contraseña incorrectos", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

#Para Log Out, copiado de Finance
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/registro", methods=["GET", "POST"])
def registro():

    session.clear()
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not usuario:
            return apology("Debe añadir usuario", 400)
        if not password:
            return apology("Debe añadir contraseña", 400)
        if password != confirmation:
            return apology("Las contraseñas no coinciden", 400)

        rows = db.execute("SELECT * FROM usuarios WHERE usuario = ?", usuario)
        if len(rows) != 0:
            return apology("El usuario ya existe", 400)

        user_id = db.execute(
            "INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)",
            usuario,
            generate_password_hash(password)
        )

        session["user_id"] = user_id

        return redirect("/")

    else:
        return render_template("registro.html")

#Acceder a mi perfil
@app.route("/miperfil")
@login_required
def miperfil():
    return render_template("miperfil.html")

@app.route("/changepassword", methods=["POST"])
@login_required
def changepassword():

    current = request.form.get("current")
    new = request.form.get("new")
    confirmation = request.form.get("confirmation")

    # Verificar contraseñas iguales
    if new != confirmation:
        return apology("Las contraseñas no coinciden", 400)

    # Obtener contraseña actual del usuario
    row = db.execute("SELECT * FROM usuarios WHERE id = ?", session["user_id"])[0]

    # Comprobar contraseña actual
    if not check_password_hash(row["password_hash"], current):
        return apology("La contraseña actual es incorrecta", 400)

    # Actualizar contraseña
    db.execute(
        "UPDATE usuarios SET password_hash = ? WHERE id = ?",
        generate_password_hash(new), session["user_id"]
    )

    flash("Contraseña cambiada correctamente")
    return redirect("/miperfil")

@app.route("/crear_evento", methods=["POST"])
@login_required
def crear_evento():
    titulo = request.form.get("titulo")
    fecha = request.form.get("fecha")
    descripcion = request.form.get("descripcion")

    if not titulo or not fecha:
        return apology("Debe rellenar título y fecha", 400)

    db.execute(
        "INSERT INTO eventos (usuario_id, titulo, fecha, descripcion) VALUES (?, ?, ?, ?)",
        session["user_id"], titulo, fecha, descripcion
    )

    flash("Evento creado correctamente")
    return redirect("/eventos")

@app.route("/crear_propuesta", methods=["POST"])
@login_required
def crear_propuesta():

    titulo = request.form.get("titulo")
    contenido = request.form.get("contenido")

    if not titulo or not contenido:
        return apology("Debe rellenar todos los campos", 400)

    db.execute(
        "INSERT INTO propuestas (usuario_id, titulo, contenido) VALUES (?, ?, ?)",
        session["user_id"], titulo, contenido
    )

    flash("Propuesta enviada correctamente")
    return redirect("/propuestas")

@app.route("/propuestas")
def propuestas():
    lista_propuestas = db.execute("""
        SELECT propuestas.*, usuarios.usuario
        FROM propuestas
        JOIN usuarios ON propuestas.usuario_id = usuarios.id
        ORDER BY fecha DESC
    """)
    return render_template("propuestas.html", propuestas = lista_propuestas)

@app.route("/noticias")
def noticias():
    return apology("Esta página esta en construcción", 503)

@app.route("/contacto")
def contacto():
    return apology("Esta página esta en construcción", 503)
