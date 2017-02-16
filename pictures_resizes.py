# -*- coding: UTF-8 -*-
from scipy import misc                                                                                      # module importation
from skimage.io import imread
import numpy as np
import glob
from os.path import join

path = "D:/Users/chpere/Documents/Python/Projects_Python/Data_set" 
pictures_list = [] # [glob.glob(path) for path in ["*.png","*.jpeg","*.jpg"]]                          # permit to save all the files in the path with the extension selected
for ext in ('*.gif', '*.png', '*.jpg', '*.jpeg','*.bmp'):
   pictures_list.extend(glob.glob(join(path, ext)))
print("You have {} in your files, process to change resolution in progress".format(len(pictures_list)))     # print the number of files in the folder

crit = 150                                                                      # minimum size of height or length of the picture
img_modif = 0
for files in pictures_list:                                                     # loop for in the number of files
    img = open(files,'r')                                                       # open the pictures 
    im = imread(files)                                                          # and read it
    #print(len(im), len(im[0]))
    #size = (1/(min(len(im),len(im[0]))/100))*100
    if(min(len(im),len(im[0]))>crit):                                           # enter the loop if the picture is larger ou higher of the criteria crit (number minimal of pixels)
        img2 = misc.imresize(im, int((1/(min(len(im),len(im[0]))/crit))*100), interp='bicubic') # resize the picture 25% of the original 
        misc.imsave(files[:len(files)-4]+'2.jpg', img2)                                         # save the pictures with the name (path included) with the number 2
    #print(size)
        new_img = files.split("\\")                                                             # split the path to access to the name of the files
    
        print("The picture {} was created".format(new_img[len(new_img)-1]))                     # avert the user that the pictures was changed 
        img_modif += 1                                                                          # number of loop / pictures modified 
    
    img.close()
    
print("\nYou have modified {} pictures".format(img_modif))                                      # say how many pictures was mdified 
