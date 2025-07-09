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
              \nЗавершенные курсы: {", ".join(self.finished_courses)}"
    
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
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {Student.average_score(self.grades)}"
    
    
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
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
student.rate_lecture(lecturer, 'Python', 7)   # None
student.rate_lecture(lecturer, 'Java', 8)     # Ошибка
student.rate_lecture(lecturer, 'С++', 8)      # Ошибка
student.rate_lecture(reviewer, 'Python', 6)   # Ошибка
reviewer.rate_hw(student,'Python', 3) # Оценка студента по курсу Python

 
print(reviewer)
print(lecturer)
print(student>student)