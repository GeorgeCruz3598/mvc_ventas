#MODEL -> Associated to DATA DEfine what types of data, HOw it will be stored, operations over data

from database import db  # import db object from SQLalchemy

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120),nullable = False)
    price = db.Column(db.Float(11,2),nullable = False) #define float de 11 digitos maximo y 2 decimales
    stock = db.Column(db.Integer,nullable = False) 
    
    #specify type of relation with "sales" table~ class
    sales_relation = db.relationship('Sale',back_populates='product_relation') #ojito
    
    
    def __init__(self,description,price,stock): #builder o constructor
        self.description = description
        self.price = price
        self.stock = stock
        
    #adicionar objeto de clase  Usuario en db  autoamtically al crear 
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    #recuperar todos los objetos = rows de table-clase usuario        
    @staticmethod
    def get_all():
        return Product.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)
    
    #Update Fields
    def update(self,description= None, price=None, stock=None):
        if description and price and stock: # unlike users, all 3 fields must exist simultanoeusly
            self.description, self.price, self.stock = description, price, stock
        db.session.commit()
        
    #delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()