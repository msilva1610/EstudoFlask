from my_app import db
 
class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    company = db.Column(db.String(255))
 
    def __init__(self, name, gender, company):
        self.name = name
        self.gender = gender
        self.company = company
 
    def __repr__(self):
        return '<Clientes %d>' % self.id