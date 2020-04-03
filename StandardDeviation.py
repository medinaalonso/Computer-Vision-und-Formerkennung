import numpy as np # linear algebra
import pandas as pd 
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os, sys
from IPython.display import display
from IPython.display import Image as _Imgdis
from PIL import Image
import numpy as np
from time import time
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.image as im
import scipy



folder = "C:/Users/DiBot/Desktop/CIC/RFVC/Photos/"

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

print("Imagenes existentes: {0} ".format(len(onlyfiles)))
print("Imagenes ")
image = []

n=50
train_files = []
y_train = []
i=0
for _file in onlyfiles:
    
    train_files.append(_file)
    label_in_file = _file.find("_")
    
print("Files in train_files: %d" % len(train_files))

# Dimensiones originales
image_width = 640
image_height = 480
ratio = 4

image_width = int(image_width / ratio)
image_height = int(image_height / ratio)

channels = 3
nb_classes = 1

dataset = np.ndarray(shape=(len(train_files), channels, image_height, image_width),
                     dtype=np.float32)

i = 0
#A array de Numpy
for _file in train_files:
    
    img = Image.open(folder + "/" + _file)  
    img.thumbnail((image_width, image_height))
    
    x = img_to_array(img)  
   

   
    x = x.reshape((3, 120, 160))

   # x = (x - 128.0) / 128.0
    dataset[i] = x
    i += 1
    if i % 250 == 0:
        print("%d array" % i)
print(dataset[1]) 
print("Iamgenes guardadas!")
arreglo = np.sum(dataset,axis=0) / n
"""
print(type(arreglo))
print(arreglo)
aveIm=arreglo.transpose(2,0,1).reshape(-1,arreglo.shape[1])
im.imsave("ave.png", aveIm, format = 'png')
"""
suma = 0
for j in np.arange(n):
    suma += np.square(arreglo - dataset[j])
    suma = suma / (n - 1)
    res = np.sqrt(suma)


res = res.astype(np.uint8)
res=res.transpose(2,0,1).reshape(-1,res.shape[1])

im.imsave("Noise.png", res, format = 'png')

