def is_palindrome(string):
    string = ''.join([x for x in string if x != " "])
    if string == string[::-1]:
        return "YES"
    else:
        return "NO"

print(is_palindrome('borrow or rob'))