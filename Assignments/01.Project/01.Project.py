#nod = number of days
nod = int(input("Number of Days: "))
years = (nod / 365)
print("Years:", int(years))

weeks = ((nod % 365) / 7)
print("Weeks:", int(weeks))

days = ((nod % 365) % 7)
print("Days:", int(days))