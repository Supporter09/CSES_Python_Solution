dna = input()

curr_char = ""
length = 0
max_length = -1

for i in range(len(dna)):
    if curr_char == "" and length == 0:
        curr_char = dna[i]
        length = 1
    else:
        if dna[i] == curr_char:
            length += 1
        elif dna[i] != curr_char:
            if length > max_length:
                max_length = length
            length = 1
            curr_char = dna[i]
if length > max_length:
    max_length = length

print(max_length)