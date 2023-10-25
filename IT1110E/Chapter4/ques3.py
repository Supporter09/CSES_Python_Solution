def substrings_count(string):
    # Idea 1: Brute-force all substrings and check
    # count = 0
    # for i in range(len(string)):
    #     for j in range(i, len(string)):
    #         check = string[i:j+1]
    #         if check[0] == check[-1]:
    #             count += 1

    # return count

    # Idea 2: Linear + Hash table
    count = 0
    string_dict = dict()

    for char in string:
        if string_dict.get(char) != None:
            count += 1
            count += string_dict.get(char)
            string_dict[char] += 1
        else:
            count += 1
            string_dict[char] = 1
    return count

print(substrings_count('toi la sinh vien bach khoa ha noi'))
