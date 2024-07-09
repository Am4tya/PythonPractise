phones = {
    "John" : 982618,
    "Ria" : 468932,
    "Joy" : 468201,
}
# printing the dictionary
# print(phones)

#checking type of dict
print(type(phones))

# check length of dictionary
print(len(phones))

# access items of dictionary
print(phones["John"])
print(phones.get("John"))
print(phones.keys())

# update the value in dict
phones["John"] = 98234
print(phones)

# add elements in dict
phones["Kia"] = 234567
print(phones)

more_phones = {
    "Kia" : 242436
}

# phones.update(more_phones)
# print(phones)

# # remove elements in a dict
# phones.pop("John")
# print(phones)

# phones.popitem() # this will remove the last added item
# print(phones)

# phones.clear() #this will empty the dict
# print(phones)

# printing elements of a dict
# for x,y in phones.items():
#     print(x,y)

# Nested dictionaries
phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5,
    } 
}

print(phones["Area1"]["y"])
print(phones["Area2"]["c"])