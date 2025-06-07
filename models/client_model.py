from database import db  # import db object from SQLalchemy

class Client(db.Model):
    __tablename__ = "clients"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable = False)
    email = db.Column(db.String(100),nullable = False)
    phone = db.Column(db.String(20),nullable = False)
    
    #specify type of relation with sales table~class
    sales_relation = db.relationship('Sale', back_populates = 'client_relation')
                                       #we use Classname 'Sale'
    
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    #adicionar objeto de clase  Usuario en db  autoamtically al crear 
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    #recuperar todos los objetos = rows de table-clase usuario        
    @staticmethod
    def get_all():
        return Client.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Client.query.get(id)
    
    #Update Fields
    def update(self,name= None, email=None, phone=None):
        if name and email and phone: # unlike users, all 3 fields must exist simultanoeusly
            self.name, self.email, self.phone = name, email, phone
        db.session.commit()
        
    #delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()