class Student:
    grade = None  
    def set_grade(self, grade):
        self.grade = grade

  
    def display(self):
        print("Student grade is", self.grade)


student1 = Student()
student1.set_grade(9)  
student1.display()  
