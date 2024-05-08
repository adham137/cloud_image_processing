from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField, FieldList, FormField, StringField
from wtforms.validators import InputRequired

class UploadFileForm(FlaskForm):
    # Declare our form variables
    # file = FileField("File", validators= [InputRequired()]) # The file field, required to not be blank
    file = FileField("File") # The file field, required to not be blank
    upload = SubmitField("Upload File")                     # The submit field
    next = SubmitField("Next")

class ChooseOperationForm(FlaskForm):
    # Declare our form variables
    imageName = StringField('image name:')
    operation = SelectField("Operation", choices=[('edge_detection', 'Detect Edges'), ('color_inversion', 'Invert Colors')])
    # submit = SubmitField("Upload File")                     # The submit field

class ChooseOperationsForm(FlaskForm):
    # Declare the list of files and choices
    operations = FieldList(FormField(ChooseOperationForm), min_entries= 1)
    submit = SubmitField("Upload File")                     # The submit field

class DownloadProcessedImageForm(FlaskForm):
    # Declare our form variables
    imageName = StringField('image name:')
    submit = SubmitField("Download File")                     # The submit field

class DownloadProcessedImagesForm(FlaskForm):
    # Declare our form variables
    enteries = FieldList(FormField(DownloadProcessedImageForm), min_entries= 1)