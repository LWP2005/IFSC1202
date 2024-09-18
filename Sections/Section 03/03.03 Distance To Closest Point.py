numA = int(input("Enter Point A: "))
numB = int(input("Enter Point B: "))
numC = int(input("Enter Point C: "))
difAB = numB - numA
difAC = numC - numA
if difAB < difAC:
    print(difAB)
else:
    print(difAC)