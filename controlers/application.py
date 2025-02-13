from bottle import template,request, redirect, Bottle
from models.cadastro_usuario import CadastroUsuario

class Application:
    def __init__(self):
        self.pages = {
            'login': self.login
            
        }
        self.__model = CadastroUsuario()
        self.__curent_loginusername = None
        
    def login(self):
        return template('app/views/html/login')