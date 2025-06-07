#MODEL -> Associated to DATA DEfine what types of data, HOw it will be stored, operations over data 
    #data structure, DB -> bussines logic
from sqlalchemy import Nullable
from database import db  # import db object from SQLalchemy

class Sale(db.Model):
    __tablename__ = "sales"
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable = False)
    client_id = db.Column(db.Integer,db.ForeignKey('clients.id'), nullable = False) #reference to table_name + field
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'), nullable = False) 
    quantity = db.Column(db.Integer,nullable = False) 
    
    ##sspecify types of relations: 1:n(client-sales) n:n(product-sales), 1:1, n:1
    # This specification must be added to clients, products models~ data
    client_relation = db.relationship('Client', back_populates = 'sales_relation')
    product_relation = db.relationship('Product', back_populates = 'sales_relation')
    
    def __init__(self,date, client_id, product_id,quantity): #builder o constructor
        self.date = date
        self.client_id = client_id
        self.product_id = product_id
        self.quantity = quantity
        
    #adicionar objeto de clase  Usuario en db  autoamtically al crear 
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    #recuperar todos los objetos = rows de table-clase usuario        
    @staticmethod
    def get_all():
        return Sale.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Sale.query.get(id)
    
    #Update Fields
    def update(self, date= None, client_id=None, product_id=None, quantity= None):
        if date and client_id and product_id and quantity: # unlike users, all 3 fields must exist simultanoeusly
            self.date, self.client_id, self.product_id, self.quantity = date, client_id, product_id, quantity
        db.session.commit()
        
    #delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()