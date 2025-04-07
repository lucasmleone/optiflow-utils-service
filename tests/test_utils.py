from src.utils import safe_division, remove_duplicates
def test_safe_division_normal():
    assert safe_division(10, 2) == 5.0

def test_safe_division_zero():
    assert safe_division(10, 0) == "Error: división por cero"

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3 ,4]) == {1, 2, 3, 4}

