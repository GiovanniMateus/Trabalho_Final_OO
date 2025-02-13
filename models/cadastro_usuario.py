import json
import os
import uuid

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
            
    def check_users(self, nome, senha):
        for user in self.user:
            if user ['nome'] == nome and user ['senha'] == senha:
                session_id = str(uuid.uuid4())
                self.authenticated_users[session_id] = user
                return session_id
        return None
    
    def get_current_user(self, session_id):
        return self.authenticated_users.get(session_id, None)

    def get_user_name(self, session_id):
        user = self.get_current_user(session_id)
        return user['nome'] if user else None

    def get_user_session_id(self, nome):
        for session_id, user in self.authenticated_users.items():
            if user['nome'] == nome:
                return session_id
        return None

    def logout(self, session_id):
        if session_id in self.authenticated_users:
            del self.authenticated_users[session_id]