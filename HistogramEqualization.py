# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:21:48 2019

@author: h2r
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def histogram(img):
    height=img.shape[0]
    width=img.shape[1]
    hist=np.zeros((256))
    for i in np.arange(height):
        for j in np.arange(width):
            a=img.item(i,j)
            hist[a]+=1
    return hist

def cumulative_histogram(hist):
    cum_hist=hist.copy()
    
    for i in np.arange(1,256):
        cum_hist[i]=cum_hist[i-1]+cum_hist[i]
    
    return cum_hist

def main():
    
    imgpath="low_contrast_1.jpg"
    
    img=cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE) #default
    plt.imshow(img,cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.show() 
    
    hist,bins=np.histogram(img.ravel(),256,[0,255])
    plt.xlim([0,255])
    plt.ylim([0,6000])
    plt.plot(hist)
    plt.title('Histogram_before')
    plt.xlim(xmin=0,xmax=256)
    plt.show()
    
    height=img.shape[0]
    width=img.shape[1]
    
    pixels=width*height
    
    hist=histogram(img)
    cum_hist=cumulative_histogram(hist)
    
    for i in np.arange(height):
        for j in np.arange(width):
            a=img.item(i,j)
            b=math.floor(cum_hist[a]*255.0/pixels)
            img.itemset((i,j),b)
    
    outpath="after.jpg"
    cv2.imwrite(outpath,img)
    plt.imshow(img, cmap='gray')
    plt.title('Image_after')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    
    hist,bins=np.histogram(img.ravel(),256,[0,255])
    plt.xlim([0,255])
    plt.ylim([0,6000])
    plt.plot(hist)
    plt.title('Histogram_after')
    plt.xlim(xmin=0,xmax=256)
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
    
main()