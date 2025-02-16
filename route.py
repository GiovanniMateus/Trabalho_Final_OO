from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response
from controlers.application import Application

app = Bottle()
ctl = Application()

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static/')

@app.route('/menu/<username>', methods = ['GET'])
def action_pagina(username=None):
    if not username:
        return ctl.render('menu')
    else:
        return ctl.render('menu',username)

@app.route('/login', method='GET')
def login():
    mensagem = request.query.mensagem or "" 
    return ctl.render('login',mensagem = mensagem)

@app.route('/login', method='POST')
def action_login():
    nome = request.forms.get('nome')
    senha = request.forms.get('senha')

    print(f"Nome recebido: '{nome}', Senha recebida: '{senha}'")  # Debug

    if ctl.authenticate_user(nome, senha):
        response.set_cookie("session_id", "algum_valor")  # Simula login
        redirect('/menu')
    else:
        return template('views/html/login', mensagem="Nome ou senha incorretos!")


    
@app.route('/cadastro', method ='POST')
def action_cadastro():
    nome = request.forms.get('nome')
    senha= request.forms.get('senha')
    
    if nome and senha:
        ctl.cadastrar_usuario(nome, senha)
        return ctl.render('login', mensagem = 'Cadastro realizado com sucesso')
    else:
        return ctl.render('login', mensagem = 'Preencha todos os campos')
    
@app.route('/menu', method=['GET','POST'])
def menu():
    session_id = request.get_cookie("session_id")
    if not session_id:
        redirect('/login')  # Se não estiver logado, redireciona para login
    return template('views/html/menu')

    
    
    
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)