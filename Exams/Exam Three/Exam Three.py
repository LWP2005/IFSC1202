import math
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)
    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    def angles(self):
        angle1 = math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)) * (180 / math.pi)
        angle2 = math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)) * (180 / math.pi)
        angle3 = math.acos((self.s1**2 + self.s2**2 - self.s3**2) / (2 * self.s1 * self.s2)) * (180 / math.pi)
        return [angle1, angle2, angle3]
triangle_list = []
with open("Exams/Exam Three/Exam Three Triangles.txt", "r") as file:
    for line in file:
        sides = line.strip().split(',')
        triangle = Triangle(sides[0], sides[1], sides[2])
        triangle_list.append(triangle)
for i, triangle in enumerate(triangle_list, 1):
    print(f"Triangle {i}:")
    print(f"Type: {triangle.type()}")
    print(f"Side 1: {triangle.s1}")
    print(f"Side 2: {triangle.s2}")
    print(f"Side 3: {triangle.s3}")
    print(f"Perimeter: {triangle.perimeter()}")
    print(f"Area: {triangle.area()}")
    angles = triangle.angles()
    print(f"Angle 1 (opposite of Side 1): {angles[0]:.2f}°")
    print(f"Angle 2 (opposite of Side 2): {angles[1]:.2f}°")
    print(f"Angle 3 (opposite of Side 3): {angles[2]:.2f}°")
    print('-' * 40)