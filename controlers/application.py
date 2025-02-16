import json
import os
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
        self.db_path = "controlers/database/estoques.json"
        
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
    
    def carregar_dados(self):
        if not os.path.exists(self.db_path):
            return {}
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def salvar_dados(self, dados):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)

    def get_estoques(self, usuario_id):
        dados = self.carregar_dados()
        return dados.get(usuario_id, [])
    
    def adicionar_estoque(self, usuario_id):
        dados = self.carregar_dados()
        if usuario_id not in dados:
            dados[usuario_id] = []
        
        novo_estoque = {"id": len(dados[usuario_id]) + 1, "nome": f"Estoque {len(dados[usuario_id]) + 1}"}
        dados[usuario_id].append(novo_estoque)

        self.salvar_dados(dados)

    def remover_estoque(self, usuario_id, estoque_id):
        dados = self.carregar_dados()
        if usuario_id in dados:
            dados[usuario_id] = [e for e in dados[usuario_id] if str(e["id"]) != str(estoque_id)]
            self.salvar_dados(dados)