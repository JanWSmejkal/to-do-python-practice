mylist = ['a', 'b', 'c', 'd']
list = []
for i, j in enumerate(mylist):
    list.append(mylist[i])
    print(f"Listlength:{len(list)}, Iteration:{i+1}")
