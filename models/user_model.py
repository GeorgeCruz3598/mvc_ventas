from database import db  # import db object from SQLalchemy
from werkzeug.security import generate_password_hash, check_password_hash  # to protect passwords

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable = False)
    username = db.Column(db.String(20),nullable = False)
    passwd = db.Column(db.String,nullable = False)
    role = db.Column(db.String(20),nullable = False)
    
    def __init__(self,name,username,passwd,role):
        self.name = name
        self.username = username
        self.passwd = self.hash_passwd(passwd)
        self.role = role
        
    @staticmethod
    def hash_passwd(passwd):
        return generate_password_hash(passwd)
    
    #compare passwd attribute and a password entered by user
    def verify_passwd(self, passwd):
        return check_password_hash(self.passwd,passwd)
    
    #adicionar objeto de clase  Usuario en db  autoamtically al crear 
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    #recuperar todos los objetos = rows de table-clase usuario        
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    #Update Fields
    def update(self,name= None, username=None, passwd=None, role=None):
        if name:
            self.name = name
        if username:
            self.username = username
        if passwd:
            self.passwd = self.hash_passwd(passwd)
        if role:
            self.role = role
        db.session.commit()
        
    #delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()