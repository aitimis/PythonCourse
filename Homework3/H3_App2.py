# 25P - (use recursion)
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    if n <= 1 :
        return 1
    else:
        return sum_of_square(n-1) + n ** 2

print(sum_of_square(10))