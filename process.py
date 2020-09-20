import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import sys
import os
import json

output_data = dict()
folder_with_images = sys.argv[1]

if not os.path.isdir(folder_with_images):
    print("Unfortunately, this folder does not exist. Try again")
else:
    model = tf.keras.models.load_model('model/model_final.h5')
    print("processing...")
    for item in os.listdir(os.path.join(folder_with_images)):
        img_path = os.path.join(folder_with_images, item)
        img = image.load_img(img_path, target_size=(150, 150, 3))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        pred = model.predict(x, batch_size=10)
        output_data[item] = ("male" if pred > .5 else "female")
    with open('process_results.json', 'w') as json_file:
        json.dump(output_data, json_file)
    print("DONE! File with results has been saved in ", os.getcwd())
