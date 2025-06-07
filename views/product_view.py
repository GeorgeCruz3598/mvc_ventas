#to renderize templates for user
from flask import render_template

#display all products rows-objects
def list(products):
    return render_template('products/index.html', products =products)  
        # products is the parent folder and not the url name to differentiate "index functions" of different BPs

# FORM create products 
def create():
    return render_template('products/create.html')

# FORM Edit the selected product based on id (id of clicked Edit button row )
def edit(product):
    return render_template('products/edit.html',product=product)