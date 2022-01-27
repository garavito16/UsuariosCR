

from flask import render_template,redirect, request
from proyecto.modelos.modelo_usuario import Usuario
from proyecto import app

@app.route('/',methods=['GET'])
def initial():
    listaUsuarios = Usuario.listarUsuarios()
    return render_template('index.html',lista=listaUsuarios)

@app.route('/create_user',methods=["GET"])
def render_create_user():
    return render_template('create.html')

@app.route('/create_user',methods=["POST"])
def create_user():
    usuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "correo_electronico" : request.form["correo_electronico"]
    }
    id = Usuario.agregarUsuario(usuario)
    if(id > 0):
        return redirect('/')