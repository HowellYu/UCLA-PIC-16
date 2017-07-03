#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:24:34 2017

@author: howell
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import random
import cv2


"""Q1"""
"""image: the image input"""
def gray_scale(image):
    
    im = np.array(image)
    
    #make gray_scale
    gray = im
    gray[:,:,0] = im[:,:,0]
    gray[:,:,1] = im[:,:,0]
    gray[:,:,2] = im[:,:,0]
    
    return gray
"""
m_input: the original image
method: either uniform or gaussian
k: the parameter user chooses for the method, odd number
sigma: the parameter for gaussian 
"""
def blurring(m_input, method, k, sigma = 10, show = False):
    
    m_input = np.array(m_input)  
    
    #make sure the image is in gray scale
    m_input = gray_scale(m_input)
    gray = np.array(m_input)   
    
    #return gray
    
    #get the dimension of the picture
    row_len = gray.shape[0]
    col_len = gray.shape[1]
    #blurred = np.zeros((row_len, col_len))
    
    blurred = np.matrix.copy(gray)
    margin_width = int(k/2) 
    half_k = int(k/2) #the width of the submatrix is k.
    
    #uniform blurring
    if method == "uniform":
        
        for i in range(margin_width, row_len - margin_width):
            for j in range(margin_width, col_len - margin_width):
                
                #extract submatrix
                submatrix = gray[np.ix_([i - half_k, i + half_k], 
                                      [j - half_k, j + half_k])]
    
                #get mean of the submatrix
                blurred[i][j] = np.mean(submatrix)
    
    #gaussian blurring
    elif method == "gaussian":
        
        for i in range(margin_width, row_len - margin_width):
            for j in range(margin_width, col_len - margin_width):
            
               #get the weight matrix
               #submatrix = gray[np.ix_([i - half_k, i + half_k], [j - half_k, j + half_k])]
               submatrix = gray[(i - half_k):(i+half_k), (j - half_k): (j + half_k)]
               weight = np.zeros((k, k))
               
               for u in range(k):
                   for v in range(k):
                       weight[u][v] = (0.5/np.pi/sigma ** 2) * math.exp(-0.5 * 
                             ((u - half_k) ** 2 + (v - half_k) ** 2)/sigma ** 2)
                
                #normalize the weight matrix
               normal_weight = np.divide(weight, np.sum(weight))
               #return normal_weight, submatrix
           
                #multiplication
               blurred[i][j] = np.sum(normal_weight * submatrix[:, :, 0])
    
    if show == True:
        plt.imshow(blurred)
    
    return blurred
        

'''
Add salt and pepper noise to image
prob: Probability of the noise
'''
def sp_noise(image, prob):
    
    output = np.array(image)
    image_2D = output[:,:,0]
    
    temp = np.zeros(image_2D.shape)
    thres = 1 - prob 
    for i in range(image_2D.shape[0]):
        for j in range(image_2D.shape[1]):
            rdn = random.random()
            if rdn < prob:
                temp[i][j] = 0
            elif rdn > thres:
                temp[i][j] = 255
            else:
                temp[i][j] = image_2D[i][j]
    output[:,:,0], output[:,:,1], output[:,:,2] = temp, temp, temp 
    
    plt.imshow(output)
    return output

"""test"""
im = Image.open('/Users/howellyu/Desktop/UCLA/Class/2017 Winter/PIC 16/W6/jason.jpg')

#add salt & pepper noise
sp_0 = gray_scale(im)
sp_20 = sp_noise(im)
sp_40 = sp_noise(im, 0.4)
plt.imshow(sp_0)
plt.imshow(sp_20)
plt.imshow(sp_40)

#blur with uniform 
blurring(sp_0, "uniform", 9, sigma = 10, show = True)
blurring(sp_20, "uniform", 9, sigma = 10, show = True)
blurring(sp_40, "uniform", 9, sigma = 10, show = True)

#blur with gaussian 
blurring(sp_0, "gaussian", 9, sigma = 10, show = True)
blurring(sp_20, "gaussian", 9, sigma = 10, show = True)
blurring(sp_40, "gaussian", 9, sigma = 10, show = True)


#im2 = Image.open('/Users/howellyu/Desktop/UCLA/Class/2017 Winter/PIC 16/W6/image2.jpg')
#im3 = Image.open('/Users/howellyu/Desktop/UCLA/Class/2017 Winter/PIC 16/W6/image4.jpg')
#blurring(im, "uniform", 20)
#blurring(im, "gaussian", 10, 10)



"""Q2"""
"""
matrix_multi: return the sum of the element product of 2 matrices
"""
def matrix_multi(M1, M2, return_total = True):
    
    #check dimension 
    if (M1.shape != M2.shape):
        print("dimension not match")
    #    return M1, M2
    
    new_matrix = np.zeros(M1.shape)
    
    for i in range(M1.shape[0]):
        for j in range(M1.shape[1]):
            new_matrix[i][j] = M1[i][j] * M2[i][j]
    if return_total == False:
        return new_matrix
    return np.sum(new_matrix)

"""
m_input: image
option: horizontal, vertical or both
"""
def detect_edge(m_input, option):
    
    #3 by 3 operating matrix
    horizontal = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    vertical = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])  
    
    m_input = np.array(m_input)
    edge = m_input
    m = m_input[:,:,0]
    row_len = m_input.shape[0]
    col_len = m_input.shape[1]
       
    for i in range(0, row_len - 2):
        for j in range(0, col_len - 2):
            
            submatrix = m[i: (i + 3), :]
            submatrix = submatrix[:, j:(j+3)]
            Gx = matrix_multi(submatrix, horizontal)
            Gy = matrix_multi(submatrix, vertical)
            
            if option == "horizontal":
                edge[i][j] = Gx
            elif option == "vertical":
                edge[i][j] = Gy
            elif option == "both":
                edge[i][j] = np.sqrt(Gx**2 + Gy**2)
                
    plt.imshow(edge)
    return edge
