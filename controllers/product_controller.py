# Act as he link between View-presentatio and Model(what & how data will be stored)
# cONTROLLER -> extract data from  model provide data to view, provide the Updated-MOdified-deleted data in view to model,
#            -> brain, operations, interaction between M-V

from flask import request, redirect, url_for, Blueprint

from models.product_model import Product #Model-> data
from views import product_view  #view

product_bp = Blueprint('product',__name__, url_prefix="/products") # for user_bp ->  "127.0.0.1/" is mapped as "127.0.0.1/products"

#Display
@product_bp.route("/")
def index():
    #recuper todos los registros DE client de model
    products = Product.get_all()
    return product_view.list(products) #envia a vista para presentacion

#product/create
@product_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        #Create object to store in model
        product = Product(description,price,stock)
        product.save() #save
        
        return redirect(url_for('product.index')) # / = /user para user_bp
    
    return product_view.create()

#product/edit
@product_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    product = Product.get_by_id(id)  
    if request.method=='POST':
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        product.update(description=description,price=price, stock=stock)
        return redirect(url_for('product.index')) # / = /user redirect al index de user_bp

    return product_view.edit(product) #the form will be showed while not click on button

#product/delete
@product_bp.route("/delete/<int:id>")
def delete(id):
    product = Product.get_by_id(id)  
    product.delete()
    return redirect(url_for('product.index'))