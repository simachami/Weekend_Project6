from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user, login_required
from . import bp as auth
from app.forms import LoginForm, SignUpForm
from app.models import User

@auth.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    signin_form = LoginForm()
    if signin_form.validate_on_submit():
        email = signin_form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(signin_form.password.data):
            login_user(user)
            flash(f'{signin_form.email.data} successfully logged in!' ,category='success')
            return redirect('/')
        else:
            flash(f'Invalid User Info, Please try again!', category='danger')
    return render_template('signin.jinja', form=signin_form)


@auth.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('auth.sign_in'))



@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SignUpForm()
    if form.validate_on_submit():
        user_info = {
            'first_name' : form.first_name.data,
            'last_name' : form.last_name.data,
            'username' : form.username.data,
            'email' : form.email.data,
        }
        try:
            user = User()
            user.from_dict(user_info)
            user.hash_password(form.password.data)
            user.commit()
            flash(f'{user.first_name if user.first_name else user.username} is registered', category='success')
            login_user(user)
            return redirect('/')
        except:
            flash(f'Username or Email is already taken. Please try again!', category='danger')
    return render_template('signup.jinja', form=form)
