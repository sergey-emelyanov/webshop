from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class CreateForm(FlaskForm):
	title = StringField('title', validators=[DataRequired()], render_kw={'class': 'form-control'})
	price = IntegerField('price', render_kw={'class': 'form-control'})
	submit = SubmitField('submit')
