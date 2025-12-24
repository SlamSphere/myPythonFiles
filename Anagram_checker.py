import sys

def check_length(string1, string2):
    if len(string1) != len(string2):
        print("The strings are not anagrams.")
        sys.exit()

def anagram_check(string1, string2):
    for char in string1:
        if char in string2:
            string2 = string2.replace(char, '', 1)
        else:
            print(f"The strings: {string1} and {string2} are not anagrams.")
            sys.exit()
    print(f"The strings: {string1} and {string2} are anagrams.")

string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

check_length(string1, string2)
anagram_check(string1, string2)