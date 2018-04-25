from datetime import datetime
from flask import Flask, session, g, render_template

app = Flask(__name__)
app.config.from_object('websiteconfig')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.context_processor
def current_year():
    return {'current_year': datetime.utcnow().year}


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


app.add_url_rule('/charts', endpoint='charts', view_func=app.send_static_file)

from flask_website.views import general
app.register_blueprint(general.mod)

from flask_website import utils

app.jinja_env.filters['datetimeformat'] = utils.format_datetime
app.jinja_env.filters['dateformat'] = utils.format_date
app.jinja_env.filters['timedeltaformat'] = utils.format_timedelta
app.jinja_env.filters['displayopenid'] = utils.display_openid
