import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.clientes.models import Clientes
 
clientes = Blueprint('clientes', __name__)
 
@clientes.route('/')
@clientes.route('/home')
def home():
    return "Welcome to the clientes Home api."
 
 
class ClientesView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            clientes = Clientes.query.paginate(page, 100).items
            res = {}
            for cliente in clientes:
                res[cliente.id] = {
                    'name': cliente.name,
                    'gender': str(cliente.gender),
                    'company': str(cliente.company),
                }
        else:
            cliente = Clientes.query.filter_by(id=id).first()
            if not cliente:
                abort(404)
            res = {
                'name': cliente.name,
                'gender': str(cliente.gender),
                'company': str(cliente.company),
            }
        return jsonify(res)
 
    def post(self):
        name = request.form.get('name')
        gender = request.form.get('gender')
        company = request.form.get('company')
        cliente = Clientes(name, gender, company)
        db.session.add(cliente)
        db.session.commit()
        return jsonify({cliente.id: {
            'name': cliente.name,
            'gender': str(cliente.gender),
            'company': str(cliente.company),
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
clientes_view =  ClientesView.as_view('clientes_view')
app.add_url_rule(
    '/cliente/', view_func=clientes_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/cliente/<int:id>', view_func=clientes_view, methods=['GET']
)