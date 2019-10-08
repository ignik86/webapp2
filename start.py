from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import orm
import os


from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

from flask import Flask, render_template, redirect, request, url_for


nav = Nav()
SECRET_KEY = os.urandom(32)


@nav.navigation()
def mynavbar():
    return Navbar(
        'Test App',
        View('Home', 'main'),

        Subgroup(
            'Tags',
            View('Values', 'values'),

        ),
    )


class Values(object):
    def __init__(self, tag_id, value, date):
        self.tag_id = tag_id
        self.value = value
        self.date = date

    def __repr__(self):
        return "Value('%s')" % (self.value)


class Tags(object):
    def __init__(self,id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "Tag('%s')" % (self.name)


class SelectTag(FlaskForm):
    tag = SelectField(u'TagName', coerce=int)


def create_app():

  application = Flask(__name__)

  nav.init_app(application)
  Bootstrap(application)
  application.config['SECRET_KEY'] = SECRET_KEY

  return application


app = create_app()
engine = create_engine('mysql+mysqlconnector://root:MT0334!@172.24.15.181:3306/plc_tag', echo=False)
meta = MetaData(bind=engine, reflect=True)
orm.Mapper(Values, meta.tables['values'])
orm.Mapper(Tags, meta.tables['tags'])

session = orm.Session(bind=engine)


@app.route('/values',  methods=('GET', 'POST'))
def values():

    q = session.query(Tags)
    tags = q.all()
    values = Values(0,0,0)
    selected = False
    select_form = SelectTag()
    select_form.tag.choices = [(g.id, g.name) for g in tags]
    if select_form.validate_on_submit():
        q = session.query(Values).filter(Values.tag_id == select_form.tag.data)
        values = q.all()
        selected = True

    return render_template('values.html', values=values, tags=tags, select=select_form, selected=selected)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')





