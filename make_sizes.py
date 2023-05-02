# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:14:04 2023

@author: monim
"""

from glob import glob
import os
import cv2

in_path = 'trial/'
out_path = 'test_images/size/'

for image in glob(in_path+'*.png'):
    im = cv2.imread(image)
    h,w,c = im.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '_original.png', im)
    small = cv2.resize(im, (0,0), fx=0.5, fy=0.5)
    h,w,c = small.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', small)
    small = cv2.resize(small, (0,0), fx=0.5, fy=0.5)
    h,w,c = small.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', small)
    small = cv2.resize(small, (0,0), fx=0.5, fy=0.5)
    h,w,c = small.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', small)
    
for image in glob(in_path+'*.png'):
    im = cv2.imread(image)
    big = cv2.resize(im, (0,0), fx=1.5, fy=1.5, interpolation= cv2.INTER_LINEAR)
    h,w,c = big.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', big)
    big = cv2.resize(big, (0,0), fx=1.5, fy=1.5, interpolation= cv2.INTER_LINEAR)
    h,w,c = big.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', big)
    big = cv2.resize(big, (0,0), fx=1.5, fy=1.5, interpolation= cv2.INTER_LINEAR)
    h,w,c = big.shape
    cv2.imwrite(out_path + image.split('\\')[1][:-4] + '_' +
                str(h) + 'x' + str(w) + '.png', big)