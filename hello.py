from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app = Flask(__name__)

app.route('/')
def index():
    return '<h1> Hello World <h1>'
    
# Run server
    if __name__ == '__main__':
         app.run(debug = True)
 