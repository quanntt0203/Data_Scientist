from flask import session, redirect
from flask_restful import Resource, Api
#from flask_login import login_required

class ApiBase(Resource):
    def __init__(self):
        pass

    def check_auth(self) -> bool:
        logged_in = session.get('logged_in')
        return logged_in


#@api.resource('/',
#              '/hello')
class HelloWord(ApiBase):

    def __init__(self):
        pass

    #@login_required
    def get(self):
        if not super().check_auth():
            return redirect('/')

        return {'hello': 'word'}

def add_resources(app) -> Api:
    api = Api(app)
    api.add_resource(HelloWord, '/api/hello')

    return api