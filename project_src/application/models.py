from google.appengine.ext import db

class Order(db.Model):
    title = db.StringProperty()
    weight = db.FloatProperty()
    token = db.StringProperty()