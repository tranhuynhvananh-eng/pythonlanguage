class Student:
    def __init__(self, name, age, math, english, vantv):
        self.name = name
        self.age = age
        self.math = math
        self.english = english
        self.vantv = vantv
    def introduce(self):
        print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")
        print(f"Điểm: Toán = {self.math}, Anh = {self.english}, Văn = {self.vantv}")
    def diemtrungbinh(self):
        return (self.math + self.english + self.vantv) / 3
    def diemtbcalop(student_list):
        if len(student_list) == 0:
            return 0
        total = 0
        for s in student_list:
            total += s.diemtrungbinh()
        return total / len(student_list)
students = []
n = int(input("Nhập số lượng học sinh: "))
for i in range(n):
    print(f"\nNhập thông tin học sinh thứ {i + 1}:")
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    math = float(input("Điểm Toán: "))
    english = float(input("Điểm Tiếng Anh: "))
    vantv = float(input("Điểm Văn: "))
    student = Student(name, age, math, english, vantv)
    students.append(student)
for s in students:
    s.introduce()
    print("Điểm trung bình:", s.diemtrungbinh())

print("\n=== Điểm trung bình của cả lớp ===")
print(Student.diemtbcalop(students))
