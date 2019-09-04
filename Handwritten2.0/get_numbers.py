import cv2
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import os

def get_images(filepath):
    imgs = []

    img = cv2.imread(filepath)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgs.append(imgGray)

    img = imgs[0]

    img = cv2.resize(img, (0,0), fx = 0.125, fy = 0.125)

    plt.imshow(img,cmap='gray')
    plt.show()

    treshold = 60

    treshImg = img < treshold
    x, y = np.where(treshImg)

    data = np.append(x[..., None], y[..., None], axis=1)

    db = DBSCAN(eps = 3, min_samples=3)
    db.fit(data)

    labelovi = np.unique(db.labels_)

    odvojene_slike = []
    minimalni_y = []


    for lab in labelovi:

        xt = x[db.labels_ == lab]
        yt = y[db.labels_ == lab]

        xmin = np.min(xt)
        xmax = np.max(xt)

        ymin = np.min(yt)
        ymax = np.max(yt)

        slika = img[xmin:xmax+1, ymin:ymax+1]
        max_slike = np.max(slika.shape)
        new_img = np.ones((int(max_slike*1.1), int(max_slike*1.1)))*255

        height_slike = slika.shape[0]
        height_new_img = new_img.shape[0]
        pocetni_height = (height_new_img - height_slike) // 2
        krajnji_height = pocetni_height+height_slike

        width_slike = slika.shape[1]
        width_new_img = new_img.shape[1]
        pocetni_width = (width_new_img - width_slike) // 2
        krajnji_width = pocetni_width + width_slike

        new_img[pocetni_height:krajnji_height, pocetni_width:krajnji_width] = slika
        odvojene_slike.append(new_img)
        minimalni_y.append(ymin)
    plt.imshow(odvojene_slike[0], cmap='gray')
    plt.savefig('primer.png')
    redoslijed = np.argsort(minimalni_y)

    sortirane_slike = []
    for indeks in redoslijed:
        sortirane_slike.append(odvojene_slike[indeks])
    
    return sortirane_slike