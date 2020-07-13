from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask('sayhello')
app.secret_key = 'ni cai cai'
#配置数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:123456@127.0.0.1:3306/flasktest?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from sayhello import views,errors