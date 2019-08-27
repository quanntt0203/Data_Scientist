from flask import flash, session, request, render_template, redirect,url_for, Blueprint
#from app_init import app
from web.models import LoginModel as model

auth_controller = Blueprint('auth', __name__, url_prefix='/')

###
#
#
@auth_controller.route('/', methods=['GET'])
def home():
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/login')
    else:
        return render_template('/home/index.html')

###
#
#
@auth_controller.route('/login', methods=['POST','GET'])
def do_admin_login():
    logged_in = session.get('logged_in')
    if request.method == 'GET':
        if not logged_in:
            return render_template('login.html')

        elif logged_in:
            return redirect('/')

    else: # POST
        login_model = model(request.form['username'], request.form['password'])
        logged_in = (login_model.password == 'admin' and  login_model.username == 'admin')
        if logged_in:
            session['logged_in'] = logged_in

        else:
            flash('wrong password!')

        return redirect('/')

###
#
#
@auth_controller.route('/logout/', methods=['GET'])
def do_logout():
    session['logged_in'] = False
    return redirect('/login')