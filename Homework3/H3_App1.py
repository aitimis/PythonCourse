# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with all int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

input_list = [1, True, '123', False, 6, ()]

def ordered_ints(list_of_objects: list):
    ints_list = []
    for object in list_of_objects:
        if type(object) == tuple: #count the lenght if it can't be directly converted to int
            object_lenght = len(object)
            ints_list.append(object_lenght)
            continue
        if type(object) == str or True or False: # convert to int if possible
            object = int(object)
            ints_list.append(object)
    ints_list.sort()
    ints_list.reverse()
    return ints_list

result = ordered_ints(input_list)
print(result)