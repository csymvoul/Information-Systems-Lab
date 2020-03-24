mylist = []
print(type(mylist))

mylist.append(1)
for i in range(5):
    mylist.append(i)

for item in mylist:
    print(item)