import cv2
import os
from PIL import Image

import numpy as np

def getImageAndLabels(
        #path,
        Img):
    # facesSamples=[]
    # ids=[]
    # iamgepath = [os.path.join(path, f) for f in os.listdir(path)]
    face_dector = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')

    gray_img = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)
    face = face_dector.detectMultiScale(gray_img, 1.2)
    for x, y, w, h in face:
        cv2.rectangle(Img, [x, y], [x + w, y + h], [0, 245, 250], 3, cv2.LINE_AA)
    cv2.imshow('img2', Img)


if __name__ == '__main__':
    k = 2
    if k == 1:
        image = cv2.imread('D:/tu/RM.png')
    else:
        image = cv2.imread('D:/tu/man1.jpg')
    getImageAndLabels(image)
    cv2.waitKey(0)

