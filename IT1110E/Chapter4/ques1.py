def to_uppercase(string):
    count = 0 
    i = 0
    while i < 4 and i < len(string):
        if string[i].isupper():
            count += 1
        i += 1
    
    if count >= 2:
        return string.upper()
    else: return string
    
print(to_uppercase('aBz    da@s hi'))