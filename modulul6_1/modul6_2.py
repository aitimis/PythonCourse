# # open
#
# file = open('my_file.txt', 'w')
# file.write('My new text')
# file.close()
#
# # file.__enter__()
# # file.__exit__()
# with open('my_file.txt', 'w') as file:
#     file.write('Random text')
#
#
#
# print(type(file))
#
#
#

class A():
    __test = 'test'

a = A()

print(a.__test)