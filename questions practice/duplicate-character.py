text = "programming"

frequency ={}

for char in text:
    
    frequency[char] = frequency.get(char,0) +1

for  char, count in frequency.items():
    
    if count > 1:
        print(char,count)