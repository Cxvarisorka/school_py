class Student: 
    def __init__(self,name,lastname,score):
        self.name = name.capitalize()
        self.lastname = lastname.capitalize()
        self.score = score
        
    def get_info(self):
        print(f"Student's Name Is {self.name} And Lastname Is {self.lastname}")
        
class School:
    def __init__(self,school_name,school_adress):
        self.school_name = school_name.capitalize()
        self.school_adress = school_adress
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)
        print(f'Succsesfully Added {student.name} In {self.school_name} School.')
        print('------------------------------------------------------\n')
    
    def remove_student(self,index):
        removed_student = self.students.pop(index)
        print(f"Succsesfully Removed {removed_student.name} {removed_student.lastname} From {self.school_name} School")
        print('------------------------------------------------------\n')
        
    def show_students(self):
        if len(self.students) == 0:
            print(f"In {self.school_name} There Is No Any Students")
            print('------------------------------------------------------\n')
            return
        for student in self.students:
            student.get_info()
        print('------------------------------------------------------\n')
    
    def show_school_info(self):
        print(f"School Name Is {self.school_name}.")
        print(f"School Address Is {self.school_adress}")
        print('------------------------------------------------------\n')

class Program:
    def __init__(self):
        self.schools = []
        
    def add_school(self):
        
        school_name = input("Please Enter School Name: ")
        school_address = input("Please Enter School Address: ")
        
        school = School(school_name,school_address)
        
        for elem in self.schools:
            if elem.school_name == school.school_name:
                print('School Already Exsists.')
                return
        
        self.schools.append(school)
        
        print('Succsesfully Added New School.')
        print('------------------------------------------------------\n')
    
    def remove_shcool(self):
        if len(self.schools) == 0:
            print('There is no any schools to remove.')
            print('------------------------------------------------------\n')
            return

        self.show_schools()
        
        user_input = int(input('Which School Do you Want To Delete?: '))
        
        if user_input > len(self.schools):
            print('Please Enter Valid Option.')
        else:
            deleted_school = self.schools.pop(user_input - 1)
            print(f'School {deleted_school.school_name} Succsesfully Deleted.')
            
        print('------------------------------------------------------\n')
            
    def show_schools(self):
        
        if len(self.schools) == 0:
            print('There is no any schools added.')
            print('------------------------------------------------------\n')
            return
        
        number = 1
        
        for school in self.schools:
            print(f"{number}: {school.school_name}")
            number += 1

        print('------------------------------------------------------\n')
    
    def top_students_all(self):
        
        if len(self.schools) == 0:
            print('There is no any schools or students.')
            print('------------------------------------------------------\n')
            return
        
        students_scores = []
        top_students = []
        
        for school in self.schools:
            for student in school.students:
                students_scores.append((student.name + ' ' + student.lastname,student.score))
        
        students_scores.sort(key=lambda x: x[1], reverse=True)
    
        for student in students_scores[:3]:
            top_students.append({"name": student[0], "score": student[1]})
        
        print("Top 3 students in all schools are...")
        
        for student in top_students:
            student_name = student["name"]
            student_score = student["score"]
            
            print(f"Name: { student_name }, Score: { student_score }")
                       
        print('------------------------------------------------------\n')
    
    def top_shcool(self):
        
        if len(self.schools) == 0:
            print('There is no any school Added.')
            print('------------------------------------------------------\n')
            return
        
        all_schools = []
        
        for school in self.schools:
            all_schools.append((school.school_name,school.students))
            
        all_schools.sort(key=lambda school: len(school[1]), reverse=True)
        
        first_school = all_schools[0]
        
        print(f"Top school is {first_school[0]} with {len(first_school[1])} students.")
    
        print('------------------------------------------------------\n')
        
    def add_student_school(self):
        if len(self.schools) == 0:
            print('There is no any school added.')
            print('------------------------------------------------------\n')
            return
        
        self.show_schools()
        
        user_input = int(input('Choose School To Add Student: '))
        
        if user_input > len(self.schools):
            print(f'There is no school number {user_input}')
        else:
            school = self.schools[user_input - 1]
            
            students_count = int(input('How many students do you want to add: '))
            
            count = 0
            
            for count in range(students_count):
                student_name = input('What is student name: ')
                student_lastname = input('What is student lastname: ')
                student_score = int(input("What is student score: "))
                
                print('-------------------------------------')
                
                student_created = Student(student_name,student_lastname,student_score)
                
                student_exsist = False
                
                for elem in self.schools:
                    for stu in elem.students:
                        if stu.name == student_created.name and stu.lastname == student_created.lastname:
                            print(f'Student is already exsist in {elem.school_name} school!')
                            student_exsist = True
                            break
                    break
                
                if student_exsist:
                    print(f"{student_name} {student_lastname} will not added into {school.school_name} school.")
                    continue
                    
                
                school.add_student(student_created)
                
                print(f'{student_created.name} Added Succsesfully in {school.school_name}')

        print('------------------------------------------------------\n')
    
    def remove_student_school(self):
        if len(self.schools) == 0:
            print('There is no any school added.')
            print('------------------------------------------------------\n')
            return
        
        self.show_schools()
        
        user_input = int(input('Choose School To Remove Student: '))
        
        if user_input > len(self.schools):
            print(f'There is no school number {user_input}')
        else:
            school = self.schools[user_input - 1]
            
            number = 1
            
            for student in school.students:
                print(f"{number}. {student.name} {student.lastname}")
                number += 1
            
            choose_student = int(input("Please enter which student do you want to remove: "))
            
            if choose_student > number:
                print('Invalid Option.')
            else:
                school.remove_student(choose_student - 1)
        
        print('------------------------------------------------------\n')
    
    def show_students_school(self):
        if len(self.schools) == 0:
            print('There is no any school added.')
            print('------------------------------------------------------\n')
            return
        
        self.show_schools()
        
        user_input = int(input('Choose School To See Students: '))
        
        if user_input > len(self.schools):
            print(f'There is no school number {user_input}')
        else:
            school = self.schools[user_input - 1]
            
            school.show_students()
            
            
program = Program()
         
def menu():
    
    # Add show student list option
    
    questions = {
        1: 'Show School List',
        2: 'Most Popular School',
        3: 'Top 3 Students Of All School',
        4: 'Add Student To School',
        5: 'Remove Student From School',
        6: 'Add School',
        7: 'Delete School',
        8: 'Show Students In School',
        9: 'Exit'
    }
    
    user_input = 0
    
    while user_input != 9:
        
        # Print all the questions
        for index,question in questions.items():
            print(f"{index}. {question}")
    
        # Get user input
        user_input = int(input('Please Choose: '))
        
        if user_input == 1:
            program.show_schools()
        elif user_input == 2:
            program.top_shcool()
        elif user_input == 3:
            program.top_students_all()
        elif user_input == 4:
            program.add_student_school()
        elif user_input == 5:
            program.remove_student_school()
        elif user_input == 6:
            program.add_school()
        elif user_input == 7:
            program.remove_shcool()
        elif user_input == 8:
            program.show_students_school()
        elif user_input == 9:
            print('Thanks For Using Our Program')
            break
        else:
            print('Invalid Option!')

menu()       
            
            
            
