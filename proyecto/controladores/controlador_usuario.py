

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

@app.route('/ver_usuario/<id>',methods=["GET"])
def mostrar_usuario(id):
    usuario = {
        "id" : id
    }
    result = Usuario.mostrarUsuario(usuario)
    return render_template('mostrar.html',usuario=result)

@app.route('/editar_usuario/<id>',methods=["GET"])
def ver_editar_usuario(id):
    usuario = {
        "id" : id
    }
    result = Usuario.mostrarUsuario(usuario)
    return render_template('edit.html',usuario=result)

@app.route('/editar_usuario/<id>',methods=["POST"])
def editar_usuario(id):
    usuario = {
        "id" : id,
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "correo_electronico" : request.form["correo_electronico"]
    }
    result = Usuario.editarUsuario(usuario)
    return redirect('/ver_usuario/'+str(id))

@app.route('/eliminar_usuario/<id>')
def eliminar_usuario(id):
    usuario = {
        "id" : id
    }
    result = Usuario.eliminarUsuario(usuario)
    print(result)
    return redirect('/')