from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from repository import db
from repository.user import User
from repository.post import Post

class MyHomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('views.auth.login'))

class UserModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('views.auth.login'))

class PostModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('views.auth.login'))

admin = Admin(name='flask-blog', template_mode='bootstrap4', index_view=MyHomeView())
admin.add_view(UserModelView(User, db.session))
admin.add_view(PostModelView(Post, db.session))
