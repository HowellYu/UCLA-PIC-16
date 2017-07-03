import numpy as np
from copy import deepcopy
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
# import time as t


""" generate a new number either 2 or 4 """


def new_number():
    temp = np.random.randint(3)

    if temp == 0:
        return new_number()
    else:
        return 2 * temp


""" add a new number to the current matrix """


def add_number(current_matrix):
    temp = True

    while temp:
        x = np.random.randint(4)
        y = np.random.randint(4)
        if current_matrix[x][y] == 0:
            current_matrix[x][y] = new_number()
            temp = False

    return current_matrix


""" reverse the element in the value """


def rev_dict_list(m_dict):
    for num in m_dict.keys():
        m_dict[num] = m_dict[num][::-1]
    return m_dict


""" add the number appear in the same row (transpose False) or coln (transpose True) """


def row_addition(current_matrix, go_up, transpose):
    # use a dict to store the number after row_addition
    storage = {0: [], 1: [], 2: [], 3: []}
    # if go left or right
    if transpose: current_matrix = current_matrix.transpose()
    # if go down
    if not go_up: current_matrix = current_matrix[::-1]

    for i in range(4):
        current_col = current_matrix[:, i]
        # 1 == 2 (and 3 == 4)
        if current_col[0] == current_col[1] and current_col[0] != 0:
            storage[i].append(2 * current_col[0])
            if current_col[2] == current_col[3] and current_col[2] != 0:
                storage[i].append(2 * current_col[2])
            else:
                if current_col[2] != 0:
                    storage[i].append(current_col[2])
                if current_col[3] != 0:
                    storage[i].append(current_col[3])
        # only 2 == 3
        elif current_col[1] == current_col[2] and current_col[1] != 0:
            if current_col[0] != 0:
                storage[i].append(current_col[0])
            storage[i].append(2 * current_col[1])
            if current_col[3] != 0:
                storage[i].append(current_col[3])
        # only 3 == 4
        elif current_col[2] == current_col[3] and current_col[2] != 0:
            if current_col[0] != 0:
                storage[i].append(current_col[0])
            if current_col[1] != 0:
                storage[i].append(current_col[1])
            storage[i].append(2 * current_col[2])
        # 1 == 4:
        elif current_col[0] == current_col[3] and current_col[1] == 0 and current_col[2] == 0 and current_col[0] != 0:
            storage[i].append(2 * current_col[0])
        # 1 == 3:
        elif current_col[0] == current_col[2] and current_col[1] == 0 and current_col[0] != 0:
            storage[i].append(2 * current_col[0])
            if current_col[3] != 0:
                storage[i].append(current_col[3])
        # 2 == 4:
        elif current_col[1] == current_col[3] and current_col[2] == 0 and current_col[1] != 0:
            if current_col[0] != 0:
                storage[i].append(current_col[0])
            storage[i].append(2 * current_col[1])
        # 1 != 2 != 3 != 4
        else:
            if current_col[0] != 0: storage[i].append(current_col[0])
            if current_col[1] != 0: storage[i].append(current_col[1])
            if current_col[2] != 0: storage[i].append(current_col[2])
            if current_col[3] != 0: storage[i].append(current_col[3])
    # convert double to int
    for i in range(4):
        [int(num) for num in storage[i]]
    if go_up:
        return storage
    else:
        return rev_dict_list(storage)


""" add 0's on the top or before the list in a dict """


def add_zeros(m_dict, after):

    for num in m_dict.keys():
        if not after:
            m_dict[num] = m_dict[num][::-1]
        while len(m_dict[num]) != 4:
            m_dict[num].append(0)
        if not after:
            m_dict[num] = m_dict[num][::-1]
    return m_dict


""" move the to the pointed direction (include row/coln addition) """


def movement(current_matrix, direction):

    # adjust go_up and transpose based on the direction
    go_up = True; transpose = False; after = True
    if direction == "Down" or direction == "Right": go_up = False; after = False
    if direction == "Left" or direction == "Right": transpose = True

    # get the dict that store the list of number after the movement
    m_storage = row_addition(current_matrix, go_up, transpose)

    # add 0's to m_storage
    m_storage = add_zeros(m_storage, after)

    # put the list of m_storage into a matrix
    temp_matrix = np.zeros((4, 4))
    for i in range(4):
        temp_matrix[i, :] = m_storage[i]
    if direction == "Left" or direction == "Right":
        return temp_matrix
    else:
        return temp_matrix.transpose()


""" color for different number """


color_dic = {
    0: "yellow",
    2: "LightBlue1",
    4: "SkyBlue1",
    8: "DeepSkyBlue",
    16: "RoyalBlue1",
    32: "RoyalBlue3",
    64: "blue2",
    128: "blue4",
    256: "dark green",
    512: "forest green",
    1024: "lawn green",
    2048: "orange",
    4096: "dark orange",
    8192: "white"
}






