#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:05:52 2017

@author: Howell
""" 


#Q1    
def divide(a, b, k):
    #check valid k input
    if(k%1 != 0 or k < 0):
        print("Invalid input. k has to be non-negative whole number!")
        return
    elif(a < 0 or b < 0):
        print("Invalid input. a and b have to be positive number!")
        return 

    #rounding
    temp = a*b**(-1)
    temp *= 10**k

    #check 1 more digit to determine carry (+1)
    if(temp-int(temp) < 0.5):
        result = int(temp)*(10**k)**(-1)
    else:
        result = int(temp + 1)*(10**k)**(-1)
    
    #just in case we have a computing error. 
    int_len = len(str(int(result)))
    total_len = int_len + k
    result = str(result)
    new_result = ""
    
    for i in range(total_len + 1):
        new_result += result[i]
    new_result = float(new_result)
    
    return new_result    
    
    

#Q2
def check_leap(Y): #check whether this year is leap year
    #check century year
    if(Y%100 == 0):
        if(Y%400 == 0):
            leap = True
        else:
            leap = False
    
    #check normal year
    elif(Y%4 == 0):
        leap = True
    else:
        leap = False
    return leap


    
#range: since the start of the century 
def weekday(M, D, Y):
    #check the input year
    if(Y < 100 or Y%1 != 0): 
        print("Invalid input of year.")
        return 
     
    #check the input month
    if(M < 1 or M > 12 or M%1 != 0): 
        print("Invalid input of month.")
        return 

    #check the input date. 

    if(D < 1 or D%1 != 0): print("Invalid input of day!"); return;
    elif(D > 31 and M == 1): print("Invalid input of day!"); return; 
    elif(D > 31 and M == 3): print("Invalid input of day!"); return;
    elif(D > 30 and M == 4): print("Invalid input of day!"); return;
    elif(D > 31 and M == 5): print("Invalid input of day!"); return;
    elif(D > 30 and M == 6): print("Invalid input of day!"); return;
    elif(D > 31 and M == 7): print("Invalid input of day!"); return;
    elif(D > 31 and M == 8): print("Invalid input of day!"); return;
    elif(D > 30 and M == 9): print("Invalid input of day!"); return;
    elif(D > 31 and M == 10): print("Invalid input of day!"); return;
    elif(D > 30 and M == 11): print("Invalid input of day!"); return;
    elif(D > 31 and M == 12): print("Invalid input of day!"); return;
    
    #consider the leap year
    elif (M == 2):
        if(check_leap(Y)):
            if(D > 29):
                print("Invalid input of day!")
                return
        else:
            if(D > 28):
                print("Invalid input of day!")
                return 
    
    #Schwerdtfeger's method
    #https://www.wikiwand.com/en/Determination_of_the_day_of_the_week#/Schwerdtfeger.27s_method
    #calculate c
    if (M >= 3):
        c = int(Y/100)
        g = Y - 100*c
    elif (M < 3):
        c = int((Y-1)/100)
        g = Y - 1 - 100*c 
    
    #calculate e
    if(M == 1): e=0
    elif(M == 2): e=3
    elif(M == 3): e=2
    elif(M == 4): e=5
    elif(M == 5): e=0
    elif(M == 6): e=3
    elif(M == 7): e=5
    elif(M == 8): e=1
    elif(M == 9): e=4
    elif(M == 10): e=6
    elif(M == 11): e=2
    elif(M == 12): e=4
    
    #calculate f
    if(c%4 == 0): f = 0
    elif(c%4 == 1): f = 5
    elif(c%4 == 2): f = 3
    elif(c%4 == 3): f = 1
    
    #calculate weekday 
    w = (D + e + f + g + int(g/4))%7
    if(w == 0): return "Sunday" 
    elif(w == 1): return "Monday"
    elif(w == 2): return "Tuesday"
    elif(w == 3): return "Wednesday"
    elif(w == 4): return "Thursday"
    elif(w == 5): return "Friday"
    elif(w == 6): return "Saturday"


    
#Q3
#flip n coins from a list input_list 
def flip_coin(input_list, n):
    my_list = input_list
    for i in range(n):
        if(my_list[i] == 1):
            my_list[i] = 0
        else:
            my_list[i] = 1
    return my_list

#move n coins from table1 to table2 
def move_coin(table1, table2, n):
    i = 0
    while(i != n):
        table2.append(table1[i])
        table1.pop(i)
        i += 1
    return 



#test function
def tables(L):
    table1 = L
    table2 = []
    move_coin(table1, table2, sum(table1))
    flip_coin(table2, len(table2))
    if(sum(table1) == sum(table2)): 
        print("Same number of 1's!")
        print("Both table1 and table2 have", sum(table1), "number of 1's")
    return table1, table2

#test 
#create table L 
import random
L=[0]*100
for i in random.sample(range(100),20): L[i]=1
[L1,L2]=tables(L)
L1.count(1)
L2.count(1)
    

    
#Q4
def longestpath(my_dict):
    
    path = 0
    max_path = 0
    
    #for loop for each key
    for item in my_dict:
        
        #storage to store the key that have gone through
        storage = []
        storage.append(item)
        path = 1
        new_key = my_dict[item]
        #find the length of the path
        
        while(new_key in my_dict.keys() and new_key != my_dict[new_key] and new_key not in storage):
            
            #count
            path += 1
            storage.append(new_key)
            new_key = my_dict[new_key]
            
        #update max_path
        max_path = max(max_path, path)
    return max_path   
    
dic1={1:2, 2:3, 3:4}
dic2={1:2, 2:3, 3:5, 5:7}
dic3={1:'a', 'a':3, 4:5, 5:20, 20:19, 19:18, 18:17, 16:'a'}
dic4={1:2, 2:2}   

longestpath(dic1)
longestpath(dic2)
longestpath(dic3)
longestpath(dic4)


    
#Q5
import random

#First generate a fair coin. 
def fair_coin():
    return random.randint(0, 1)

#Now generate a unfair coin using the fair_coint() above. 
def biasedflip():
    
    round1 = fair_coin()
    round2 = fair_coin()
    
    #if (1,1), return 1
    #if (1,0) or (0,1), return 0
    #if (0,0), flip twice again
    if(round1 == 1 and round2 == 1):
        return 1
    if(round1 + round2 == 1):
        return 0
    else:
        #flip again
        return biasedflip() 

#Now run a simulation to test whether the success rate is 1/3
def coin_simulation(n): 
    
    sum = 0
    
    for i in range(n):
        sum += biasedflip()
    return sum/n

print(coin_simulation(10000)) #around 0.333







#TEST BOX

#Challenge 1
divide(20,7,6)

#Challenge 2
weekday(5,4,1987)
weekday(12,10,1815)
weekday(3,2,2078)

#Challenge 3
L=[0]*100
for i in random.sample(range(100),20):
    L[i]=1
[L1,L2]=tables(L)
L1.count(1)
L2.count(1)

#Challenge 4
dic1={1:2,2:3,3:4}
dic2={1:2,2:3,3:5,5:1}
dic3={1:'a','a':3,4:5,5:20.01,20.01:19,19:18,18:17,16:'a'}
dic4={1:2,2:2}

#Challange 5
S=[]
for i in range(1000):
    S=S+[biasedflip()]
S.count(1)/len(S)
