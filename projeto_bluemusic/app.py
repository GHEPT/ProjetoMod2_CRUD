from flask import (Flask, Blueprint, render_template,request)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)

@bp.route('/')
def home():
  return render_template('index.html')



