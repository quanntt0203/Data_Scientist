import os
from app_init import app
from web.controllers import auth
from api import flask_api as api

app.register_blueprint(auth.auth_controller)

# add app api resources
api.add_resources(app)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)