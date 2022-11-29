from rubikpy.main import make_scramble


def single_input(given_input, expected_file, n_test=0, debug=False, gen_img=False):

    make_scramble(given_input, debug, gen_img)

    with open('..//output//Final Rubik Cube.csv', 'r') as output, open(expected_file, 'r') as expected:

        file_one = output.readlines()
        file_two = expected.readlines()

    flag = True

    with open('diff.csv', 'a') as out_file:

        out_file.write(f"{n_test}. --------------------------------------------------------------------------------------\n")

        for ind, line in enumerate(file_two):

            if line not in file_one:
                out_file.write(f"--({ind}) {line}")
                flag = False

    return flag
