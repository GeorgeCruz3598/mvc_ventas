# Act as he link between View-presentatio and Model(what & how data will be stored)
# cONTROLLER -> extract data from  model provide data to view, Update-MOdify-delete data,
#            -> brain, operations, interaction between M-V
from flask import request, redirect, url_for, Blueprint

from models.client_model import Client #Model-> data
from views import client_view  #view

client_bp = Blueprint('client',__name__,url_prefix="/clients") # for user_bp ->  "127.0.0.1/" is mapped as "127.0.0.1/users"

#Display
@client_bp.route("/")
def index():
    #recuper todos los registros DE client de model
    clients = Client.get_all()
    return client_view.list(clients) #envia a vista para presentacion

#client/create
@client_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
    
        #Create object
        client = Client(name,email,phone)
        client.save() #save
        
        return redirect(url_for('client.index')) # / = /user para user_bp
    
    return client_view.create()

#client/edit
@client_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    client = Client.get_by_id(id)  
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        client.update(name=name,email=email, phone=phone)
        return redirect(url_for('client.index')) # / = /user redirect al index de user_bp
    
    return client_view.edit(client)

#client/delete
@client_bp.route("/delete/<int:id>")
def delete(id):
    client = Client.get_by_id(id)  
    client.delete()
    return redirect(url_for('client.index'))