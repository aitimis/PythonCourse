"""
Get from input abcdefg
Return bcdefgh

"""

x=input("input=")

if (x[0] == "a"):
    z1 = x[0]
elif (x[0] == "b"):
    z1 = chr(ord(x[0]) + 1)
elif (x[0] == "c"):
    z1 = chr(ord(x[0]) + 2)
elif (x[0] == "d"):
    z1 = chr(ord(x[0]) + 3)
elif (x[0] == "e"):
    z1 = chr(ord(x[0]) + 4)
elif (x[0] == "f"):
    z1 = chr(ord(x[0]) + 5)
elif(x[0]=="g"):
    z1 = chr(ord(x[0]) + 6)
if (x[1] == "a"):
    z2 = x[0]
elif (x[1] == "b"):
    z2 = chr(ord(x[1]) + 1)
elif (x[1] == "c"):
    z2 = chr(ord(x[1]) + 2)
elif (x[1] == "d"):
    z2 = chr(ord(x[1]) + 3)
elif (x[1] == "e"):
    z2 = chr(ord(x[1]) + 4)
elif (x[1] == "f"):
    z2 = chr(ord(x[1]) + 5)
elif(x[1]=="g"):
    z2 = chr(ord(x[1]) + 6)
if (x[2] == "a"):
    z3 = x[0]
elif (x[2] == "b"):
    z3 = chr(ord(x[2]) + 1)
elif (x[2] == "c"):
    z3 = chr(ord(x[2]) + 2)
elif (x[2] == "d"):
    z3 = chr(ord(x[2]) + 3)
elif (x[2] == "e"):
    z3 = chr(ord(x[2]) + 4)
elif (x[2] == "f"):
    z3 = chr(ord(x[2]) + 5)
elif(x[2]=="g"):
    z3 = chr(ord(x[2]) + 6)
if (x[3] == "a"):
    z4 = x[0]
elif (x[3] == "b"):
    z4 = chr(ord(x[3]) + 1)
elif (x[3] == "c"):
    z4 = chr(ord(x[3]) + 2)
elif (x[3] == "d"):
    z4= chr(ord(x[3]) + 3)
elif (x[3] == "e"):
    z4 = chr(ord(x[3]) + 4)
elif (x[3] == "f"):
    z4 = chr(ord(x[3]) + 5)
elif(x[3]=="g"):
    z4 = chr(ord(x[3]) + 6)
print(z1,z2,z3,z4,sep="")