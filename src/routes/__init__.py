from flask import Blueprint, render_template, abort, redirect, url_for, current_app
from jinja2 import TemplateNotFound

views = Blueprint(  'views', __name__)

from routes.blog import views as blog_views
from routes.auth import views as auth_views
from routes.blogger import init_blog_views

views.register_blueprint(blog_views)
views.register_blueprint(auth_views)
init_blog_views()

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

@views.route('/test')
def test():
    try:
        return render_template('test.html')
    except TemplateNotFound:
        abort(404)

@views.route("/site-map")
def site_map():
    site_map = {}
    for rule in current_app.url_map.iter_rules():
        current_app.logger.info(rule)
        site_map[rule.rule] = rule.endpoint
    return site_map