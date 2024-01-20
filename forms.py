from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

DEFAULT_IMAGE = '/static/Rocky.png'

class AddPets(FlaskForm):


    pet_name = StringField("Pet Name",
                           validators=[InputRequired()])
    species = SelectField("Species",
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])

    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes",
                        validators=[Optional()])

class EditPet(FlaskForm):

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    
    notes = StringField("Notes",
                        validators=[Optional()])
    
    # Could not use BooleanField as Bootstrap form-control did not give me checkboxes back
    available = SelectField("Available?",
                            choices=[(1, 'Yes'), (0, 'No')],
                            coerce=int)