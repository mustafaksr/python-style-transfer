import tensorflow as tf 
import numpy as np
import tensorflow_hub as hub
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from io import BytesIO
import base64

def show_n(image):
    fig = Figure(figsize=(6,6))
    plt.tight_layout()
    ax = fig.subplots()
    ax.imshow(np.squeeze(image, axis=0))
    ax.set_xticks(())
    ax.set_yticks(())
    buf = BytesIO()
    fig.savefig(buf, format="png",pad_inches=0.1,bbox_inches='tight')
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    image=f"<img src='data:image/png;base64,{data}'/>"
    return image

def style(file,file2):
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)
    stylized_image = hub_module(file,
                            file2)[0]
    return stylized_image
