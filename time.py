time1 = int(input("First time: "))
suffix1 = input("suffix: ")
time2 = int(input("Second time: "))
suffix2 = input("suffix: ")

if time1 == time2:
    if suffix1 == suffix2:
        print("Same")
    else:
        if suffix2 < suffix1:
            print("Before")
        else:
            print("After")
else:
    if suffix1 < suffix2:
        print("Before")
    else:
        print("After")