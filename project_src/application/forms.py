from flaskext import wtf
from flaskext.wtf import validators

class NewOrderForm(wtf.Form):
    title = wtf.TextField('title', validators=[validators.Required()])
    weight = wtf.TextField('weight', validators=[validators.Required()])
