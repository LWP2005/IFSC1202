print("First Timestamp: ")
fhours = int(input("Hours: "))
fminutes = int(input("Minutes: "))
fseconds = int(input("Seconds: "))

print("Second Timestamp: ")
shours = int(input("Hours: "))
sminutes = int(input("Minutes: "))
sseconds = int(input("Seconds: "))

firsttimestamp = ((fhours * 60 * 60) + (fminutes * 60) + fseconds)
secondtimestamp = ((shours * 60 * 60) + (sminutes * 60) + sseconds)
timedifference = (secondtimestamp - firsttimestamp)
print(timedifference)