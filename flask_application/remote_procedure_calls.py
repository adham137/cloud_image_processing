import os
from flask import Flask, send_from_directory

def process_image(image, operation):
    
    # Put the image and the operation in a message
    # Connect to a vm
    # Send the message to a free vm and recieve the result
    # Return the result image

    processed_file_path = os.path.join('./static/processed_images', image.filename)
    return  send_from_directory(path= processed_file_path, as_attachment= True)