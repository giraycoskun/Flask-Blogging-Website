from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_login import login_required
from flask_admin import BaseView, expose
from flask_login import current_user
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from service.auth import admin_required
from routes.admin import admin

class BlogEditorForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    text = TextAreaField("text", validators=[DataRequired()])
    tags = StringField("tags", validators=[DataRequired()])
    draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")


class BlogView(BaseView):
    @expose('/')
    def index(self):
        return render_template('blog/index.html')

    @expose('/editor')
    def editor(self):
        form = BlogEditorForm()
        return render_template('blog/editor.html', form=form)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('views.auth.login'))

def init_blog_views():
    admin.add_view(BlogView(name='Blog-Editor', url='blogger'))
