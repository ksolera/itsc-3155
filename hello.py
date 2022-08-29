print("Hello, World, Weight Calculator!")
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / .45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * .45
    print("Weight in Kgs: " + str(converted))

