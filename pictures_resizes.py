# -*- coding: UTF-8 -*-
from scipy import misc                                                                                      # module importation
from skimage.io import imread
import numpy as np
import glob
from os.path import join

path = "D:/Users/chpere/Documents/Python/Projects_Python/" 
pictures_list = []
for ext in ('*.gif', '*.png', '*.jpg', '*.jpeg','*.bmp'):                                                   # permit to save all the files in the path with the extension selected
   pictures_list.extend(glob.glob(join(path, ext)))
print("You have {} in your files, process to change resolution in progress".format(len(pictures_list)))     # print the number of files in the folder

                                                                                               # minimum size of height or length of the picture

img_modif = 0
for files in pictures_list:                                                                                 # loop for in the number of files
    img = open(files,'r')                                                                                   # open the pictures 
    im = imread(files)                                                                                      # and read it
    #if(min(len(im),len(im[0]))>crit):                                                                       # enter the loop if the picture is larger ou higher of the criteria crit (number minimal of pixels)
    img2 = misc.imresize(im, round((1/(min(len(im),len(im[0]))/crit))*100), interp='bicubic')             # resize the picture 25% of the original 
    misc.imsave(files[:len(files)-4]+'_2.jpg', img2)                                                     # save the pictures with the name (path included) with the number 2
    new_img = files.split("\\")                                                                         # split the path to access to the name of the files
    
    print("The picture {} was created".format(new_img[len(new_img)-1]))                                 # avert the user that the pictures was changed 
    
    img.close()
    
print("\nYou have modified {} pictures".format(img_modif))                                                  # say how many pictures was mdified 
