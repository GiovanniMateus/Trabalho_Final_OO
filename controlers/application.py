import json
import os
import uuid
from bottle import template, request, redirect, Bottle
from models.cadastro_usuario import CadastroUsuario

class Application:
    def __init__(self):
        self.pages = {
            'login': self.login,
            'menu': self.menu
        }
        self.__model = CadastroUsuario()
        self.__current_login_username = None

        # Caminhos para os bancos de dados
        self.usuarios_db = "controlers/database/usuarios.json"
        self.estoques_db = "controlers/database/estoques.json"
        self.sessoes_db = "controlers/database/sessoes.json"

    ### 🔹 FUNÇÕES AUXILIARES ###
    def carregar_dados(self, caminho):
        #Carrega dados do JSON especificado
        if not os.path.exists(caminho):
            return {} if caminho == self.sessoes_db else []
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_dados(self, caminho, dados):
        #Salva os dados no JSON especificado
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)

    ### 🔹 RENDERIZAÇÃO DE PÁGINAS ###
    def render(self, page, **kwargs):
        #Renderiza uma página com os argumentos fornecidos
        if page in self.pages:
            return self.pages[page](**kwargs)
        return template(f'views/html/{page}', **kwargs)

    ### 🔹 AUTENTICAÇÃO ###
    def login(self, mensagem=""):
        #Renderiza a página de login
        return template('views/html/login', mensagem=mensagem)

    def cadastrar_usuario(self, nome, senha):
        #Cadastra um novo usuário
        self.__model.add_users(nome, senha)

    def autenticar_usuario(self, nome, senha):
        """Verifica se o usuário existe e cria uma sessão"""
        if self.__model.check_users(nome, senha):
            session_id = str(uuid.uuid4())
            sessoes = self.carregar_dados(self.sessoes_db)
            sessoes[session_id] = nome
            self.salvar_dados(self.sessoes_db, sessoes)
            self.__current_login_username = nome
            return session_id
        return None  # Nome ou senha incorretos

    def verificar_sessao(self, session_id):
        """Verifica se o usuário está autenticado"""
        sessoes = self.carregar_dados(self.sessoes_db)
        return sessoes.get(session_id)

    def logout(self, session_id):
        """Realiza logout removendo a sessão do usuário"""
        sessoes = self.carregar_dados(self.sessoes_db)
        if session_id in sessoes:
            del sessoes[session_id]
            self.salvar_dados(self.sessoes_db, sessoes)
            self.__current_login_username = None

    ### 🔹 GERENCIAMENTO DE ESTOQUES ###
    def get_estoques(self, usuario):
        """Retorna a lista de estoques do usuário"""
        estoques = self.carregar_dados(self.estoques_db)
        return estoques.get(usuario, [])

    def adicionar_estoque(self, usuario):
        """Adiciona um novo estoque para o usuário logado"""
        estoques = self.carregar_dados(self.estoques_db)
        if usuario not in estoques:
            estoques[usuario] = []

        novo_estoque = {"id": len(estoques[usuario]) + 1, "nome": f"Estoque {len(estoques[usuario]) + 1}"}
        estoques[usuario].append(novo_estoque)

        self.salvar_dados(self.estoques_db, estoques)

    def remover_estoque(self, usuario, estoque_id):
        """Remove um estoque específico do usuário"""
        estoques = self.carregar_dados(self.estoques_db)
        if usuario in estoques:
            estoques[usuario] = [e for e in estoques[usuario] if str(e["id"]) != str(estoque_id)]
            self.salvar_dados(self.estoques_db, estoques)

    ### 🔹 PÁGINA MENU ###
    def menu(self):
        """Renderiza a página do menu"""
        if not self.__current_login_username:
            redirect('/login')
        estoques = self.get_estoques(self.__current_login_username)
        return template('views/html/menu', estoques=estoques, usuario=self.__current_login_username)
