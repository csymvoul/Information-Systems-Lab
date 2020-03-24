mylist = [1, 2, 3, 4, 5]

for i, item in enumerate(mylist):
    if item == 1:
        mylist[i] = 100

for i, item in enumerate(mylist):
    print(i, " ", item)