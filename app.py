from flask import Flask

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# import config file
app.config.from_pyfile('config.cfg')

# create db obj with SQLalchemy and pass it app
db = SQLAlchemy(app)

# create first table with sqlAlchemy
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
