from flask import Flask, render_template
from upload_forms import UploadFileForm
from werkzeug.utils import secure_filename
import os

# Create flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mofta7_sery'    
app.config['UPLOAD_FOLDER'] = 'static/images'
@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])

# Define gome function
def home():

    # Create an upload form instance
    form = UploadFileForm()

    if form.validate_on_submit(): # What happens when we submit the form
        # Grab the file
        file = form.file.data 
        # Save the file
        file.save(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), # Application root directory
                app.config['UPLOAD_FOLDER'],                # Upload folder path
                secure_filename(file.filename)              # Secure file to be saved
            ))
        return 'File has been uploaded'
    
    # Return upload page and the form
    return render_template('upload_page.html', form= form)

# Run the flask application
if __name__ == '__main__':
    app.run(debug=True)

