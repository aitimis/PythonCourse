# functions


# general construction

def my_func1(arg1, arg2, arg3, kwarg1=' ', kwarg2='\m'):
    print(arg1, arg2, arg3, sep=kwarg1, end=kwarg2)
    return arg1 + arg2 + arg3


my_var1 = my_func1('str1', 'str2', 'str3', kwarg1='#', kwarg2='$')
print('\n' + 80*'#')
print(my_var1)
print("________________________________________________________________")


# create function for determining prime number
def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True
print(is_prime(3))


# list
empty_list = []
my_list1 = [1, 2, 3]
print(my_list1)
my_list1.append(4)
print(my_list1)

empty_list.append(10)
print(empty_list)



def primes(limit):
    result=[]
    for i in range(1,limit):
        if(is_prime(i)==True):
            result.append(i)
    return result

print('Primes: ', primes(10))


# bit operation

# 01010001
# 01110011

# 01110011 - OR
# 01010001 - AND
# 00100010 - XOR
#################

# 00100010
# 01110011

# 01010001



# numbers in memory
0 # 00000000000...000
1 # 00000000000...001
2 # 00000000000...010

# And
print(10 & 11)
print((10).__and__(11))

10 # 00000000000...1010
11 # 00000000000...1011
   # 00000000000...1010

# OR
print(10 | 11)
print((10).__or__(11))

10 # 00000000000...1010
11 # 00000000000...1011
   # 00000000000...1011

# XOR
print(10 ^ 11)
print((10).__xor__(11))

10 # 00000000000...1010
11 # 00000000000...1011
   # 00000000000...0001


# XOR negative number
print(-1 ^ 3)
print((-1).__xor__(3))

10 # 11111111111...1111  -1
11 # 00000000000...1011
   # 00000000000...0001



def enc_dec(text, key):
    result = ''
    for letter in text:
        number = ord(letter)
        result += (chr(number ^ key))
    return result

output = (enc_dec('Hellow World', 20500))
print(output)

output_dec = enc_dec(output, 20500)
print(output_dec)
