from geral.config import *

class Pessoa(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)
    nmrCasa = db.Column(db.Text)
    cep = db.Column(db.Text)

    
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone + ", " + self.cep + ", " + self.nmrCasa 
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "cep": self.cep,
            "nmrCasa" : self.nmrCasa,

        }

