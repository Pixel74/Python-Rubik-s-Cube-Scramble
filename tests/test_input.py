import pytest
from tests.single_input import single_input

#This scramble should give the result in expected_test_input.csv
@pytest.fixture(scope='package')
def given_input():
    #U' L2
    return "U' L2 R' F' D' F2 U D' B2 R2 B' U2 F' U2 F R2 D U B2 F2 R D2 F2 U B'"

@pytest.fixture(scope='package')
def expected_input():
    return 'expected_results//expected_test_input.csv'

def test_input(given_input, expected_input):

    temp = open('diff.csv', 'w')
    temp.close()

    assert single_input(given_input, expected_input, debug=False) == True
