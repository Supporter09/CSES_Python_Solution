def process(filepath):
    with open(filepath, 'r') as inp:
        data = inp.readlines() # read file

        custom_dict = dict() # Make a dictionary store customer data

        for line in data: # Process data
            line = line.replace('\n', '')
            data = line.split()
            if custom_dict.get(data[0]) == None:
                custom_dict[data[0]] = {
                    data[1] : int(data[2])
                }
            else:
                custom_dict[data[0]][data[1]] = custom_dict[data[0]].get(data[1], 0) + int(data[2])

        # Print customer and purchased products
        for customer in custom_dict:
            print(customer+':')
            check = custom_dict[customer]
            check = sorted(list(check.items()), key=lambda x: x[0])
            for el in check:
                print(el[0], el[1])


process('C:/Users/Admin/Desktop/Code/CSES_Python_Solution/IT1110E/Chapter6-7_Modules,Files/data2.inp')