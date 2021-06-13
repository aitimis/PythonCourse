# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
# received format dd:hh:mm:ss
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)
# 10:12:30:40
# 10:10:32:45

# print("Hello, give me two different times and I will tell you the difference between them!")
# print("The time must be in the following format: dd:hh:mm:ss")
# print()
time_1 = input("Please enter the first time\nType here: ")
time_2 = input("Perfect, now please enter the second time:\nType here: ")

dd_1 = int(time_1[:2])
hh_1 = int(time_1[3:5])
mm_1 = int(time_1[6:8])
ss_1 = int(time_1[9:])
# 1 day = 86400 seconds / 1 hour = 3600 / 1 min = 60
dd_2 = int(time_2[:2])
hh_2 = int(time_2[3:5])
mm_2 = int(time_2[6:8])
ss_2 = int(time_2[9:])
