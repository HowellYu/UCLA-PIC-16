#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:25:16 2017

@author: howell
"""

"""HW5"""

#library
import re
import sympy as sp
import math
import sympy.crypto.crypto as crypt
from sympy.solvers.solveset import linsolve
import numpy as np
from sympy.logic.inference import satisfiable
from fractions import Fraction



"""Q1"""
#this function get the number of each element and return a dict
def element_number(term, element):
    storage = {}
    for item in element:
        if item in term:
            storage[item] = 0
            #all the number associated with this element
            fre = re.findall(item + r"([0-9]*)", term)  
            for item2 in fre:
                if item2 == '':
                    storage[item] += 1
                else:
                    #print("item2 is", item2)
                    item2 = int(item2)
                    storage[item] += item2
                
#            elif len(fre) == 0:
#                storage[item] = 0
    return storage

#eq is a string of a unbalanced chemical reaction
#lin_system_eqs = sp.Matrix([[2,1,3], [1,-2,-1]])
def balance(eq):
    
    #find the number of elements in the equation
    terms = 1 + len(re.findall(r"(\+|\=)+", eq))
    
    #get all the element before and after =
    #before = re.findall(r"([0-9a-z]+)", eq)
    before = []
    after = []
    equation = eq.split()
    get_before = True
    for i in range(len(equation)):
        if equation[i] == "=":
            get_before = False
            continue
        if get_before == True and equation[i] != "+":
            before.append(equation[i])
        elif equation[i] != "+":
            after.append(equation[i])
        
    #get the element in the terms
    element_mess = re.findall(r'[A-Z]{1}[a-z]*', eq)
    element = list(set(element_mess))
    element_num = len(element)
    
    #find the # of elements in in each term
    before_list = []
    after_list = []
    for term in before:
        before_list.append(element_number(term, element))
    for term in after:
        after_list.append(element_number(term, element))
    before_len = len(before_list)
    after_len = len(after_list)

    #set up the equation matrix
    M = np.zeros((element_num, terms + 1)) #extra coln of 0 for linear system
    for i in range(element_num):
        current_element = element[i]
#        print(current_element)
        for j in range(terms):
            if(j < before_len): #do not add - 
                if(current_element in before_list[j].keys()):
                    M[i][j] = (before_list[j])[current_element]
            else: #add -
                if(current_element in after_list[j - after_len].keys()):
                    M[i][j] = - (after_list[j - after_len])[current_element]
    
    #now we can solve the linear system
    #linsolve(M)
    a,b,c,d,e,f,g,h,i,j,k,l,m,n = sp.symbols("a,b,c,d,e,f,g,h,i,j,k,l,m,n")
    vari = [a,b,c,d,e,f,g,h,i,j,k,m,n]
    solution = sp.solve_linear_system(sp.Matrix(M), a,b,c,d,e,f,g,h,i,j,k,m,n)
    #solution = linsolve(M, sp.symbols('x0:'+'3', integer = True))
    #solution = sp.solve_linear_system(M, sp.symbols('x0:4'))
    
    #x0,x1,x2,x3,x4,x5,x6,x7 = sp.symbols('x0:8')
    #solution=sp.solve_linear_system(sp.Matrix(M), x0,x1,x2,x3,x4,x5)
    
    vari_used = []
    for letter in vari:
        if letter in solution.keys():
            vari_used.append(letter)
    last_vari = vari[len(vari_used)] #consider the vari not in keys()
    
    #get the coefficient 
    coeffs = []
    for letter in vari_used:
        coeffs.append(solution[letter]/last_vari)
    coeffs.append(1)
    
    #convert the coefficients into fraction 
    fractions = []
    for decimal in coeffs:
        fractions.append(Fraction(str(decimal)).limit_denominator())
    
    #get the denominators
    denominators = []
    for fraction in fractions:
        denominators.append(fraction.denominator)
    denominators = list(set(denominators))
    
    #product of denominators
    product = 1
    for denominator in denominators:
        product *= int(denominator)
    
    #adjust coefficients
    new_coeffs = []
    for fraction in fractions:
        new_coeffs.append(str(int(fraction.numerator*product/
                                  fraction.denominator)))
    
    #assemble the terms
    result = ""
    for i in range(len(before)):
        if new_coeffs[i] == "1": 
            new_coeffs[i] = ""
        if i != 0:  
            result += " + " + new_coeffs[i] + before[i] 
        
        else:
            result += new_coeffs[i] + before[i] 
    result += " = "
    for i in range(len(after)):
        if new_coeffs[i + len(before)] == "1": 
            new_coeffs[i + len(before)] = ""
        if i == 0:
            result += new_coeffs[i + len(before)] + after[i]
        else:
            result += " + " + new_coeffs[i + len(before)] + after[i]
    return result
        
        
#system = Matrix(( (1, 4, 2), (-2, 1, 14)))
#solve_linear_system(system, x, y)
    

    
"""Q2"""
def text_encipher(s, pub_key):
    

    #convert to number m
    m = 0
    for i in range(len(s)):
        m += ord(s[i]) * (128 ** (len(s) - 1 - i))
        
    #use public key to encipher m
    encipher = crypt.encipher_rsa(m, pub_key)
    
    #interprete encioher_m back into a string
    new_encipher = ''
    while encipher > 0:
        temp = chr(encipher % 128)
        new_encipher = temp + new_encipher
        encipher = int((encipher - encipher % 128) / 128)
        
    return new_encipher
    
def text_decipher(t, priv_key):
    #set m to 0 
    m = 0
    
    #reverse the process
    for i in range(len(t)):
        m += ord(t[i]) * (128 ** (len(t) - 1 - i))
    decipher = crypt.decipher_rsa(m, priv_key)
    decipher_new = ''
    while decipher > 0:
        temp = chr(decipher%128)
        decipher_new = temp + decipher_new
        decipher_m = int((decipher_m - decipher_m % 128) / 128)
        
    return decipher_new
                      


"""Q3"""
#this function plot the taylor expension using the first k terms
#k is a integer
def taylor_figure(k):
    
    x = sp.Symbol("x")
    expensions = []
    
    #get the taylor expension of each k
    previous = 0 #previous taylor term
    for i in range(k):
        current = ((-1)**i)*(x**(2*i))/math.factorial(2*i)
        expensions.append(previous + current)
        previous = previous + current #previous taylor term

    #plot
    #original plot
    m_plot = sp.plot(cos(x), xlim = (-2.0,2.0), ylim = (-1.5,1.5), 
                     line_color = 'r', show = False)
    #plot of expension
    for i in range(1, k):
        temp = sp.plot(expensions[i], xlim = (-2.0,2.0), ylim = (-1.5,1.5), 
                            line_color = 'b', show = False)
        m_plot.extend(temp)
    m_plot.show()
    return expensions


"""Q4"""
#expr is an logical expression of x and y
def all_set(expr):
    
    combinations = []
    satisfied = []
    
    #get the true/false combination
    combinations.append({'x': True, 'y': True})
    combinations.append({'x': True, 'y': False})
    combinations.append({'x': False, 'y': True})
    combinations.append({'x': False, 'y': False})
    
    #find the satisfied cases
    for combination in combinations:
        if(expr.subs(combination)):
            satisfied.append(combination)
    return satisfied

all_set((x|y)&(~x|~y))
