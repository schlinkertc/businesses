from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class SubmitBusiness(FlaskForm):
    business_name = StringField('Business: ', validators=[DataRequired()])
    business_location = StringField('Location: ', validators=[DataRequired()])
    submit = SubmitField("Submit")

class ConfirmBusiness(FlaskForm):
    confirm = SubmitField("Confirm")
