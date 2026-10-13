class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 < grade < 20:
            self.grades.append(grade)
            return f"note correct" 
        else:
            return f"note invalide"

    def get_average(self, grade):
        if grade in self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return f"grade n'existe pas"

student = Student("samuel")
print(student.add_grade(14))
print(student.add_grade(18))
print(student.add_grade(12))
print(student.add_grade(25))
print(student.add_grade(-5))

print(student.grades)
print(student.get_average(14))



        