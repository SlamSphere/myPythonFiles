from hypothesis import given
import hypothesis.strategies as st


def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False

    for ch in string1:
        if string1.count(ch) != string2.count(ch):
            return False
    return True


# Property: a string is always an anagram of itself
@given(st.text())
def test_string_is_anagram_of_itself(s):
    assert is_anagram(s, s)


# Property: sorting both strings should match anagram result
@given(st.text(), st.text())
def test_sorted_property(a, b):
    assert is_anagram(a, b) == (sorted(a.lower()) == sorted(b.lower()))
