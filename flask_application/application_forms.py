from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField
from wtforms.validators import InputRequired

class UploadFileForm(FlaskForm):
    # Declare our form variables
    file = FileField("File", validators= [InputRequired()]) # The file field, required to not be blank
    submit = SubmitField("Upload File")                     # The submit field

class ChooseOperationForm(FlaskForm):
    # Declare our form variables
    #file = FileField("File", validators= [InputRequired()]) # The file field, required to not be blank
    operation = SelectField("Operation", choices=[('edge_detection', 'Detect Edges'), ('color_inversion', 'Invert Colors')])
    submit = SubmitField("Upload File")                     # The submit field