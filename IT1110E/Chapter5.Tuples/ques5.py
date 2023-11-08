first_list = eval(input())
second_list = eval(input())

check = []
unq_val = []
for el in first_list:
    check.append(sorted(list(el)))
    if sorted(list(el)) not in unq_val:
        unq_val.append(sorted(list(el)))

for el in second_list:
    check.append(sorted(list(el)))
    if sorted(list(el)) not in unq_val:
        unq_val.append(sorted(list(el)))

count = 0
for el in unq_val:
    if check.count(el) > 1:
        count += 1

print(count)

