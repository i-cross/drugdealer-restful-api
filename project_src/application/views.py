from flask import Response, request
from json import dumps
from forms import NewOrderForm
from models import Order
import uuid

def json_response(values):
    '''This functions gets some list or dict and return in via WSGI in JSON format.'''
    return Response(dumps(values), mimetype='application/json')

def home():
    return json_response({'message': 'Hello, world!'})

def add_order():
    form = NewOrderForm()

    if form.title.data != "":
        drug_title = form.title.data
    else: return json_response({'error': 'Drug title is empty'})

    if form.weight.data != "":
        drug_weight = form.weight.data
    else: return json_response({'error': 'Drug weight is empty'})

    token = str(uuid.uuid4())

    order = Order(title = drug_title, weight = float(drug_weight), token = token)
    order.put()

    return json_response({
        'id': int(order.key().id()),
        'token': token,
        'success': True
    })

def get_order():
    token = request.args.get('token')
    if token is None:
        return json_response({'error': 'Token is empty'})

    order = Order.all().filter('token = ', token).fetch(1)
    if len(order) is 1:
        return json_response(order[0]._entity)
    else: return json_response({'error': 'Access denied'})


def delete_order():
    token = request.args.get('token')
    if token is None:
        return json_response({'error': 'Token is empty'})

    order = Order.all().filter('token = ', token).fetch(1)
    if len(order) is 1:
        order = order[0]
        order.delete()
        return json_response({'success': True})
    else: return json_response({'error': 'Access denied'})

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
    """
    return ''

