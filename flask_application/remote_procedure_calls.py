from flask import Flask, send_from_directory
from werkzeug.utils import secure_filename
import os
import time
import json
import base64


def process_images(msg):
    # msg = [{image: , operation} , ... ]

    request_headers = {
    'Content-Type': 'application/json'
    }

    # Construct the JSON object
    payload_data = []
    for entry in msg:
        encoded_img = get_base64_encoded_image(os.path.join('./images/', entry['image']))
        img_payload = {'operation': entry['operation'], 'image': encoded_img}
        payload_data.append({'image{i}': img_payload})

    image_payload_body={
                  "number_of_images":i,
                  "images":payload_data
                  }

    # response = requests.post(url=CAMERA_FEED_URL, json=image_payload_body, headers=request_headers, auth=(USERNAME, PASSWORD))

    # return  image

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

