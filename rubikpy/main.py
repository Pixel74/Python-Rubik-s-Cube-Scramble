import numpy as np
import csv
import os
from PIL import Image as Im


class Faces:

    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    def __str__(self):
        print('||' + self.name + '||')
        for lists in self.colors:
            print(lists)
        return ''

    @staticmethod
    def inverted(index):

        if index == 0:
            return 2
        elif index == 1:
            return 1
        elif index == 2:
            return 0
        else:
            raise ValueError


def horizontal_turn(green, red, blue, orange, white, yellow, index, sense):

    # Function for moves like U, U' & D, D'

    temp = []
    if sense == 1:

        for item in green.colors[index]:
            temp.append(item)

        green.colors[index] = red.colors[index].copy()
        red.colors[index] = blue.colors[index].copy()
        blue.colors[index] = orange.colors[index].copy()
        orange.colors[index] = temp.copy()

        if index == 0:
            white.colors = rotate_matrix(white.colors, 1).copy()

        if index == 2:
            yellow.colors = rotate_matrix(yellow.colors, 0).copy()

    if sense == 0:

        for item in green.colors[index]:
            temp.append(item)

        green.colors[index] = orange.colors[index].copy()
        orange.colors[index] = blue.colors[index].copy()
        blue.colors[index] = red.colors[index].copy()
        red.colors[index] = temp.copy()

        if index == 0:
            white.colors = rotate_matrix(white.colors, 0).copy()

        if index == 2:
            yellow.colors = rotate_matrix(yellow.colors, 1).copy()

    del temp


def vertical_turn(green, red, blue, orange, white, yellow, index, sense):

    # Function for moves like L, L' & R, R'

    temp = []
    if sense == 1:

        for lists in green.colors:
            temp.append(lists[index])

        green.colors[0][index] = white.colors[0][index]
        green.colors[1][index] = white.colors[1][index]
        green.colors[2][index] = white.colors[2][index]

        white.colors[0][index] = blue.colors[2][blue.inverted(index)]
        white.colors[1][index] = blue.colors[1][blue.inverted(index)]
        white.colors[2][index] = blue.colors[0][blue.inverted(index)]

        blue.colors[2][blue.inverted(index)] = yellow.colors[0][index]
        blue.colors[1][blue.inverted(index)] = yellow.colors[1][index]
        blue.colors[0][blue.inverted(index)] = yellow.colors[2][index]

        yellow.colors[0][index] = temp[0]
        yellow.colors[1][index] = temp[1]
        yellow.colors[2][index] = temp[2]

        if index == 0:
            orange.colors = rotate_matrix(orange.colors, 1)

        if index == 2:
            red.colors = rotate_matrix(red.colors, 0)

    if sense == 0:

        for lists in green.colors:
            temp.append(lists[index])

        green.colors[0][index] = yellow.colors[0][index]
        green.colors[1][index] = yellow.colors[1][index]
        green.colors[2][index] = yellow.colors[2][index]

        yellow.colors[0][index] = blue.colors[2][blue.inverted(index)]
        yellow.colors[1][index] = blue.colors[1][blue.inverted(index)]
        yellow.colors[2][index] = blue.colors[0][blue.inverted(index)]

        blue.colors[2][blue.inverted(index)] = white.colors[0][index]
        blue.colors[1][blue.inverted(index)] = white.colors[1][index]
        blue.colors[0][blue.inverted(index)] = white.colors[2][index]

        white.colors[0][index] = temp[0]
        white.colors[1][index] = temp[1]
        white.colors[2][index] = temp[2]

        if index == 0:
            orange.colors = rotate_matrix(orange.colors, 0).copy()

        if index == 2:
            red.colors = rotate_matrix(red.colors, 1).copy()

    del temp


