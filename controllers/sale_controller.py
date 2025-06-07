# Act as he link between View-presentatio and Model(what & how data will be stored)
# cONTROLLER -> extract data from  model provide data to view, provide the Updated-MOdified-deleted data in view to model,
#            -> brain, operations, interaction between M-V

from flask import request, redirect, url_for, Blueprint

from models.product_model import Product #Model-> data
from models.client_model import Client 
from models.sale_model import Sale 

from views import sale_view

from datetime import datetime #ro format date y-m-d

sale_bp = Blueprint('sale',__name__, url_prefix="/sales") # for user_bp ->  "127.0.0.1/" is mapped as "127.0.0.1/sales"

#Display
@sale_bp.route("/") #it will be showed -> /sales + / -> /sales/
def index():
    #recuper todos los registros DE ventas de model
    sales = Sale.get_all()
    return sale_view.list(sales) #envia a vista para presentacion

#sales/create
@sale_bp.route("/create",methods=['GET','POST']) #/sales + /create -> /sales/create
def create():
    if request.method == 'POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str,"%Y-%m-%d").date()
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        
        #Create object to store in model
        sale = Sale(date=date,client_id=client_id, product_id=product_id,quantity=quantity)
        sale.save() #save
        
        return redirect(url_for('sale.index')) # / = /user para user_bp
    
    #addtionally we must send the clients and products to display in selector
    clients =  Client.get_all()    
    products =  Product.get_all()
    
    return sale_view.create(clients, products)

#product/edit
@sale_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    sale = Sale.get_by_id(id)  
    if request.method=='POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str,"%Y-%m-%d").date()
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']

        sale.update(date=date,client_id=client_id, product_id=product_id,quantity=quantity)
        return redirect(url_for('sale.index')) # / = /user redirect al index de user_bp

    #addtionally we must send the clients and products to display in selector
    clients =  Client.get_all()    
    products =  Product.get_all()

    return sale_view.edit(sale, clients, products) #the form will be showed while not click on button

#product/delete
@sale_bp.route("/delete/<int:id>")
def delete(id):
    sale = Sale.get_by_id(id)  
    sale.delete()
    return redirect(url_for('sale.index'))