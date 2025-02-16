from bottle import template,request, redirect, Bottle
from models.cadastro_usuario import CadastroUsuario


class Application:
    def __init__(self):
        self.pages = {
            'login': self.login,
            'menu':self.menu
            
        }
        self.__model = CadastroUsuario()
        self.__curent_loginusername = None
        
    def render(self,page,**kwargs):
        if page in self.pages:
            return self.pages[page](**kwargs)  # Passa os argumentos para a função correspondente
        return template(f'views/html/{page}', **kwargs)
        
        
    def login(self, mensagem = ""):
        return template('views/html/login', mensagem = mensagem)
    
    def cadastrar_usuario(self,nome,senha):
        self.__model.add_users(nome, senha)
        
    def authenticate_user(self, nome, senha):
        return self.__model.check_users(nome, senha)
    
    def menu(self):
        return template('views/html/menu')
    
    