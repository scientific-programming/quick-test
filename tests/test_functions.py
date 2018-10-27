from quicktest import square


def test_square_positive_integers():
    assert square(1) == 1
    assert square(2) == 4
    assert square(4) == 16
    assert square(100) == 10000
    assert 2 == 1
