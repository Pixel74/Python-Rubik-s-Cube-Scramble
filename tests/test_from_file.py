import pytest

from tests.single_input import single_input


@pytest.fixture(scope='package')
def file():
    return "inputs.txt"


@pytest.fixture(scope='package')
def expected_file():

    folder = "expected_results//"

    def gen_string(index):
        return f"{folder}expected_test_file_{index}.csv"

    return gen_string

@pytest.fixture(scope="package")
def gen_img():
    return False


def test_from_file(file, expected_file, gen_img):

    temp = open('diff.csv', 'w')
    temp.close()

    with open(file, "r") as inputs:

        results = {}
        scramble = inputs.readlines()

        for ind, i in enumerate(scramble):
            results[ind] = single_input(i, expected_file(ind), ind, debug=False, gen_img=gen_img)

    if False in results.values():
        assert False
    assert True
