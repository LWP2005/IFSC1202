import csv
properties = []
with open('Exams/Exam Two/Exam Two Properties.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        address = row[0]
        city = row[1]
        state = row[2]
        zip_code = row[3]
        price = float(row[4])
        properties.append([address, city, state, zip_code, price])
zipcodes = []
for property in properties:
    zip_code = property[3]
    price = property[4] 
    found = False
    for zipcode in zipcodes:
        if zipcode[0] == zip_code:
            zipcode[1] += 1
            zipcode[2] += price
            found = True
            break
    if not found:
        zipcodes.append([zip_code, 1, price])
print("Zipcode\t\tCount\t\tAverage Price")
for zipcode in zipcodes:
    zip_code = zipcode[0]
    count = zipcode[1]
    avg_price = zipcode[2] / count
    print(f"{zip_code}\t\t{count}\t\t${avg_price:.2f}")