from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound

views = Blueprint(  'views', __name__)

from routes.blog import views as blog_views
from routes.auth import views as auth_views

views.register_blueprint(blog_views)
views.register_blueprint(auth_views)

@views.route('/')
def root():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@views.route('/index')
def index():
    try:
        return redirect(url_for('views.root'))
    except TemplateNotFound:
        abort(404)
        