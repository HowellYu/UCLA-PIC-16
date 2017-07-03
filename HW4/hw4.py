#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:29:46 2017

@author: howellyu
"""

"""module"""
import math
import re
import matplotlib.pyplot as plt
import numpy as np


"""Q1"""
#import happiness_dict for test
dict_path = "/Users/howellyu/Desktop/happiness_dict.txt"
happiness_file = open(dict_path, 'r').read()
exec(happiness_file)

def happiness(s):
    words=re.findall('\w+',s)
    score=0
    count=0
    for word in words:
        if word in happiness_dictionary.keys():
            score+=happiness_dictionary[word]
            count+=1
    return score/count


the_bells='hear the sledges with the bells silver bells what a world of merriment their melody foretells how they tinkle tinkle tinkle in the icy air of night while the stars that oversprinkle all the heavens seem to twinkle with a crystalline delight keeping time time time in a sort of runic rhyme to the tintinnabulation that so musically wells from the bells bells bells bells bells bells bells from the jingling and the tinkling of the bells'
the_raven='once upon a midnight dreary while i pondered weak and weary over many a quaint and curious volume of forgotten lore while i nodded nearly napping suddenly there came a tapping as of some one gently rapping rapping at my chamber door tis some visitor i muttered tapping at my chamber door only this and nothing more ah distinctly i remember it was in the bleak december and each separate dying ember wrought its ghost upon the floor eagerly i wished the morrow vainly i had sought to borrow from my books surcease of sorrow sorrow for the lost lenore for the rare and radiant maiden whom the angels name lenore nameless here for evermore '

happiness(the_bells)

#article is the string that will be tested.
#n is the number of words tested as the same time.

def story_arc(article, n):
    
    happy_rate = []
    
    #split article into words
    article = re.findall('\w+', article)

    #get the happy_rate of each substring
    temp_str = ""
    index = 0
    i = 0
    while(index + n < len(article)):
        while(i < n):
            temp_str += article[index]
            temp_str += " "
            i += 1
            index += 1
        i = 0
        index -= math.floor(n/2)
        
        #calculate the happiness of this substring
        happy_rate.append(happiness(temp_str))
        
        temp_str = ""
        
    plt.plot(happy_rate, color = "r")
    plt.xlabel("Part of the Story")
    plt.ylabel("Happiness")
    plt.title("Happiness of the Story")
    plt.show()
    return
    

"""Q2"""

story_arc(the_bells, 10)
#
#N is a input matrix
def pagerank(N):

    n = len(N)
    coln_sum = 0

    #add p
    p = 0.1
    #N += p
    N = np.add(N, p)

    #normalize colns
    for i in range(n):
        coln_sum = float(sum(N[:, i]))
        for j in range(n):
            N[j, i] /= coln_sum

    #find the 1st eigenvector
    eigenvectors = np.linalg.eig(N)[1]
    eigenvector = eigenvectors[:, n - 1]

    #normalize the eigenvector we got
    eigenvector /= np.linalg.norm(eigenvector)

    #get the score and ranks
    rank = eigenvector.argsort() + 1
    rank = rank[::-1]

    return eigenvector, rank

"""
#N is a input matrix
def pagerank(N):
    
    n = len(N)
    coln_sum = 0
    
    #add p 
    p = 0.1
    #N += p
    N = np.add(N, p)
    
    #normalize colns
    for i in range(n):
        coln_sum = float(sum(N[:, i]))
        for j in range(n):
            N[j, i] /= coln_sum
    
    #find the 1st eigenvector
    eigenvalue = np.linalg.eig(N)[0]
    eigenvector = np.linalg.eig(N)[1]
    temp = np.where(eigenvalue == 1)
    
    #normalize the eigenvector we got
    eigenvector /= np.linalg.norm(eigenvector)
    
    #get the score and ranks
    eigenvector = abs(eigenvector)
    
    rank = np.argsort(-eigenvector)
    
    return eigenvector, rank
"""                              
    
    
    



    
"""Q3"""
#m_input is the input network
#def: Strength is in-weight
def degree(m_input):
    
    #transform into a matrix
    N = np.array(m_input)
    #N = float(N)
    N = N.astype(float)
    
    #get the dimension of the matrix
    row_len = len(N)
    col_len = len(N[0])
    
    #check whether the matrix is symmetric
    if(row_len != col_len):
        return "row length must equal coln length"
    
    #get the total weight
    strength = [None] * row_len
    for i in range(row_len):
        strength[i] = sum(N[i, :])
    
    strength = np.array(strength)
    #get the rank
    rank = np.argsort(strength)[::-1]
    
    return strength, rank


    
"""Q4"""
#m_input is a matrix 
def comparison(m_input):
    
    strength = list(degree(m_input)[0])
    score = list(pagerank(m_input)[0])
    
    #plot
    plt.scatter(strength, score)
    plt.xlabel("strength")
    plt.ylabel("Score")
    plt.title("Score Vs. Strength")
    plt.legend()
    plt.show()
    
    return


"""Q5"""
#G is a binary network
#v, w are two specified nodes
#k is a natural #
def number_paths(G, v, w, k):
    return np.linalg.matrix_power(np.array(G), k)[w][v]
G=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
v=0
w=3
k=20
number_paths(G, v, w, k)