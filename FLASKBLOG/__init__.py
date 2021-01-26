from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY']='e95b70cb73d3e650884d944ce06fff25'
app.config['SQLAlCHEMY_DATABASE_URI'] ='sqlite:////home/denis/Desktop/flaskblog/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from FLASKBLOG import routes