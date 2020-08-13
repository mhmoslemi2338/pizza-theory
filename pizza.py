import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from show import Show

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY,rep
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if ((x-269)**2+(y-269)**2)<200**2 :
            cv2.circle(tmp,(x,y),10,(255,0,0),-1)
            mouseX,mouseY = x,y
            rep+=1
            
def getpoint(img):
    global tmp
    tmp=img.copy()
    tmp=cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
    global rep
    rep=0
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    while(1):
        if rep==1:
            break
        cv2.imshow('image',tmp)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break      
    cv2.destroyAllWindows()
    cordinate='(x,y)= '+'('+str(mouseX-269)+','+str(-mouseY+269)+')'
    cv2.circle(tmp,(269,269),4,(0,255,0),-1)
    return cordinate,cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB),[mouseX,mouseY]


def draw_line(img,theta,color='green'):
    if theta==90:
        theta=89.97
    if theta==270:
        theta=269.97
    P=[mouseX-269,-mouseY+269]
    theta=theta%360
    tmp2=img.copy()
    if theta<90 or theta>270:
        L1=P[0]
        L2=539
        S=1
    elif theta<270:
        L2=-539
        L1=P[0]
        S=-1
    for X in range(L1,L2,S):
        Y=int(P[1]+math.tan(theta*math.pi/180)*(-P[0]+X))
        if (X)**2+(Y)**2>265**2:
            if theta<90 and theta >45:
                Y=np.abs(Y)
            end=[int(X+269),int(269-Y)]
            break
    if np.abs(Y)>=1000:
        Y=int(np.sign(Y)*math.sqrt(265**2-X**2))
        end[1]=int(269-Y)
    if color=='blue':
        cv2.line(tmp2,(mouseX,mouseY),(end[0],end[1]),(0,0,255),4);
    if color=='green':
        cv2.line(tmp2,(mouseX,mouseY),(end[0],end[1]),(0,255,0),4);
    return tmp2,end

def execute(img,n):
    cordinate,tmp,P=getpoint(img)
    tmp2=img.copy()
    cv2.circle(tmp2,(P[0],P[1]),10,(0,0,255),-1)
    for th in range(0,360,int(360/n)):
        color='blue'
        if ((th/int(360/n))%2)==0:
            color='green'
        tmp2,_=draw_line(tmp2,th,color)
    cv2.circle(tmp2,(P[0],P[1]),8,(255,0,0),-1)
    return tmp,tmp2,cordinate
'''
#############################################################################################
################################     showing the result    ##################################
#############################################################################################
'''

n=12

img=cv2.imread('c.png')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


IMG1,IMG2,title=execute(img,n)
Show.compareim(IMG1,IMG2,title,size=2)
plt.show()

