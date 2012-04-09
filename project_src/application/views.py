from flask import Response
from json import dumps

def json_response(values):
    '''This functions gets some list or dict and return in via WSGI in JSON format.'''
    return Response(dumps(values), mimetype='application/json')

def home():
    return json_response({'message': 'Hello, world!'})

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
    """
    return ''

