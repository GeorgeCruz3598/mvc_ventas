#to renderize templates for user
from flask import render_template

#display all products rows-objects
def list(sales):
    return render_template('sales/index.html', sales =sales)  
        # products is the parent folder and not the url name to differentiate "index functions" of different BPs

# FORM create products 

#Unlike porducts and clients we must pass products and client tables in order to 
# display content of client and product in a selector (with sale table only have ids of products and clients) 

def create(clients,products):
    return render_template('sales/create.html',clients=clients, products=products)

# FORM Edit the selected product based on id (id of clicked Edit button row )
def edit(sale, clients, products):
    return render_template('sales/edit.html',sale=sale,clients=clients, products=products)