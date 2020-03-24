mylist = [1, 2, 3, 4, 5]

mylist.extend("end")
mylist.append(["end"])
for item in mylist:
    print(item)

print(type(mylist[0]))
print(type(mylist[-1]))