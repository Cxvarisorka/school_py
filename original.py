class Student: 
    def __init__(self,name,lastname,age):
        self.name = name.capitalize()
        self.lastname = lastname.capitalize()
        self.age = age
        
    def get_info(self):
        print(f"Student's Name Is {self.name} And Lastname Is {self.lastname}")
        
class School:
    def __init__(self,school_name,school_adress):
        self.school_name = school_name.capitalize()
        self.school_adress = school_adress
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)
    
    def remove_student(self,index):
        removed_student = self.students.pop(index)
        print(f"Removed Student Fullname Is {removed_student.name} {removed_student.lastname}")
    
    def show_students(self):
        if len(self.students) == 0:
            print(f"In {self.school_name} There Is No Any Students")
        for student in self.students:
            student.get_info()
    
    def show_school_info(self):
        print(f"School Name Is {self.school_name}.")
        print(f"School Address Is {self.school_adress}")
        print('-----------------------------------------------------')
