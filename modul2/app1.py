"""
Get from input 23:30:31
Get from input 23:31:31
find the difference between the 2 inputs in seconds
"""
x=input("Get time1: ")
hours=int(x[0:2])
minutes=int(x[3:5])
seconds=int(x[6:8])
print(type(hours))
print(hours)
print(type(minutes))
print(seconds)
print(type(seconds))

y=input("Get time2: ")
hours2=int(y[0:2])
minutes2=int(y[3:5])
seconds2=int(y[6:8])
print(type(hours))
print(hours)
print(type(minutes))
print(seconds)
print(type(seconds))

t1=3600*hours+60*minutes+seconds
t2=3600*hours2+60*minutes2+seconds2
print(t2-t1)









