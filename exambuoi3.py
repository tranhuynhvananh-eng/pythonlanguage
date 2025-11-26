class Student:
    def __init__(self,name,gpa):
        self.name = name
        self.__gpa = gpa
    def gpa(self):
        return self.__gpa
    def testgpa(self, diem):
        if 0.0<= diem <=4.0:
            self.__gpa=diem
        else :
            print("GPA values between 0.0 and 4.0")
    def display(self):
        print(f"Studen:{self.name}, GPA: {self.__gpa}")
p= Student("anh",3.9)
p.display()