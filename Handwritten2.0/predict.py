import cv2
import tensorflow as tf
import numpy as np
from get_numbers import get_images
import matplotlib.pyplot as plt
from get_formula import get_formula
import sys

model = tf.keras.models.load_model("results/dataset.h5")

CATEGORIES = ["0","1","2","3","4","5","6","7","8","9", "+", "-"]

def prepare(img):
    IMG_SIZE = 28  
    new_array = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  
    """plt.imshow(new_array, cmap='gray')
    plt.show() """
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def main (argv):
    images = get_images(argv)
    for image in images:
        plt.imshow(image, cmap='gray')
        plt.show()
    finalni_brojevi = []
    for image in images:
        prediction = model.predict([prepare(image)])  
        print(np.argmax(prediction))
        finalni_brojevi.append(np.argmax(prediction))

    get_formula(finalni_brojevi)

if __name__ == "__main__":
    main(sys.argv[1])