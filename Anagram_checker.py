import sys
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string1 = string1.lower()
string2 = string2.lower()
str1_len = len(string1)
str2_len = len(string2)
if str1_len != str2_len:
    print("The strings are not anagrams.")
    sys.exit()
place1 = 0
place2 = 0
str_range = str1_len - 1
while place1 <= str_range:
    while string1[place1] != string2[place2]:
        place2 += 1
        if place2 > str_range:
            print("The strings are not anagrams.")
            sys.exit()
    string2 = string2.replace(string2[place2], '', 1)
    place2 = 0
    place1 += 1 
print("The strings are anagrams.")
