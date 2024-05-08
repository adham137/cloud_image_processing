from flask import Flask, render_template, send_from_directory, redirect, url_for, Response, send_file
from application_forms import UploadFileForm, ChooseOperationForm, ChooseOperationsForm, DownloadProcessedImageForm, DownloadProcessedImagesForm
from werkzeug.utils import secure_filename
import os
from PIL import Image
from remote_procedure_calls import process_images

# Create flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mofta7_sery'    
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/images/')

#############################################################################################

# Global Variables

# Create an array of uploaded files
uploaded_files = []
# Message to be sent to server
msg = []
# Processed images
processed_images = []

#############################################################################################


# Define home function, allows user to upload images
@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])
def home():

    # Create an upload form instance
    form = UploadFileForm()

    if form.validate_on_submit(): # What happens when we submit the form
            
            if form.upload.data:
            # Grab the file
                file = form.file.data 
                # Save the file
                file.save(
                    os.path.join(
                        os.path.abspath(os.path.dirname(__file__)),         # Application root directory
                        app.config['UPLOAD_FOLDER'],                # Upload folder path
                        secure_filename(file.filename)              # Secure file to be saved
                    ))
                # Update uploaded files array
                uploaded_files.append(file.filename)
                # Update the view
                return render_template('upload_page.html', form= form, filenames = uploaded_files)
            if form.next.data:
                # Return a page allowing user to choose the image and the operation required with it
                # return redirect(url_for('choose_operation', filename= secure_filename(file.filename)))
                return redirect('choose_operations')
    

    # Return upload page and the form
    return render_template('upload_page.html', form= form)

#############################################################################################

# Get the constructed form to be displatyed to the user
@app.route('/choose_operations', methods=['GET'])
def choose_operations_get():
     
    # Create a form to submit multiple operations for multiple images
    form = ChooseOperationsForm()

    # Fill in the Form data
    operations_data = [{'imageName': uploaded_img, 'operation': ChooseOperationForm()} for uploaded_img in uploaded_files]
    form.process(data={'operations': operations_data})

    # Return the Form
    return render_template('choose_operation.html', form=form)

# Post the filled form from the user
@app.route('/choose_operations', methods=['POST'])
def choose_operations_post():
     
    form = ChooseOperationsForm()

    # Construct the message
    global msg
    msg = [{'image': entry['imageName'], 'operation': entry['imageName']} for entry in form.operations.data]
    # Redirect to 'loading' function
    return redirect('loading')

#############################################################################################

@app.route('/loading', methods=['GET'])
def loading_screen_get():
     
    # Display loading screen
    # render_template('loading_screen.html')
    # Call RPC
    global processed_images
    processed_images = process_images(msg)
    # Return the download page
    return render_template('loading_screen.html')

@app.route('/loading', methods=['POST'])
def loading_screen():
     
    return redirect('download_file.html')

#############################################################################################

@app.route('/download_file', methods= ['GET'])
def download_file_get():

    return 'Under Construction'
    # Create an download form instance
    form = DownloadProcessedImagesForm()

    # Fill in the Form data
    enteries_data = [{'imageName': img.filename, 'submit': False} for img in processed_images]
    form.process(data={'enteries': enteries_data})

# Define download function, allows user to download images
@app.route('/download_file', methods= ['POST', 'GET'])
def download_file():
    
    # Create an download form instance
    form = DownloadProcessedImageForm()
    
   # print(f"################# {app.static_folder}")
    if form.validate_on_submit(): # What happens when we submit the form

        # Download the file
        processed_folder = os.path.join(app.static_folder, 'processed_images')
        processed_file_path = os.path.join(processed_folder, filename)
        return send_file(path_or_file=processed_file_path, mimetype= 'image/jpg', as_attachment= True)
        
        
    # Return download page and the form
    return render_template('download_processed_image.html', form= form)
    

#############################################################################################

# Run the flask application
if __name__ == '__main__':
    app.run(debug=True)

