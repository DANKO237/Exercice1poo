class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def afficher_info(self):
        return f"name: {self.name},- age: {self.age}"


student_1 = Student("Alice", 20)
student_2 = Student("Marc", 24)
student_3 = Student("Sarah", 19)
print(student_1.name)
print(student_1.age)


print(student_1.afficher_info())
print(student_2.afficher_info())
print(student_3.afficher_info())
# la difference entre la class Student et l'object student_1 c'est
# le fait que sansla class Student l'object student_& n'exciste pas