"""Test"""
detect_edge(im, "vertical")
detect_edge(im, "horizontal")
detect_edge(im, "both")

   
"""Q3"""
"""summation gives the sum of index * height, used to compute mean later"""
def summation(histogram, threshold, front = True):
    
    total = 0
    
    if front == True:
        for i in range(threshold):
            total += i * histogram[i]
    elif front == False:
        for i in range(threshold, 256):
            total += i * histogram[i]
    return total 
            
"""var_sum compute the variance before divided by the total height"""
def var_sum(histogram, threshold, mean, front = True):
    
    total = 0
    
    if front == True:
        for i in range(threshold): 
            total += (i - mean) ** 2 * histogram[i]
    elif front == False:
        for i in range(threshold, 256):
            total += (i - mean) ** 2 * histogram[i]
    return total
            
"""
Image: input image
show: whether to imshow() the modified image
"""
def otsu_threshold(image, show = False):
    
    #transformation
    image = np.array(image)
    image_2D = image[:,:,0]
    
    row_len = image.shape[0]
    col_len = image.shape[1]
    var_total = []
    new_image = image
    
    #1. create frequency histogram
    fre = np.zeros(256)
    for i in range(row_len):
        for j in range(col_len):
            fre[image_2D[i][j]] += 1
    
    #2. loop through each threshold
    for t in range(256):
        
        
        #find weight
        total_height_front = np.sum(fre[0 : t]) #<= threshold 
        total_height_back = np.sum(fre[t : 256]) #> threshold
        weight_front =  total_height_front/ row_len / col_len
        weight_back = 1 - weight_front

        #find mean
        mean_front = 0
        mean_back = 0
        
        if total_height_front != 0:
            mean_front = summation(fre, t) / total_height_front
        if total_height_back != 0:
            mean_back = summation(fre, t, False) / total_height_back
        
        #find variance 
        var_front = 0
        var_back = 0
        if total_height_front != 0:
            var_front = var_sum(fre, t, mean_front) / total_height_front
        if total_height_back != 0:
            var_back = var_sum(fre, t, mean_back, False) / total_height_back
         
        #total variance 
        var_total.append(weight_front * var_front + weight_back * var_back)
    
    #optimal threshold
    opt = var_total.index(min(var_total))
    #print("Your optimal threshold is", opt)
    
    #change to foreground and backgroud
    for i in range(row_len):
        for j in range(col_len):
            if image_2D[i][j] < opt:
                image_2D[i][j] = 0
            else:
                image_2D[i][j] = 255
    
    #change back to 3D                    
    new_image[:,:,0], new_image[:,:,1], new_image[:,:,2] = image_2D, image_2D, image_2D
    
    if show == True:
         plt.imshow(new_image)
    return new_image
    
"""Test"""
otsu_threshold(im, show = True)



"""Q4"""
"""
m_input: the original image
method: either uniform or gaussian
k: the parameter user chooses for the method, odd number
sigma: the parameter for gaussian 
"""  
def blur_background(m_input, method, k, sigma = 10):
    
    m_input = np.array(m_input)  
    
    #make sure the image is in gray scale
    m_input = gray_scale(m_input)
    gray = np.array(m_input)   
    
    #return gray
    
    #get the dimension of the picture
    row_len = gray.shape[0]
    col_len = gray.shape[1]
    #blurred = np.zeros((row_len, col_len))
    
    blurred = np.matrix.copy(gray)
    margin_width = int(k/2) 
    half_k = int(k/2) #the width of the submatrix is k.
    
    black_white = otsu_threshold(m_input)[:,:,0]
                
    #uniform blurring
    if method == "uniform":
        
        for i in range(margin_width, row_len - margin_width):
            for j in range(margin_width, col_len - margin_width):
                if black_white[i][j] == 255:       
                    #extract submatrix
                    submatrix = gray[np.ix_([i - half_k, i + half_k], 
                                          [j - half_k, j + half_k])]
        
                    #get mean of the submatrix
                    blurred[i][j] = np.mean(submatrix)
    
    #gaussian blurring
    elif method == "gaussian":
        
        for i in range(margin_width, row_len - margin_width):
            for j in range(margin_width, col_len - margin_width):
                if black_white[i][j] == 255: 
                   #get the weight matrix
                   #submatrix = gray[np.ix_([i - half_k, i + half_k], [j - half_k, j + half_k])]
                   submatrix = gray[(i - half_k):(i+half_k), (j - half_k): (j + half_k)]
                   weight = np.zeros((k, k))
                   
                   for u in range(k):
                       for v in range(k):
                           weight[u][v] = (0.5/np.pi/sigma ** 2) * math.exp(-0.5 * 
                                 ((u - half_k) ** 2 + (v - half_k) ** 2)/sigma ** 2)
                    
                    #normalize the weight matrix
                   normal_weight = np.divide(weight, np.sum(weight))
                   #return normal_weight, submatrix
               
                    #multiplication
                   blurred[i][j] = np.sum(normal_weight * submatrix[:, :, 0])
    
    plt.imshow(blurred)
    
    return blurred

"""Test"""
blur_background(im, "gaussian", 20)        
    
