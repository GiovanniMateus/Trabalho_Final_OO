import json
import os

class CadastroUsuario():
    def __init__(self, arquivo = 'controlers/database/usuarios.json'):
        self.arquivo = arquivo
        self.user = self.load_users()
        
    def load_users(self):
        try:
            with open(self.arquivo , 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def add_users(self, nome, senha):
        new_users = ({'nome': nome, 'senha': senha})
        self.user.append(new_users)
        self.save_users()
        
    def save_users(self):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok= True)
        
        with open (self.arquivo, 'w') as f:
            json.dump(self.user, f, indent=4)
            