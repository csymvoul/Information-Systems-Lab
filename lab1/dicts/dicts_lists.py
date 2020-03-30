my_dict = {"grades": [5, 6, 4, 7, 10]}
count = 0
i = 0
for key in my_dict:
    for grade in my_dict[key]:
        count += grade
        i += 1
print("The average is equal to: ", count/i)


