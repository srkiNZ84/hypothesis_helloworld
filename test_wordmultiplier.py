from wordmultiplier import multiplyWords
from hypothesis import given, reject
from hypothesis.strategies import integers, text
from string import ascii_lowercase

VALID_WORDS= ascii_lowercase + "_-."

@given(text(alphabet=VALID_WORDS, max_size=10), integers(min_value=0, max_value=10))
def test_combinations(word, number):
    try:
        returnString = multiplyWords(word, number)
        assert len(returnString) == len(word * number)
    except ValueError:
        reject()

@given(text(alphabet=VALID_WORDS, max_size=10), integers(min_value=0, max_value=10))
def test_reverse(word, number):
    try:
        returnString = multiplyWords(word, number)
        assert returnString[::-1][::-1] == returnString
    except ValueError:
        reject()

def test_simple_multiply():
    assert multiplyWords("hello", 5) == "hellohellohellohellohello"
