# creating a set
names = {"sia", "mia", "tia"}

# #print set
# print(names)

# #check length of set
# print(len(names))

# #check data type of set
# print(type(names))

# #Accessing items of set
# for x in names:
#     print(x)

# # check if an item exists in a set
# if "sia" in names:
#     print("sia is in the set")

# # add element in set
# names.add("ria")
# print(names)

# # add another sequence in a set
# names_list = ["kia", "ria"]
# names.update(names_list)
# print(names)

# # removing element from a set
# names.discard("sia") # this function will not throw error if value is not present in set 
# print(names)

# # joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
# print(s1, s2)

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

# keep only dublicates while joining
# s1.intersection_update(s2)
# print(s1)

# keep all value except dublicates
# s1.symmetric_difference_update(s2)
# print(s1)