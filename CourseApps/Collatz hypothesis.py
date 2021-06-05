# Exercise Module 3

c0 = int(input("Enter any non-negative and non-zero number: "))
steps = 0

while True:
    if c0 == 1:
        break
    if c0 % 2 == 0:
        c0 /= 2
        steps += 1
        print(c0)
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        print(c0)
        steps += 1

print("Steps:", steps)



