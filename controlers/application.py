from bottle import template,request, redirect, Bottle

class Application:
    def __init__(self):
        self.pages = {
            'login': self.login
            
        }
        
    def login(self):
        return template('app/views/html/portal')