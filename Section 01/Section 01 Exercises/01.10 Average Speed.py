kilo = float(input("Enter Length of Race in Kilometers: "))
miles = kilo / 1.61

minutes = float(input("Minutes to Run Race: "))
seconds = float(input("Seconds to Run Race: "))
mts = minutes * 60
totalseconds = mts + seconds

hours = totalseconds / 3600
speed = miles / hours
print("Average Speed:", speed)