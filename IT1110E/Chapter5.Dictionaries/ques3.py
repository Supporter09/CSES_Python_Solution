text = []
while True:
    try:
        tmp = input().split(' ')
        tmp = [x for x in tmp if x != '']
        text.extend(tmp)
    except:
        break

# print(text)
text_dict = dict()
for el in text:
    print(text_dict.get(el, 0), end=" ")
    text_dict[el] = text_dict.get(el, 0) + 1

