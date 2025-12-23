import sys
import unittest
def is_anagram(string1, string2):
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
        while place2 < str2_len:
            if string1[place1] == string1[place2]:
                count1 += 1
            if string1[place1] == string2[place2]:
                count2 += 1
            place2 += 1
        if count1 != count2:
            return False
        place1 += 1
    return True
class TestAnagram(unittest.TestCase):
    def test_simple_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
    def test_not_anagram(self):
        self.assertFalse(is_anagram("hello", "world"))
    def test_different_lengths(self):
        self.assertFalse(is_anagram("cat", "cats"))
    def test_same_word(self):
        self.assertTrue(is_anagram("dog", "dog"))
    def test_case_insensitive(self):
        self.assertTrue(is_anagram("School", "cHools"))
    def test_single_character(self):
        self.assertTrue(is_anagram("a", "a"))
    def test_empty_strings(self):
        self.assertTrue(is_anagram("Saket Hi", "Hi Saket"))
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnagram)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
print("Running unit tests...\n")
run_tests()
print("\nAnagram Checker\n")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
