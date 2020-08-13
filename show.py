import matplotlib.pyplot as plt
import numpy as np
import cv2
class Show:    
    @staticmethod
    def show_me(img,title='',mode='',scale=1):
        if scale!=1:
            height=int(img.shape[0]*(scale))
            width=int(img.shape[1]*(scale))
            dimention=(width,height)
            img = cv2.resize(img, dimention, interpolation=cv2.INTER_AREA)
        if mode=='':
            plt.figure(figsize=(int(7*scale), int(14*scale)))
        if len(img.shape)==2:
            plt.imshow(img,'gray')    
        else:
            plt.imshow(img)
        plt.axis(False)
        plt.title(title)
        #plt.show()
    @staticmethod
    def compareim(img1,img2,title1='',title2='',size=1,triple=0,img3=[],title3=''):
        if triple!=0:
            plt.figure(figsize=(int(10*size), int(20*size)))
            plt.subplot(1,3,1)
            Show.show_me(img1,title1,mode='compare')
            plt.subplot(1,3,2)
            Show.show_me(img2,title2,mode='compare')
            plt.subplot(1,3,3)
            Show.show_me(img3,title3,mode='compare')
        else:
            plt.figure(figsize=(int(10*size), int(20*size)))
            plt.subplot(1,2,1)
            Show.show_me(img1,title1,1)
            plt.subplot(1,2,2)
            Show.show_me(img2,title2,1)