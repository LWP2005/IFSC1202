class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  # A list to store grades
    def RunningAverage(self):
        valid_grades = [int(grade) for grade in self.Grades if grade != '']
        if valid_grades:
            return sum(valid_grades) / len(valid_grades)
        return 0.0
    def TotalAverage(self):
        total_grades = [int(grade) if grade != '' else 0 for grade in self.Grades]
        return sum(total_grades) / len(total_grades)
    def LetterGrade(self):
        total_avg = self.TotalAverage()
        if total_avg >= 90:
            return 'A'
        elif total_avg >= 80:
            return 'B'
        elif total_avg >= 70:
            return 'C'
        elif total_avg >= 60:
            return 'D'
        else:
            return 'F'
class StudentList:
    def __init__(self):
        self.StudentList = []
    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.StudentList.append(student)
    def find_student(self, tnumber):
        for index, student in enumerate(self.StudentList):
            if student.TNumber == tnumber:
                return index
        return -1
    def print_student_list(self):
        print(f"{'First Name':<12}{'Last Name':<12}{'ID':<12}{'Running Avg':<14}{'Semester Avg':<14}{'Letter Grade'}")
        print('-' * 70)
        for student in self.StudentList:
            running_avg = student.RunningAverage()
            semester_avg = student.TotalAverage()
            letter_grade = student.LetterGrade()
            print(f"{student.FirstName:<12}{student.LastName:<12}{student.TNumber:<12}{running_avg:<14.2f}{semester_avg:<14.2f}{letter_grade}")
    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    firstname, lastname, tnumber = parts
                    self.add_student(firstname, lastname, tnumber)
    def add_scores_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                tnumber, score = parts
                score = score.strip()
                student_index = self.find_student(tnumber)
                if student_index != -1:
                    student = self.StudentList[student_index]
                    student.Grades.append(score)
def main():
    student_list = StudentList()
    student_list.add_student_from_file('Assignments/11.Project/11.Project Students.txt')
    student_list.add_scores_from_file('Assignments/11.Project/11.Project Scores.txt')
    student_list.print_student_list()
if __name__ == "__main__":
    main()