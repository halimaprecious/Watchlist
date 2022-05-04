
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import data_required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators = [data_required()])
    review = TextAreaField('Movie review', validators = [data_required()])
    submit = SubmitField('Submit')