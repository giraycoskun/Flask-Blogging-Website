from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired 
from flask_login import login_user, logout_user
from repository.user import get_user_by_username

views = Blueprint(  'auth', __name__,
                    template_folder='../templates/auth')

class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = StringField(label='password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')


@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)

    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data) 
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('admin.index') 
            return redirect(next)
    flash('Invalid username or password.', category='error')
    return render_template('login.html', form=form)

@views.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('views.index'))