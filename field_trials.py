class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    
        
    def average_score(dict_):
            sum=0
            grades_=0
            for key in dict_:
                for index in dict_[key]:
                   sum+=index
                   grades_+=1
            if sum==0:
                return 0
            sum=sum/grades_
            return sum
        
    def rate_lecture(self,lecturer,course_4_greate,grade):
        if isinstance(lecturer, Lecturer) and course_4_greate in self.courses_in_progress and course_4_greate in lecturer.courses_attached:
            if grade >= 0 and grade <= 10:
                lecturer.grades.setdefault(course_4_greate,[])
                lecturer.grades[course_4_greate].append(grade)
            else:
                print("Оценки должны быть по 10-балльной шкале")
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Student.average_score(self.grades)} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
              \nЗавершенные курсы: {", ".join(self.finished_courses)}  \n"
    
    def __eq__(self, other):
        if Student.average_score(self.grades)==Student.average_score(other.grades):
            return "равны"
        elif Student.average_score(self.grades)>Student.average_score(other.grades):
            return f'{self.name} {self.surname}имеет больший средний бал: {Student.average_score(self.grades)}'
        else:
            return f'{other.name} {other.surname} имеет больший средний бал: {Student.average_score(other.grades)}'
        
    def __lt__(self, other):
        return Student.average_score(self.grades)>Student.average_score(other.grades)
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)
        self.grades={}

    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {Student.average_score(self.grades)} \n"
    
    
    def __eq__(self, other):
        if Student.average_score(self.grades)==Student.average_score(other.grades):
            return "равны"
        elif Student.average_score(self.grades)>Student.average_score(other.grades):
            return f'{self.name} {self.surname}имеет больший средний бал: {Student.average_score(self.grades)}'
        else:
            return f'{other.name} {other.surname} имеет больший средний бал: {Student.average_score(other.grades)}'
        
    def __lt__(self, other):
        return Student.average_score(self.grades)<Student.average_score(other.grades)
    


class Reviewer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \n"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
list_students=[]
list_lectors=[]
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Федор', 'Федоров')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Степан', 'Степанов')
student_1 = Student('Ольга','Алёхина', 'Ж')
student_2 = Student('Олег', 'Алёхин', 'М')
list_students.append(student_1)
list_students.append(student_2)
list_lectors.append(lecturer_1)
list_lectors.append(lecturer_2)
student_1.courses_in_progress += ['Python', 'Java','C#']
student_2.courses_in_progress += ['Python', 'C++', 'Java']
lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Java', 'C#']
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Python', 'C#']
 
student_1.rate_lecture(lecturer_1, 'Python', 7)   
student_1.rate_lecture(lecturer_2, 'C#', 9)
student_1.rate_lecture(lecturer_2, 'Java', 8)     
student_2.rate_lecture(lecturer_1, 'C++', 8)      
student_2.rate_lecture(lecturer_2, 'Java', 6)  
student_2.rate_lecture(reviewer_1, 'Python', 6)
reviewer_1.rate_hw(student_1,'Python', 3) 
reviewer_2.rate_hw(student_2,'Python', 5)
reviewer_1.rate_hw(student_2,'C++', 4)
reviewer_2.rate_hw(student_1,'C#', 5)


def sum_rate(arr,key):
    sum=0
    len_arr=0
    for object in arr:
        class_dict=object.grades
        if key in class_dict:
         for index in class_dict[key]:
            sum+=index            
            len_arr+=1
        else:
            continue
    if len_arr==0:
        print('Нет оценок')
        return
    print(sum/len_arr) 
    
print(reviewer_1)
print(lecturer_1)
print(student_1)
print(student_1>student_2)    #Сравнение средних оценок студентов
print(student_1==student_2)   #Сравнение(более развернутый ответ)
sum_rate(list_students,'C#')  # Средняя оценка студентов по курсу
sum_rate(list_lectors,'Java') # Средняя оценка лекторов по курсу


