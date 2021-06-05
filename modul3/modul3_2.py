# while

def add_numbers():
    sum = 0
    num_list =[]
    while sum < 100 :
        nr = int(input("Ad numbers = "))
        if nr  >= 0 :
           sum= sum + nr
           num_list.append(nr)
    if sum == 100 :
        return num_list
    else :
        return sum
print(add_numbers())
