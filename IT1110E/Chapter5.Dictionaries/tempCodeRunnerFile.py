president_dict = {}
text = []
while True:
    try:
        arr = input().split(" ")
        text.append(arr)
    except:
        break

for el in text:
    president_dict[str(el[0])] = president_dict.get(el[0], 0) + int(el[1])

key = [str(x) for x in president_dict.keys()]

res = sorted(key, key = lambda s : s.lower())

for element in res:
    print(element, president_dict[element])
