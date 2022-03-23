from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, IntegerField, SelectField
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

class NewPropertyForm(FlaskForm):
    title = StringField("Property Title", validators=[InputRequired()])

    number_of_bedrooms = IntegerField("No. of Rooms", validators=[InputRequired()])

    number_of_bathrooms = IntegerField("No. of Bathrooms", validators=[InputRequired()])

    location = StringField("Location", validators=[InputRequired()])

    price = IntegerField("Price", validators=[InputRequired()])

    property_type = SelectField("Type", choices=[("House","House"), ("Apartment","Apartment")])

    description = TextAreaField("Description")

    photo = FileField("Photo", validators=[InputRequired(),FileAllowed(["jpg","png"], "Sorry, this isn't an accepted file format.")])