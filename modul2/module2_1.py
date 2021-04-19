name = 'John'
age = 26

print('name: ', name, ', age: ', age)

#print = 'print'

#print('name: ', name, ', age: ', age)

# type function

#result = type(name)
#print(result)

#result = type(age)
#print(result)

# print(5 * name)
# result1 = 5 * name
# result2 = type(result1)

# print(result2)

# result = id(name)
# print(result)

print(8 + 8)
print((8).__add__(8))

print(80 * ' text')
print(' text' * 8)

print(80 * '#')

# print(8 * ' text')
print((8).__mul__( ' text'))
print((' text').__mul__(8))

print(8 - 8)
print((8).__sub__(8))

print(8 / 8)
print((8).__truediv__(8))

print(8**8)
print((8).__pow__(8))
print(pow(8, 8))


# Float

var = (8).__truediv__(8)
print(type(var))
'\n'
'\n'


a = (3)
b = (4)
c = (5)

x = (-b + (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)

y = (-b - (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
print(x)
print(y)

bsqr = b.__pow__(2)
mul = (4).__mul__(a.__mul__(c))
dif1 = bsqr.__sub__(mul)
print(type(dif1))
var = (1).__truediv__(2)
dif1 = float(dif1)
rad = dif1.__pow__(var)
print(type(var))
print(type(rad))
b = complex(b)
dif2 = (-b).__sub__(rad)


# Complex

nr1 = 1 +1j
nr2 = 3 + 5j
print(nr1+nr2)
print(type(nr1))

# Strings

my_str = 'My String \n no multi line'
print(my_str)

my_str1 = '''this
is
a
multi
string
test
'''
print(my_str)

my_str2 = r"My String \n no multi line"
print(my_str2)

my_str2 = f"""My String {my_str1}"""
print(my_str2)


# dir
info = dir(my_str2)
print(info)


var1 = 'this is {}'
cap = var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

phone = "0747.655.444"
split1 = phone.split("7")
print(split1)

split1 = phone.rsplit(sep = '.', maxsplit = 1)
print(split1)

split1 = phone.split(sep ='.', maxsplit = 1)
print(split1)


# input
# text = input('give me your name: ')
# name = input('give me your name: ')

# print(var1, input('give me your name: '))


# slice
text = "My Text"
first_letter = "My Text"[0]
print(first_letter)
slice1 = text[1:4]
print(slice1)
slice2 = text[0:7:2]
print(slice2)


#
#  text = input('Enter a 10 character word here: ')
slice1 = text[0:5]
slice2 = text[5:11]
#print(slice1)
#print(slice2)
print(slice2 + slice1)

# negative step
text[::-1]


# True, False

my_bool = True
print(type(my_bool))
my_bool = False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

adunare = True + False
print(adunare)

print(dir(True))

adunare = True.__add__(False)
print(adunare)

# None

my_none = None

x = print('')
print(x)

# Truth









