# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n: int):
    factorial = 1
    for number in range(1, n+1):
        factorial *= number ** 2
    return factorial

print("my result:")
print(factorial_of_squares(3))
print("result should be:")
print((1**2)*(2**2)*(3**2))