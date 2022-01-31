from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField

class Tasks(FlaskForm):
    id   = IntegerField()
    title= StringField()
    description= TextAreaField()
    done = BooleanField()
