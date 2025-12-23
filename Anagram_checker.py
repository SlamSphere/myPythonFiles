import sys
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
str1_len = len(string1)
str2_len = len(string2)
def check_length(str1_len, str2_len):
    if str1_len != str2_len:
        print("The strings are not anagrams.")
        sys.exit()
index_1 = 0
index_2 = 0
str_range = str1_len - 1
def character_checker(index_1, index_2, str_range):
    while string1[index_1] != string2[index_2]:
        index_2 += 1
        if index_2 > str_range:
            print("The strings are not anagrams.")
            sys.exit()
    return index_2
def anagram_check(index_1, index_2, str_range):
    while index_1 <= str_range:
        index_2 = 0
        character_checker(index_1, index_2, str_range)
        string2.replace(string2[index_2], '', 1)
        index_1 += 1 
    print("The strings are anagrams.")
check_length(str1_len, str2_len)
anagram_check(index_1, index_2, str_range)

