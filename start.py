from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import orm
from sqlalchemy import exc
import os


from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField
from wtforms.fields.html5 import DateField
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
            View('Config', 'config')
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
    date_from = DateField('Start:', validators=[DataRequired()])
    date_to = DateField('End:', validators=[DataRequired()])

class ConfigForm(FlaskForm):
    tagname = StringField('TagName', validators=[DataRequired()])
    tag_type = SelectField(u'Type', choices=[('boolarray', 'boolarray'),
                                             ('float', 'float'), 
                                             ('short', 'short'),
                                             ('byte', 'byte'),
                                             ('integer', 'integer')])
    dbnumber = DecimalField(u'DB Number')
    startadress = DecimalField(u'Start adress',places=3)
    size = DecimalField(u'Size',places=3) 

def create_app():

  application = Flask(__name__)

  nav.init_app(application)
  Bootstrap(application)
  application.config['SECRET_KEY'] = SECRET_KEY

  return application


app = create_app()
engine = create_engine('mysql+mysqlconnector://root:MT0334!@172.24.15.181:3306/plc_tag_test', echo=False)
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
        q = session.query(Values)\
            .filter(Values.tag_id == select_form.tag.data)\
            .filter(Values.date >= select_form.date_from.data)\
            .filter(Values.date <= select_form.date_to.data)
        values = q.all()
        selected = True

    return render_template('values.html', values=values, tags=tags, select=select_form, selected=selected)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/config',  methods=('GET', 'POST'))
def config():
    tag_config = ConfigForm()
    return render_template('config.html',tag_config=tag_config)
    
if __name__ == "__main__":  
    app.run(host='127.0.0.1',debug= True)
      