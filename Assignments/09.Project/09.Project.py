import csv
def load_distance_table(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        distance_table = [row for row in reader]
    return distance_table
def print_distance_table(distance_table):
    for row in distance_table:
        print(row)
def find_city_index(city, cities):
    try:
        return cities.index(city)
    except ValueError:
        return -1
def main():
    file_name = 'Assignments/09.Project/09.Project Distances.csv'
    # Load the distance table from the CSV file
    distance_table = load_distance_table(file_name)
    # Print the distance table
    print_distance_table(distance_table)
    # Get cities from user input
    from_city = input("Enter the From City: ").strip()
    to_city = input("Enter the To City: ").strip()
    # Extract cities from the table
    city_list = [row[0] for row in distance_table]
    # Find indices for From City and To City
    from_index = find_city_index(from_city, city_list)
    to_index = find_city_index(to_city, distance_table[0])
    # Validate and print distance
    if from_index == -1:
        print("Invalid From City.")
    elif to_index == -1:
        print("Invalid To City.")
    else:
        distance = distance_table[from_index][to_index]
        print(f"Distance from {from_city} to {to_city}: {distance}")
if __name__ == "__main__":
    main()