# 40P
# Calculate the diagonal of a rectangle with sides lenght recievd from input

print("I'm going to calculate the diagonal of a rectangle, just give me two lenghts")

l1 = int(input("Please enter the value for the first lenght\nType here: "))
l2 = int(input("Please enter the value of the second lenght\nType here: "))
# the formula for the diagonal is -> d² = l1² + l2²
d = ((l1**2) + (l2 ** 2)) ** 0.5
print(d)