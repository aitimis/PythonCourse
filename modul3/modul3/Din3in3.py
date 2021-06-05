list = []
gen1 = (i for i in range(0, 99, 3))
for i in gen1:
   # if i % 3 == 0:
    print(i)
    next(gen1)
    next(gen1)


