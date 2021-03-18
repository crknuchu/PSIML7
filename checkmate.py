import numpy as np
import PIL
from PIL import Image
import os

# used some code from here for the first task https://stackoverflow.com/questions/14767594/how-to-detect-object-on-images

#/home/mihailo/Desktop/PSIML/checkmate_public/public/set/0
os.chdir(input())

def coords(image):

    image_data = np.asarray(image)
    image_data_blue = image_data[:,:,2]
    #print(image_data)

    median_blue = np.median(image_data_blue)

    non_empty_columns = np.where(image_data_blue.max(axis=0)>median_blue)[0]
    non_empty_rows = np.where(image_data_blue.max(axis=1)>median_blue)[0]

    boundingBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

    print(str(boundingBox[0])+","+str(boundingBox[2])) # x,y coord

for f in os.listdir("."):
    if f.endswith(".png"):
        image = Image.open(f)

coords(image)


