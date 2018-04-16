import cv2
import numpy
import os
from PIL import ImageOps
from PIL import Image 
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.model_selection import train_test_split

# directory_Path = 'C://Users//Manish//Desktop//gear_images//axes01'

# files = os.listdir(directory_Path)

# i = 0

# for file in files:
#     print(file)
#     image =  Image.open(directory_Path + "//"+ file)
#     image_eq = ImageOps.equalize(image)

#     if(os.path.exists(directory_Path+'//axes-equalised')):
#         image_eq.save('C://Users//Manish//Desktop//gear_images//axes01//axes-equalised//result{}.jpeg'.format(i))
#     else:
#         os.makedirs(directory_Path+'//axes-equalised')

#     i = i + 1

#     array = plt.imread('C://Users//Manish//Desktop//gear_images//axes01//result1.jpeg')



# image =  Image.open('C://Users//Manish//Desktop//gear_images//axes01//10291102_zm.jpeg')
# image_eq = ImageOps.equalize(image)
from io import BytesIO
import requests
response = requests.get('https://shop.epictv.com/sites/default/files/ae42ad29e70ba8ce6b67d3bdb6ab5c6e.jpeg')

image = Image.open(BytesIO(response.content))

plt.imshow(image)
# image_eq.save('C://Users//Manish//Desktop//gear_images//axes01//result1.jpeg')

# array = plt.imread('C://Users//Manish//Desktop//gear_images//axes01//result1.jpeg')

# # plt.hist(array.ravel(),bins= 256 , range = [0,255])

# # plt.show()

# print(array.flatten())

# (trainX, testX, trainY, testY) = train_test_split(array.flatten(), dataset.target, test_size=0.25)