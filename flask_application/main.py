from flask import Flask, render_template, send_from_directory, redirect, url_for, Response, send_file
from application_forms import UploadFileForm, ChooseOperationForm, DownloadProcessedImageForm
from werkzeug.utils import secure_filename
import os
from remote_procedure_calls import process_image

# Create flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mofta7_sery'    
app.config['UPLOAD_FOLDER'] = 'static/images'

#############################################################################################

# Define home function, allows user to upload images
@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])
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
        
        # Return a page allowing user to choose an image and the operation required with it
        return redirect(url_for('choose_operation', filename= secure_filename(file.filename)))
    
    # Return upload page and the form
    return render_template('upload_page.html', form= form)

#############################################################################################

# Allows user to choose operations done to images
@app.route('/choose_operation/<filename>', methods= ['GET', 'POST'])
def choose_operation(filename):
    
    # Create an operation form instance
    form = ChooseOperationForm()

    if form.validate_on_submit(): # What happens when we submit the form

        # Use RPC to send the file and the operation to a remote server
        operation = form.operation.data
        image = send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment= True)
        processed_image = process_image(image, operation) ### Yet to be implemented
        # Process the image as a Response object
        #processed_image = Response(processed_image)
        

        # Create folder for proccessed images
        processed_folder = os.path.join(app.static_folder, 'processed_images')
        if not os.path.exists(processed_folder):
            os.makedirs(processed_folder)

        # Save the processed image 
        processed_file_path = os.path.join(processed_folder, filename)
        with open(processed_file_path, 'wb') as f:
            f.write(processed_image.get_data())

        # Return a page allowing user to download an image
        return redirect(url_for('download_file', filename= secure_filename(filename)))
    
    # Return upload page and the form
    return render_template('choose_operation.html', form= form)

#############################################################################################

# Define download function, allows user to download images
# Not Yet Tested
@app.route('/download_file/<filename>', methods= ['GET'])
def download_file(filename):
    
    # Create an download form instance
    form = DownloadProcessedImageForm()

    if form.validate_on_submit(): # What happens when we submit the form

        # Download the file
        processed_folder = os.path.join(app.static_folder, 'processed_images')
        processed_file_path = os.path.join(processed_folder, filename)
        return send_from_directory(path= processed_file_path, as_attachment= True)
        
    # Return download page and the form
    return render_template('download_processed_image.html', form= form)
    

#############################################################################################

# Run the flask application
if __name__ == '__main__':
    app.run(debug=True)

