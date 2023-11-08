text = []
while True:
    try:
        text.extend(input().split(' '))
    except:
        break

word_dict = dict()

for t in text:
    word_dict[t] = word_dict.get(t, 0) + 1

# print(word_dict.items())
check = list(map(list, word_dict.items()))
check = sorted(check, key= lambda x: (-x[1], x[0]))
# print(check)

for el in check:
    print(el[0])

