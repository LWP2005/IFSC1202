classA = input("Number of Students in Classroom A: ")
classB = input("Number of Students in Classroom B: ")
classC = input("Number of Students in Classroom C: ")

desksA = ((int(classA)) / 2)
desksB = ((int(classB)) / 2)
desksC = ((int(classC)) / 2)

totaldesks = str(desksA + desksB + desksC)
print(totaldesks)