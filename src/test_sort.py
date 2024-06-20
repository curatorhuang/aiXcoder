def test_merge_sorted_lists():
    left = [1, 3, 5, 7]
    right = [2, 4, 6, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge(left, right) == expected


def test_merge_with_empty_lists():
    left = []
    right = []
    expected = []
    assert merge(left, right) == expected


def test_merge_with_one_empty_list():
    left = [1, 2, 3]
    right = []
    expected = [1, 2, 3]
    assert merge(left, right) == expected

    left = []
    right = [1, 2, 3]
    assert merge(left, right) == expected


def test_merge_with_unequal_length_lists():
    left = [1, 2, 3]
    right = [4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert merge(left, right) == expected

    left = [1, 2, 3, 4, 5]
    right = [6]
    assert merge(left, right) == expected


def test_merge_with_same_elements():
    left = [1, 2, 3, 4, 5]
    right = [5, 4, 3, 2, 1]
    expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert merge(left, right) == expected


def test_merge_with_duplicates_in_one_list():
    left = [1, 2, 2, 3, 4]
    right = [5, 6, 7]
    expected = [1, 2, 2, 3, 4, 5, 6, 7]
    assert merge(left, right) == expected


def test_merge_reverse_sorted_lists():
    left = [8, 6, 4, 2]
    right = [7, 5, 3, 1]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge(left, right) == expected
