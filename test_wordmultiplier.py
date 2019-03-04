from wordmultiplier import multiplyWords
from hypothesis import given, reject
from hypothesis.strategies import integers, text

@given(text(max_size=5), integers(min_value=0, max_value=10))
def test_combinations(word, number):
    try:
        multiplyWords(word, number)
    except ValueError:
        reject()

def test_simple_multiply():
    assert multiplyWords("hello", 5) == "hellohellohellohellohello"
