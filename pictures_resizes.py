# -*- coding: UTF-8 -*-
from scipy import misc                                                                                      # module importation
from skimage.io import imread
import numpy as np
import glob

pictures_list = glob.glob("D:/Users/chpere/Documents/Python/Projects_Python/*jpg")                          # permit to save all the files in the path with the extension selected
print("You have {} in your files, process to change resolution in progress".format(len(pictures_list)))     # print the number of files in the folder

for files in pictures_list:                                                     # loop for in the number of files
    img = open(files,'r')                                                       # open the pictures 
    im = imread(files)                                                          # and read it

    img2 = misc.imresize(im, 25, interp='bicubic')                              # resize the picture 25% of the original 
    misc.imsave(files[:len(files)-4]+'2.jpg', img2)                             # save the pictures with the name (path included) with the number 2
    
    new_img = files.split("\\")                                                 # split the path to access to the name of the files
    
    print("The picture {} was changed".format(new_img[len(new_img)-1]))         # avert the user that the pictures was changed 
    
    
    