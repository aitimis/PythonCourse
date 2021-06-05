# try:
#     1/0
#     raise AttributeError
#     raise Exception
# except ZeroDivisionError:
#     print("")


# take two values from input and divide them

def divide_values():
    my_div = None
    try:
        a = int(input("First nr.: "))
        b = int(input("Second nr.: "))
    except ValueError:
        print("Pls enter numbers not letters")
        return None
    try:
        my_div = a / b

    except ZeroDivisionError:
        print("Don t divide by zero")
    return my_div


print(divide_values())



