# Act as he link between View-presentatio and Model(what & how data will be stored)
# cONTROLLER -> extract data from  model provide data to view, Update-MOdify-delete data,
#            -> brain, operations, interaction between M-V
from flask import request, redirect, url_for, Blueprint

from models.user_model import User #Model-> data
from views import user_view  #view

user_bp = Blueprint('user',__name__,url_prefix="/users") # for user_bp ->  "127.0.0.1/" is mapped as "127.0.0.1/users"
@user_bp.route("/")
def index():
    #recuper todos los registros DE User de model
    users = User.get_all()
    return user_view.list(users) #envia a vista para presentacion

#user/create
@user_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        passwd = request.form['passwd']
        role = request.form['role']       
        
        #Create object
        user = User(name,username,passwd,role)
        user.save() #save
        
        return redirect(url_for('user.index')) # / = /user para user_bp
    
    return user_view.create()

#user/edit
@user_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    user = User.get_by_id(id)  
    if request.method=='POST':
        name = request.form['name']
        username = request.form['username']
        passwd = request.form['passwd']
        role = request.form['role']       
        
        user.update(name=name,username=username,passwd=passwd,role=role)
        return redirect(url_for('user.index')) # / = /user redirect al index de user_bp
    
    return user_view.edit(user)

#user/delete
@user_bp.route("/delete/<int:id>")
def delete(id):
    user = User.get_by_id(id)  
    user.delete()
    return redirect(url_for('user.index'))