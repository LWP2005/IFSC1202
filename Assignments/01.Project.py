#nod = number of days
nod = int(input("Number of Days: "))
years = (nod / 365)
print(int(years))

weeks = ((nod % 365) / 7)
print(int(weeks))

days = (