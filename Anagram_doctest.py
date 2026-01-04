def is_anagram(string1, string2):
    """
    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("evil", "Evil")
    True
    >>> is_anagram("triangle", "integral")
    True
    >>> is_anagram("hello", "world")
    False
    >>> is_anagram("test", "tests")
    False
    >>> is_anagram("aabb", "abbb")
    False
    >>> is_anagram("dog", "dog")
    True
    """
    string1 = string1.lower()
    string2 = string2.lower()
    str1_len = len(string1)
    str2_len = len(string2)

    if str1_len != str2_len:
        return False

    place1 = 0
    while place1 < str1_len:
        count1 = 0
        count2 = 0
        place2 = 0
        while place2 < str1_len:
            if string1[place1] == string1[place2]:
                count1 += 1
            if string1[place1] == string2[place2]:
                count2 += 1
            place2 += 1
        if count1 != count2:
            return False
        place1 += 1
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
