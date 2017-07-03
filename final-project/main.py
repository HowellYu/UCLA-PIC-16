from function import *

root = Tk()
root.title("Game 2048")
my_canvas1 = Canvas(root, bg="indian red", width=600, height=100)  # upper canvas
my_canvas2 = Canvas(root, bg="lavender blush", width=600, height=600)
my_canvas1.pack()
my_canvas2.pack()


""" draw the background canvas"""

x, y, z, w = 106, 106, 194, 194
my_canvas1.create_text(300, 60, fill="black", text="2048", font=("Verdana", 45), tag="title")
my_canvas2.create_rectangle(x-20, y-20, z + 320, w + 320, fill="sienna", outline="sienna", tag="rect1")


""" display function """


def display(m_matrix):

    my_canvas2.delete("rect2")
    my_canvas2.delete("text")
    for i in range(4):
        for j in range(4):
            value = int(m_matrix[i][j])
            my_canvas2.create_rectangle(x + j * 100, y + i * 100, z + j * 100, w + i * 100, fill=color_dic[value],
                                        outline=color_dic[value], tag="rect2")
            if value >= 2:
                my_canvas2.create_text((x + z + j * 200) / 2, (y + w + i * 200) / 2, fill="black", text=str(value),
                                       font=("Impact", 30), tag="text")


""" check whether reaches 2048 """


def check_2048(m_matrix, already_2048):

    if not already_2048:
        for i in range(4):
            for j in xrange(4):
                if m_matrix[i][j] == 2048:
                    win_note = Label(root, text="Reached 2048", bg="orange red", fg="white", font=("Verdana", 24))
                    win_note.pack()
                    b2 = Button(root, text="Exit", width=20, height=5, bg="orange red", fg="white",
                                font=("Verdana", 20), command=root.destroy)
                    b2.pack()
                    return True
                else:
                    return False
    return True

""" check whether there are valid moves remaining """


def game_over(m_matrix):

    temp1_matrix = deepcopy(m_matrix); temp2_matrix = deepcopy(m_matrix)
    temp3_matrix = deepcopy(m_matrix); temp4_matrix = deepcopy(m_matrix)
    # try moves to different direction
    temp1, temp2 = movement(temp1_matrix, "Up"), movement(temp2_matrix, "Down")
    temp3, temp4 = movement(temp3_matrix, "Right"), movement(temp4_matrix, "Left")
    if np.array_equal(temp1, temp2) and np.array_equal(temp2, temp3) and np.array_equal(temp3, temp4):
        print('No more valid moves!')
        return True
    return False

start_matrix = np.zeros((4, 4))
# start_matrix[0][0] = 1024
# start_matrix[0][1] = 1024
# start_matrix[2][1] = 2048
start_matrix
start_matrix
current_matrix = add_number(start_matrix)
current_matrix = add_number(start_matrix)  # start with 2 numbers
display(current_matrix)
reached_2048 = False


""" associate pressed keys with variable up/down/right/left
    (Also the main function)
"""


def pressed(event):

    # first check whether game over
    if game_over(current_matrix):
        return

    pressed_keys = event.keysym
    if pressed_keys in ["Up", "Down", "Right", "Left"]:
        global current_matrix
        old_matrix = deepcopy(current_matrix)  # if the matrix stays the same after the movement, we don't add.
        print("pressed:", pressed_keys)
        current_matrix = movement(current_matrix, pressed_keys)
        # display after entering a direction
        if not (np.array_equal(current_matrix, old_matrix)):
            # add a new number to the matrix
            current_matrix = add_number(current_matrix)

        display(current_matrix)
    if game_over(current_matrix):
        my_canvas2.create_text(300, 550, fill="black", text="Game Over!",
                               font=("Verdana", 30), tag="text")
        b1 = Button(root, text="Exit", width=20, height=5, bg="orange red", fg="white",
                    font=("Verdana", 20), command=root.destroy)
        if not reached_2048:
            b1.pack()

    # check whether reached 2048
    global reached_2048
    reached_2048 = check_2048(current_matrix, reached_2048)

root.bind_all('<Key>', pressed)  # bind keys together

root.mainloop()




