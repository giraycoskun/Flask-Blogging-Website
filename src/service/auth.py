from functools import wraps
from flask_login import LoginManager, current_user
from flask import flash, redirect, url_for

login_manager = LoginManager()
login_manager.login_view = 'views.auth.login'

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role == "admin":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.", 'error')
            return redirect(url_for('views.index'))
    return wrap