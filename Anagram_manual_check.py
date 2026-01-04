def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False

    for ch in string1:
        if string1.count(ch) != string2.count(ch):
            return False
    return True


test_data = [
    ("listen", "silent", True),
    ("evil", "Evil", True),
    ("triangle", "integral", True),
    ("hello", "world", False),
    ("test", "tests", False),
    ("aabb", "abbb", False),
    ("dog", "dog", True),
]


def run_tests():
    passed = 0
    for a, b, expected in test_data:
        result = is_anagram(a, b)
        if result == expected:
            print(f"PASS: {a}, {b}")
            passed += 1
        else:
            print(f"FAIL: {a}, {b} (got {result})")

    print(f"\n{passed}/{len(test_data)} tests passed")


if __name__ == "__main__":
    run_tests()
