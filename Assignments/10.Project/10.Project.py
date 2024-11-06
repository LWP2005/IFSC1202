class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        # Initialize attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        # Convert the scores into a list of floats, treating empty strings as 0.0
        self.Grades = [float(score) if score else 0.0 for score in scores]

    def RunningAverage(self):
        # Calculate the running average based on non-zero scores
        non_zero_scores = [score for score in self.Grades if score > 0]
        return sum(non_zero_scores) / len(non_zero_scores) if non_zero_scores else 0.0

    def TotalAverage(self):
        # Calculate the total average, treating missing grades as 0.0
        return sum(self.Grades) / len(self.Grades) if self.Grades else 0.0

    def LetterGrade(self):
        # Calculate the letter grade based on the total average
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


def process_students(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into parts
                data = line.strip().split(',')
                
                # Check if there are at least 4 parts (first name, last name, TNumber, and scores)
                if len(data) < 4:
                    continue  # Skip invalid lines
                
                # Extract name, TNumber, and the scores
                firstname, lastname, tnumber = data[:3]
                scores = data[3:]  # The rest are the scores
                
                # Create a Student object
                student = Student(firstname, lastname, tnumber, scores)
                
                # Output the student's information
                print(f"Student: {student.FirstName} {student.LastName} (TNumber: {student.TNumber})")
                print(f"Running Average: {student.RunningAverage():.2f}")
                print(f"Total Average: {student.TotalAverage():.2f}")
                print(f"Letter Grade: {student.LetterGrade()}")
                print("-" * 40)
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Example usage: process students from a file 'StudentScores.txt'
process_students('Assignments/10.Project/10.Project Student Scores.txt')