from flask import render_template

from application import app
from application import views


app.add_url_rule('/', view_func=views.home, methods=['GET',]) # Main page
app.add_url_rule('/drug/orders/', view_func=views.add_order, methods=['POST',])
app.add_url_rule('/drug/orders/', view_func=views.get_order, methods=['GET',])
app.add_url_rule('/drug/orders/', view_func=views.delete_order, methods=['DELETE',])

## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

