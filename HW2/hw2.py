#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:09:01 2017

@author: howell
"""
import re #regular expression library


#Q1
#check integers, floats, strings, and lists
#input: my_input is a string
def mytype(my_input):
    
    my_input = str(my_input)
    
    #check list
    match = re.search(r'\[.*\]', my_input)
    if match:
        return "list"

    #check floats
    match = re.search(r'[0-9]\.[0-9]', my_input)
    if match: 
        return "float"
        
    #check integers
    match = re.search(r'[0-9]', my_input)
    if match:
        return "int"

    #else: return string    
    return "str"

    
 
#Q2
#input: file_list is a list containing all the filenames. 
def findpdfs(file_list):
    
    names = []
    
    for item in file_list:
        name = re.findall('(.+)\..+', item)
        extension = re.findall('.+\.(.+)', item)
        if extension[0] == 'pdf':
            names.append(name[0])
    return names


#Q3
#“Firstname Lastname” -> “Lastname, Firstname”
#“Firstname Lastname” -> “Lastname, Firstname M.”
def names(input_name):
    
    #first name
    FirstName = re.search(r"^[A-Z]{1}[a-z]*", input_name)
    
    #last name
    LastName = re.search(r"[A-Z]{1}[a-z]*$", input_name)
    
    #middle initial 
    MiddleInitial = re.search("\s([A-Z]{1})[a-z]*\s", input_name)
    
    if MiddleInitial is None: 
        return (LastName.group() + ", " + FirstName.group())

    return (LastName.group() +", " + FirstName.group() + ' ' + 
            MiddleInitial.group(1) + '.')#group(1) uses regex
        
#Q4
import urllib
def findemail(URL):
    
    #get the info of the URL
    txt = urllib.request.urlopen(URL).read()
    txt = str(txt)
    
    #regular extraction
    email = re.findall(r"[\w\.\-]*@[\w\.\-]+\.[a-z]+", txt) #use b to decode byte to string
    return email

#Q5

#we can get the path of the happiness_dict outside our function. 
dict_path = input("Local happiness_dict path: ")
happiness_dict = exec(open(dict_path, 'r').read())

#calculate our happiness
def happiness(text):
    text = ' ' + text
    words = re.findall(r'(?:\s|"){1}([a-z0-9\:]+)', text)

    #calculate the happiness
    happiness = 0
    for word in words:
        if word in happiness_dictionary:
            happiness += happiness_dictionary[word]
    return happiness


#test
#Q1
a=2; b=3.04; c='abc'; d=[1,2]; e=['a','b']; f=[]
mytype(a)
mytype(b)
mytype(c)
mytype(d)
mytype(e)
mytype(f)

#Q2
filenames=['hello.py', 'image.img', 'pdf.py', 'book.pdf', 'weirdfile.pdf5']
findpdfs(filenames)

#Q3
names('Susie Rombach')
names('Susie Badger Rombach')

#Q5
the_bells='hear the sledges with the bells silver bells what a world of merriment their melody foretells how they tinkle tinkle tinkle in the icy air of night while the stars that oversprinkle all the heavens seem to twinkle with a crystalline delight keeping time time time in a sort of runic rhyme to the tintinnabulation that so musically wells from the bells bells bells bells bells bells bells from the jingling and the tinkling of the bells'
the_raven='once upon a midnight dreary while i pondered weak and weary over many a quaint and curious volume of forgotten lore while i nodded nearly napping suddenly there came a tapping as of some one gently rapping rapping at my chamber door tis some visitor i muttered tapping at my chamber door only this and nothing more ah distinctly i remember it was in the bleak december and each separate dying ember wrought its ghost upon the floor eagerly i wished the morrow vainly i had sought to borrow from my books surcease of sorrow sorrow for the lost lenore for the rare and radiant maiden whom the angels name lenore nameless here for evermore '
happiness(the_bells)
happiness(the_raven)