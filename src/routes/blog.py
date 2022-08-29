from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

views = Blueprint(  'blog', __name__,
                    template_folder='../templates/')

@views.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@views.route('/blog')
def blog():
    try:
        return render_template('blog.html')
    except TemplateNotFound:
        abort(404)

@views.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except TemplateNotFound:
        abort(404)

@views.route('/post')
def post():
    try:
        return render_template('post.html')
    except TemplateNotFound:
        abort(404)
