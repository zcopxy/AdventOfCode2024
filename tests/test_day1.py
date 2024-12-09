from days.day1 import day1_1


LIST_1 = [3, 4, 2, 1, 3, 3]
LIST_2 = [4, 3, 5, 3, 9, 3]


def test_day1_1():
    expected_result = 11
    assert day1_1(LIST_1, LIST_2) == expected_result