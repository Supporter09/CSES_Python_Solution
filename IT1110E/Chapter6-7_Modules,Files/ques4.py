def count_words(filepath):
    count = 0
    with open(filepath, 'r') as inp:
        data = inp.read() # read file
        
        lines = data.split() #Split lines of docs

        count += len(lines)

        print(count)

count_words('C:/Users/Admin/Desktop/Code/CSES_Python_Solution/IT1110E/Chapter6-7_Modules,Files/data1.inp')