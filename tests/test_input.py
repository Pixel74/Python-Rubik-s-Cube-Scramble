import pytest

from tests.single_input import single_input


# This scramble should give the result in expected_test_input.csv
@pytest.fixture(scope='package')
def given_input():
    # L F
    return "L F L' F D2 F' D' L' B F D' B2 D' U R' D2 U L' B R2 B D' L' F R2 U' R D2 B U R' L2 F R2 L' D2 F2 B' U' F2 " \
           "U R2 L B2 L R' D' U2 B2 D' L' F D F2 B2 R' F2 B L2 U F' U F B2 R' U2 D' F2 L2 B' D2 B L D' U L' F B U' B2 " \
           "L2 D' B2 F' R' D F L' R2 B' R' D' L U2 F L2 R2 F2 R' L "


@pytest.fixture(scope='package')
def expected_input():
    return 'expected_results//expected_test_input.csv'


@pytest.fixture(scope="package")
def gen_img():
    return False


def test_input(given_input, expected_input, gen_img):
    temp = open('diff.csv', 'w')
    temp.close()

    assert single_input(given_input, expected_input, debug=False, gen_img=gen_img)
