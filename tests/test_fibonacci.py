import pytest
from utils.number_utils import fibonacci_sequence


test_array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_positive():
    last_num = 9
    assert (fibonacci_sequence(last_num) == test_array[0:last_num])


def test_exception():
    with pytest.raises(ValueError):
        fibonacci_sequence(0)

