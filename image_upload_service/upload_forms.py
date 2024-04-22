from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

class UploadFileForm(FlaskForm):
    # Declare our form variables
    file = FileField("File", validators= [InputRequired()]) # The file field, required to not be blank
    submit = SubmitField("Upload File")                     # The submit field
