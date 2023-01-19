import os
import random
import datetime
import logging
from typing import Dict
from flask import Flask, render_template, request, Response, redirect, url_for
import time
import jinja2
from jinja2 import Environment, FileSystemLoader
import numpy as np 
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow_hub as hub
from style_transfer import *


# environment = Environment(loader=FileSystemLoader("templates/"))

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get('PORT')  # Get PORT setting from the environment.


@app.route('/', methods=['GET',"POST"])
def show_df2():
    """responds to request from frontend via gateway"""
    if request.method =="GET":

        context = {
            "string3": "string3",

        }
        return render_template("index.html",**context)

    else:
        try: 
            file = request.files['image']
            file2 = request.files['image2']

            img = Image.open( file )
            img =img.resize((256,256))
            file = tf.constant(np.asarray( img, dtype="float32" )/225)[tf.newaxis, ...]

            img = Image.open( file2 )
            img =img.resize((256,256))
            file2 = tf.constant(np.asarray( img, dtype="float32" )/225)[tf.newaxis, ...]


            
            s_image= show_n(style(file,file2))
            context = {
                "string3": "string3",
                "stylized":s_image
            
            }
            return render_template("index.html",**context)
        except:
            return "You didn't select images or Clicked two times or You need to refresh page to create new stylized image"


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == '__main__':
    print("PORT is "+str(PORT))
    app.run(host='0.0.0.0', port=PORT,debug=True)
