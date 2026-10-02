str1 = input("enter first string: ")
str2 = input("enter second string ")

if sorted(str1) == sorted(str2):
    print("anagram")
else:
    print("not anagram")