def frontal_back_turn(green, red, blue, orange, white, yellow, index, sense):

    # Function for moves like F, F' & B, B'

    temp = []

    if sense == 1:

        if index == 2:

            green.colors = rotate_matrix(green.colors, 1)

            for item in white.colors[2]:
                temp.append(item)

            white.colors[index][0] = orange.colors[2][2]
            white.colors[index][1] = orange.colors[1][2]
            white.colors[index][2] = orange.colors[0][2]

            orange.colors[0][2] = yellow.colors[0][0]
            orange.colors[1][2] = yellow.colors[0][1]
            orange.colors[2][2] = yellow.colors[0][2]

            yellow.colors[0][0] = red.colors[2][0]
            yellow.colors[0][1] = red.colors[1][0]
            yellow.colors[0][2] = red.colors[0][0]

            red.colors[2][0] = temp[2]
            red.colors[1][0] = temp[1]
            red.colors[0][0] = temp[0]

        if index == 0:

            blue.colors = rotate_matrix(blue.colors, 0)

            for item in white.colors[0]:
                temp.append(item)

            white.colors[index][0] = orange.colors[2][0]
            white.colors[index][1] = orange.colors[1][0]
            white.colors[index][2] = orange.colors[0][0]

            orange.colors[0][0] = yellow.colors[2][0]
            orange.colors[1][0] = yellow.colors[2][1]
            orange.colors[2][0] = yellow.colors[2][2]

            yellow.colors[2][0] = red.colors[2][2]
            yellow.colors[2][1] = red.colors[1][2]
            yellow.colors[2][2] = red.colors[0][2]

            red.colors[2][2] = temp[2]
            red.colors[1][2] = temp[1]
            red.colors[0][2] = temp[0]

    if sense == 0:

        if index == 2:

            green.colors = rotate_matrix(green.colors, 0)

            for item in white.colors[2]:
                temp.append(item)

            white.colors[index][0] = red.colors[0][0]
            white.colors[index][1] = red.colors[1][0]
            white.colors[index][2] = red.colors[2][0]

            red.colors[0][0] = yellow.colors[0][2]
            red.colors[1][0] = yellow.colors[0][1]
            red.colors[2][0] = yellow.colors[0][0]

            yellow.colors[0][0] = orange.colors[0][2]
            yellow.colors[0][1] = orange.colors[1][2]
            yellow.colors[0][2] = orange.colors[2][2]

            orange.colors[0][2] = temp[2]
            orange.colors[1][2] = temp[1]
            orange.colors[2][2] = temp[0]

        if index == 0:

            blue.colors = rotate_matrix(blue.colors, 1)

            for item in white.colors[0]:
                temp.append(item)

            white.colors[index][0] = red.colors[0][2]
            white.colors[index][1] = red.colors[1][2]
            white.colors[index][2] = red.colors[2][2]

            red.colors[0][2] = yellow.colors[2][2]
            red.colors[1][2] = yellow.colors[2][1]
            red.colors[2][2] = yellow.colors[2][0]

            yellow.colors[2][0] = orange.colors[0][0]
            yellow.colors[2][1] = orange.colors[1][0]
            yellow.colors[2][2] = orange.colors[2][0]

            orange.colors[0][0] = temp[2]
            orange.colors[1][0] = temp[1]
            orange.colors[2][0] = temp[0]

    del temp


def rotate_matrix(m, sense):

    matrix = np.array(m)
    if sense == 1:

        # Clockwise direction
        return np.rot90(matrix, k=1, axes=(1, 0))

    else:
        return np.rot90(matrix)


def test(green, red, blue, orange, white, yellow, count):

    # For make tests during the development, and print each move in terminal

    print(f"\n+++++NEXT MOVE+++++ {count}\n")

    def print_face(face: Faces):

        for ls in face.colors:
            print(ls)
        print("\n")

    def print_all(*args):

        for face in args:
            print_face(face)

    print_all(green, red, blue, orange, white, yellow)


