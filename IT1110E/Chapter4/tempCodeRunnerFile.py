string = input()
string = string.lower()

s_dict = dict()

res = '' if string[0] != " " else ' '
# True if is char 
# False if is space
curr = True if string[0] != " " else False
for char in string:
    if curr == True and char != " ":
        if s_dict.get(char) == None:
            res += char
            s_dict[char] = 1
    elif curr == True and char == " ":
        s_dict.clear()
        curr = False
        res += char
    elif curr == False and char != " ":
        curr = True
        if s_dict.get(char) == None:
            res += char
            s_dict[char] = 1

print(res)