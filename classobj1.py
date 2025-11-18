class Student:
    def __init__(self, name, age, math, english, literature):
        self.name = name
        self.age = age
        self.math = math
        self.english = english
        self.literature = literature
    def introduce(self):
        print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")
        print(f"Điểm: Toán = {self.math}, Anh = {self.english}, Văn = {self.literature}")
    def caculate_person_average_score(self):
        return (self.math + self.english + self.literature) / 3
    @staticmethod
    def calculate_class_average_score(student_list):
        if len(student_list) == 0:
            return 0
        total = 0
        for s in student_list:
            total += s.caculate_person_average_score()
        return total / len(student_list)
students = []
n = int(input("Nhập số lượng học sinh: "))
for i in range(n):
    print(f"\nNhập thông tin học sinh thứ {i + 1}:")
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    math = float(input("Điểm Toán: "))
    english = float(input("Điểm Tiếng Anh: "))
    literature = float(input("Điểm Văn: "))
    student = Student(name, age, math, english, literature)
    students.append(student)
for s in students:
    s.introduce()
    print("Điểm trung bình:", s.caculate_person_average_score())

print("\n=== Điểm trung bình của cả lớp ===")
print(Student.calculate_class_average_score(students))
