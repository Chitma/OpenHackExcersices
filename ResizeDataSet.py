from PIL import Image
from PIL import ImageOps
from resizeimage import resizeimage
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 

dataset_path = "C://Users//Manish//Desktop//manish_data"
original_image_path = "C://Users//Manish//Desktop//manish_data//axes//809257.jpeg"
equalized_image_path = "C://Users//Manish//Desktop//manish_data//axes001//809257.jpeg"

def resize_file(file_path,out_file,size):
       image = resizeimage.resize_thumbnail(Image.open(file_path),size)

       if(image.format == 'PNG'):
           image = image.convert('RGB')
           
       image_eq = ImageOps.equalize(image)
       image_eq.save(out_file)
       image_eq.close()

def get_subfolders(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolders

def modify_images(subfolders):
    for folder in subfolders:
        if(os.path.exists(folder).contains('001')):
            continue
        else:
             if(os.path.exists(folder +'001')):
                 for file in os.listdir(folder):
                     resize_file(folder+'//'+file,folder+'001'+'//'+file,(128,128))
             else:
                 os.makedirs(folder + '001')
                 for file in os.listdir(folder):
                     resize_file(folder+'//'+file,folder + '001' +'//'+file,(128,128))

def get_image_plot(Path):
    np_image = plt.imread(Path)
    plt.hist(np_image.ravel(),bins = 256,range = [0,255])
    plt.show()

if __name__ == '__main__':

  #  subfolders = get_subfolders(path = dataset_path)

   # modify_images(subfolders = subfolders)

    get_image_plot(original_image_path)

    get_image_plot(equalized_image_path)

    