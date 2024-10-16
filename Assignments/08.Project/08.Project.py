def read_constitution(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_section(lines, index):
    # Find the start of the section
    start = index
    while start > 0 and lines[start] != '':
        start -= 1
    # Adjust start to the next line after the blank line
    if lines[start] == '':
        start += 1
    
    # Find the end of the section
    end = index
    while end < len(lines) and lines[end] != '':
        end += 1
    
    return start, end

def main():
    lines = read_constitution('Assignments/08.Project/constitution.txt')

    while True:
        search_term = input("Enter a search term (or press Enter to exit): ").strip()
        if not search_term:
            print("Exiting program.")
            break
        
        found = False
        for i, line in enumerate(lines):
            if search_term.lower() in line.lower():
                if not found:
                    start, end = find_section(lines, i)
                    print(f"\nFound in Section (Lines {start + 1} to {end}):")
                    found = True
                
                print(f"{i + 1}: {line}")

        if found:
            print("\nSection Text:")
            for j in range(start, end):
                print(lines[j])
            print("\n" + "=" * 80 + "\n")
        else:
            print("No results found for that search term.\n")

if __name__ == "__main__":
    main()