from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class ListingForm(FlaskForm):
    living_space_area = IntegerField('Total Living Space Area', [DataRequired()])
    bedrooms = StringField('Beds', [DataRequired()])
    bathrooms = StringField('Baths', [DataRequired()])
    zipcode = StringField('Zipcode', [DataRequired()])
    list_price = IntegerField('List Price', [DataRequired()])
    submit = SubmitField('Submit')
