from bottle import template,request, redirect, Bottle
from models.cadastro_usuario import CadastroUsuario

class Application:
    def __init__(self):
        self.pages = {
            'login': self.login
            
        }
        self.__model = CadastroUsuario()
        self.__curent_loginusername = None
        
    def render(self,page,parameter=None):
        content = self.pages.get(page, self.login)
        if not parameter:
            return content()
        else:
            return content(parameter)
        
        
    def login(self):
        return template('views/html/login')
    
    def cadastrar_usuario(self,nome,senha):
        self.__model.add_users(nome, senha)