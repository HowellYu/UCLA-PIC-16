#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:16:01 2017

@author: howell
"""

#library
import turtle as t
import matplotlib.pyplot as plt
import urllib
import re
import numpy as np
import math
from matplotlib.backends.backend_pdf import PdfPages

"""Q1"""
#get the data 
airfare = urllib.request.urlopen("http://www.stat.tamu.edu/~sheather/book/docs/datasets/airfares.txt").read()
airfare = str(airfare)
city = re.findall(r'\\n([0-9]+)\\t', airfare)
fare = re.findall(r'\\t([0-9]+)\\t', airfare)
distance = re.findall(r'\\t([0-9]+)\\r', airfare)
fare = [float(item) for item in fare]
distance = [float(item) for item in distance]
city = [float(item) for item in city]

#scatter plot 
plt.plot(fare, distance, 'ro')
plt.xlabel("Fare")
plt.ylabel("Distance")
plt.title("Flying distance Vs. Fare")
plt.legend()
plt.show()

#histogram
plt.bar(city, distance, .4, color = 'r', label = 'distance')
shift_city = [item + 0.4 for item in city]
plt.bar(shift_city, fare, .4, color = 'b', label = 'fare')
plt.title('City Vs. Distance and Fare')
plt.xlabel("City (Number)")
plt.legend(loc = 2)
plt.show()


"""Q2"""
"""
#input layer 
x_1 = [] 
y_1 = []
input_node = 6

for i in range(2*input_node):
    if(np.cos(2*np.pi*i/input_node) <= 0):
        x_1.append(np.cos(2*np.pi*i/input_node))
    
for i in range(2*input_node):
    if(np.cos(2*np.pi*i/input_node) <= 0):
        y_1.append(np.sin(2*np.pi*i/input_node))
    
plt.plot(x_1, y_1, 'ro')

#hidden layer
A = [[0.5, 0.75], [0.5, 0.25], [0.5, -0.25], [0.5, -0.75]]

#Output Layer
x_3 = [] 
y_3 = []
input_node = 6

for i in range(2*input_node):
    if(np.cos(2*np.pi*i/input_node) >= 0):
        x_3.append(np.cos(2*np.pi*i/input_node))
    
for i in range(2*input_node):
    if(np.cos(2*np.pi*i/input_node) >= 0):
        y_3.append(np.sin(2*np.pi*i/input_node))

#establish the network
for i in range(4):
    for j in range(len(x_1)):
        plt.plot(A[i], [x_1[j], y_1[j]], 'g')
    for k in range(len(x_3)):
        plt.plot(A[i], [x_3[k], y_3[k]], 'r')    
"""
fedex = [[1,1,1,0,0,0,1,1],[0,1,1,0,1,0,1,1],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,1],
         [0,1,0,1,0,1,1,1],[0,1,0,0,0,0,1,1],[0,1,0,1,1,1,1,1],[0,1,0,0,0,1,0,0]]
n = len(fedex)
x = [0 for i in range(n)]
for i in range(n):
    x[i] = np.cos(2*np.pi*i/n) 
    
y = [0 for i in range(n)]
for i in range(n):
    y[i] = np.sin(2*np.pi*i/n)  

plt.plot(x,y,'bo')
for i in range(n):
    for j in range(n):
        if fedex[i][j] == 1:
            plt.plot([x[i],x[j]],[y[i],y[j]],'r-')
            
plt.title('Fedex Transportation among 8 Cities')
plt.show()

"""Q3"""
def fractal(order, size):
    
    #base case
    if order == 0:
        t.fd(size)
        return 
    
    #recursive steps
    order -= 1
    size /= 3
    
    fractal(order, size)
    
    t.left(60)
    fractal(order, size)
    
    t.right(120)
    fractal(order, size)
    
    t.left(60)
    fractal(order, size)
    
    return

def fractal_total(order, size):
    
    fractal(order, size)
    
    t.right(120)
    fractal(order, size)
    
    t.right(120)
    fractal(order, size)
    
    return
fractal_total(3,200)

"""Q4"""
def picture():
    pic = [[[0,0,0] for _ in range(128)] for _ in range(256)]
    blue = [[19,16,2,11], [23,5,30,7], [8,17,10,31], [20,25,14,15],
            [1,9,18,0], [12,21,22,4], [24,13,26,27], [28,29,6,11]]
    
    for i in range(128):
        for j in range(256):
            pic[j][i][2] = blue[j % 8][i % 4]/31.0
                   
    for i in range(32):
        for j in range(4):
            for k in range(256):
                pic[k][i*4 + j][0] = i/31.0
                       
    for i in range(32):
        for j in range(8):
            for k in range(128):
                pic[i*8 + j][k][1] = i/31.0
                       
    plt.imshow(pic)
    
picture()


pp = PdfPages('report.pdf')
plt.savefig(pp, format='pdf')
pp.close()