def make_csv(green, red, blue, orange, white, yellow, filename):

    # Write csv file, for make_img applications and easily implement an auto-solver reading the csv.

    with open(filename, mode='w', newline='') as rubik_csv:
        colors_writer = csv.writer(rubik_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        vcm = '      '

        # Write white face

        colors_writer.writerow(
            [vcm, vcm, vcm, white.colors[0][0], white.colors[0][1], white.colors[0][2], vcm, vcm, vcm, vcm, vcm, vcm])
        colors_writer.writerow(
            [vcm, vcm, vcm, white.colors[1][0], white.colors[1][1], white.colors[1][2], vcm, vcm, vcm, vcm, vcm, vcm])
        colors_writer.writerow(
            [vcm, vcm, vcm, white.colors[2][0], white.colors[2][1], white.colors[2][2], vcm, vcm, vcm, vcm, vcm, vcm])

        # Write orange, green, red and blue

        colors_writer.writerow([orange.colors[0][0], orange.colors[0][1], orange.colors[0][2], green.colors[0][0],
                                green.colors[0][1], green.colors[0][2], red.colors[0][0], red.colors[0][1],
                                red.colors[0][2], blue.colors[0][0], blue.colors[0][1], blue.colors[0][2]])
        colors_writer.writerow([orange.colors[1][0], orange.colors[1][1], orange.colors[1][2], green.colors[1][0],
                                green.colors[1][1], green.colors[1][2], red.colors[1][0], red.colors[1][1],
                                red.colors[1][2], blue.colors[1][0], blue.colors[1][1], blue.colors[1][2]])
        colors_writer.writerow([orange.colors[2][0], orange.colors[2][1], orange.colors[2][2], green.colors[2][0],
                                green.colors[2][1], green.colors[2][2], red.colors[2][0], red.colors[2][1],
                                red.colors[2][2], blue.colors[2][0], blue.colors[2][1], blue.colors[2][2]])

        # Write yellow

        colors_writer.writerow(
            [vcm, vcm, vcm, yellow.colors[0][0], yellow.colors[0][1], yellow.colors[0][2], vcm, vcm, vcm, vcm, vcm,
             vcm])
        colors_writer.writerow(
            [vcm, vcm, vcm, yellow.colors[1][0], yellow.colors[1][1], yellow.colors[1][2], vcm, vcm, vcm, vcm, vcm,
             vcm])
        colors_writer.writerow(
            [vcm, vcm, vcm, yellow.colors[2][0], yellow.colors[2][1], yellow.colors[2][2], vcm, vcm, vcm, vcm, vcm,
             vcm])


def make_img(csv_colors):

    colors_index = {'orange': 'Orange Title.jpg', 'green ': 'Green Title.jpg', 'red   ': 'Red Title.jpg',
                    'blue  ': 'Blue Title.jpg', 'white ': 'White Title.jpg', 'yellow': 'Yellow Title.jpg',
                    '      ': 'Black Title.jpg'}

    with open(csv_colors, 'r') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        current_y = 0
        first_open = True

        for row in csv_reader:

            current_x = 0

            for item in row:

                if first_open:

                    img_background = Im.open(os.path.join('..', 'media', 'White Background.jpg'))
                    first_open = False

                else:
                    img_background = Im.open(os.path.join('..', 'output', '-----Final-----.jpg'))

                img_color = Im.open(os.path.join('..', 'media', colors_index[item]))
                img_background.paste(img_color, (current_x, current_y))
                img_background.save(os.path.join('..', 'output', '-----Final-----.jpg'))

                img_color.close()
                img_background.close()

                current_x += 52

            current_y += 52


def reset_csv_img():

    # Reset img
    clear_img = Im.open(os.path.join('..', 'media', 'Reset_cube.jpg'))
    clear_img.save(os.path.join('..', 'output', '-----Final-----.jpg'))
    clear_img.close()

    # Reset csv
    clear_csv = open('..//output//Final Rubik Cube.csv', "w")
    clear_csv.close()


def set_default_faces():

    f_up = [["white ", "white ", "white "], ["white ", "white ", "white "], ["white ", "white ", "white "]]
    f_down = [["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"]]
    f_left = [["orange", "orange", "orange"], ["orange", "orange", "orange"], ["orange", "orange", "orange"]]
    f_right = [["red   ", "red   ", "red   "], ["red   ", "red   ", "red   "], ["red   ", "red   ", "red   "]]
    f_front = [["green ", "green ", "green "], ["green ", "green ", "green "], ["green ", "green ", "green "]]
    f_back = [["blue  ", "blue  ", "blue  "], ["blue  ", "blue  ", "blue  "], ["blue  ", "blue  ", "blue  "]]

    green = Faces('green', f_front)
    red = Faces('red', f_right)
    blue = Faces('blue', f_back)
    orange = Faces('orange', f_left)
    white = Faces('white', f_up)
    yellow = Faces('yellow', f_down)

    return green, red, blue, orange, white, yellow


def make_scramble(sc_input='', print_moves=False, gen_img=True):

    reset_csv_img()
    green, red, blue, orange, white, yellow = set_default_faces()

    if type(sc_input) == str:
        each_move = sc_input.split()
    elif type(sc_input) == list:
        each_move = sc_input
    else:
        each_move = []

    count = 0

    for ch in each_move:

        if ch == "U":
            index = 0
            sense = 1
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "U'":
            index = 0
            sense = 0
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "U2":
            index = 0
            sense = 1
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "D":
            index = 2
            sense = 0
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "D'":
            index = 2
            sense = 1
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "D2":
            index = 2
            sense = 0
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)
            horizontal_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "L":
            index = 0
            sense = 1
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "L'":
            index = 0
            sense = 0
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "L2":
            index = 0
            sense = 1
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "R":
            index = 2
            sense = 0
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "R'":
            index = 2
            sense = 1
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "R2":
            index = 2
            sense = 0
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)
            vertical_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "F":
            index = 2
            sense = 1
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "F'":
            index = 2
            sense = 0
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "F2":
            index = 2
            sense = 1
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "B":
            index = 0
            sense = 0
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "B'":
            index = 0
            sense = 1
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if ch == "B2":
            index = 0
            sense = 0
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)
            frontal_back_turn(green, red, blue, orange, white, yellow, index, sense)

        if print_moves:
            count += 1
            test(green, red, blue, orange, white, yellow, count)

    filepath = '..//output//Final Rubik Cube.csv'

    make_csv(green, red, blue, orange, white, yellow, filename=filepath)

    if gen_img:
        make_img(csv_colors=filepath)


if __name__ == '__main__':

    string_input = input('Insert a scramble: ')

    if 'auto' in string_input[:5]:

        from scramble_generator import scramble_generator

        str_scramble = scramble_generator(int(string_input[4:]))
        make_scramble(str_scramble, print_moves=True, gen_img=False)

    else:
        make_scramble(string_input, print_moves=True, gen_img=False)
