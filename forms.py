from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddRecordForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    adress = StringField('adress', validators=[DataRequired()])
    tag = StringField('tag', validators=[DataRequired()])
    note = StringField('note', validators=[DataRequired()])
    birthday = StringField('birthday', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone = StringField('phone format 380.........', validators=[DataRequired()])
    submit = SubmitField('Add record')