#count vowels
text = input("Enter the string")

vowels="aeiou"
count =0

for char in text.lower():
    if char in vowels:
        count +=1
print("input name:-",text,"vowels: ", count)