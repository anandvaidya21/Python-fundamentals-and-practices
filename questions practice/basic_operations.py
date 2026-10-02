text = input("enter string: ")

vowels = 0
consonants = 0
digits = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1
        
    elif char.isalpha():
        consonants += 1
        
    elif char.isdigit():
        digits += 1

print("vowels: ", vowels)
print("consonants: ", consonants)
print("digits: ", digits)