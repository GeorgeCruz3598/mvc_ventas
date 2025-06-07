from flask import Flask, redirect, render_template, request, url_for
from database import db # import orm sqlachemy obejt 'db'

#import BP
from controllers import user_controller, client_controller, product_controller, sale_controller


app = Flask(__name__)

#SQLAlchemy configurtaions
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#init object db
db.init_app(app)

#define/register BP -> all routes of user_controller are available in run .py
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(client_controller.client_bp)
app.register_blueprint(product_controller.product_bp)
app.register_blueprint(sale_controller.sale_bp)

#para resaltar el modulo seleccionado "active"
#Si la ruta actual (requested) == ruta como parametro entonces:
@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active = is_active)) 

@app.route("/")
def home():
    return redirect(url_for('user.index'))

if __name__=="__main__":
    with app.app_context():  #init db creation with sqlachemy as class~table
        db.create_all()
    app.run(debug=True)