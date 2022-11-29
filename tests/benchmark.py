import cProfile
import pstats


def gen_img():
    return False


def given_input():
    # L F
    return "L F L' F D2 F' D' L' B F D' B2 D' U R' D2 U L' B R2 B D' L' F R2 U' R D2 B U R' L2 F R2 L' D2 F2 B' U' F2 " \
           "U R2 L B2 L R' D' U2 B2 D' L' F D F2 B2 R' F2 B L2 U F' U F B2 R' U2 D' F2 L2 B' D2 B L D' U L' F B U' B2 " \
           "L2 D' B2 F' R' D F L' R2 B' R' D' L U2 F L2 R2 F2 R' L "


def expected_input():
    return 'expected_results//expected_test_input.csv'


cProfile.run("test_input(given_input(), expected_input(), gen_img())", "test_input_benchmark")


def file():
    return "inputs.txt"


def expected_file():
    folder = "expected_results//"

    def gen_string(index):
        return f"{folder}expected_test_file_{index}.csv"

    return gen_string


cProfile.run("test_from_file(file(), expected_file(), gen_img())", "test_file_benchmark")

# cumtime, ncalls

p = pstats.Stats("test_input_benchmark")
p.strip_dirs().sort_stats('cumtime').print_stats()

b = pstats.Stats("test_file_benchmark")
b.strip_dirs().sort_stats('cumtime').print_stats()
