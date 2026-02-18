import pytest

@pytest.fixture
def coordinates():
    return (10, 20)

@pytest.fixture
def rgb():
    return (255, 128, 0)

def test_indexing(coordinates):
    assert coordinates[0] == 10
    assert coordinates[1] == 20

def test_slicing(rgb):
    sliced = rgb[1:]
    assert sliced == (128, 0)

def test_immutability(coordinates):
    with pytest.raises(TypeError):
        coordinates[0] = 15

def test_single_element_tuple():
    single = (42,)
    assert len(single) == 1
    assert isinstance(single, tuple)

def test_length(coordinates, rgb):
    assert len(coordinates) == 2
    assert len(rgb) == 3

def test_count():
    numbers = (1, 2, 3, 2, 1, 2)
    assert numbers.count(2) == 3

def test_index(rgb):
    assert rgb.index(128) == 1

def test_unpacking(coordinates):
    x, y = coordinates
    assert x == 10
    assert y == 20

def test_concatenation(coordinates, rgb):
    combined = coordinates + rgb
    assert len(combined) == 5
    assert combined[0] == 10

def test_repetition():
    repeated = (1, 2) * 3
    assert repeated == (1, 2, 1, 2, 1, 2)

def test_in_operator(coordinates):
    assert 10 in coordinates
    assert 100 not in coordinates

def test_nested_tuple():
    nested = ((1, 2), (3, 4))
    assert nested[0] == (1, 2)
    assert nested[0][1] == 2
