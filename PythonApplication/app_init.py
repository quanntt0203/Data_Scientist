from flask import Flask
import settings

app = Flask(__name__)
app.config['ENV'] = settings.APP_ENV

app.template_folder = 'web/views'
#app.static_folder = 'web/static'