import pytest

from rubikpy.main import make_scramble

def single_input(given_input, expected_file, n_test=0, debug=False):

    make_scramble(given_input, debug)


    with open('..//output//Final Rubik Cube.csv', 'r') as output, open(expected_file, 'r') as expected:
        fileone = output.readlines()
        filetwo = expected.readlines()

    flag = True

    with open('diff.csv', 'a') as outFile:

        outFile.write(f"{n_test}. --------------------------------------------------------------------------------------\n")

        for ind, line in enumerate(filetwo):
            if line not in fileone:

                outFile.write(f"--({ind}) {line}")
                flag = False

    return flag