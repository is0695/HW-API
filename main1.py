class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.sr_grade()}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}\n'
    def sr_grade(self):
        list_grade = []
        for x in self.grades.values():
            list_grade += x
        return sum(list_grade)/len(list_grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lecturer_grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        list_grade = []
        for x in self.grades.values():
            list_grade += x
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {sum(list_grade) / len(list_grade)}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
         return f'Имя: {self.name}\nФамилия: {self.surname}\n'
#
#
best_student_1 = Student('Вася', 'Пупкин', 'муж.')
best_student_1.courses_in_progress += ['Python']
best_student_2 = Student('Пуп', 'Васькин', 'муж.')
best_student_2.courses_in_progress += ['Python']
best_student_3 = Student('Some', 'Buddy', 'муж.')
best_student_3.courses_in_progress += ['Python']
cool_mentor_1 = Reviewer('Иван', 'Иванов')
cool_mentor_1.courses_attached += ['Python']
cool_mentor_2 = Reviewer('Михаил', 'Зубенко')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_3 = Reviewer('Мария', 'Зубенко')
cool_mentor_3.courses_attached += ['Python']
best_lecturer_1 = Lecturer('Антон', 'Свиридов')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Саша', 'Волков')
best_lecturer_2.courses_attached += ['Python']
best_lecturer_3 = Lecturer('Юля', 'Новикова')
best_lecturer_3.courses_attached += ['Python']
cool_mentor_1.rate_hw(best_student_1, 'Python', 8)
cool_mentor_1.rate_hw(best_student_1, 'Python', 9)
cool_mentor_2.rate_hw(best_student_2, 'Python', 10)
cool_mentor_1.rate_hw(best_student_2, 'Python', 7)
cool_mentor_2.rate_hw(best_student_2, 'Python', 10)
cool_mentor_1.rate_hw(best_student_3, 'Python', 9)
cool_mentor_2.rate_hw(best_student_3, 'Python', 8)
best_student_1.rate_st(best_lecturer_1, 'Python', 8)
best_student_2.rate_st(best_lecturer_1, 'Python', 10)
best_student_2.finished_courses += ['Python']
best_student_1.finished_courses += ['Python']
best_student_3.finished_courses += ['Python']
students = [best_student_3, best_student_2, best_student_1]
lectureres = [best_lecturer_3, best_lecturer_2, best_lecturer_1]


print(cool_mentor_1)
print(cool_mentor_2)
print(best_lecturer_1)
print(best_student_2)
print(best_student_1)
print(best_student_3)

def student_rating(students, course_name):
    sum_all = 0
    count_all = 0
    for stud in students:
        if stud.courses_in_progress == [course_name]:
            x = stud.grades.values()
            for y in x:
                for i in y:
                    sum_all += i
                count_all += len(y)
    average_for_all = sum_all / count_all
    return average_for_all




def lecturer_rating(lectureres, course_name):
    sum_all = 0
    count_all = 0
    for lect in lectureres:
        if lect.courses_attached == [course_name]:
            x = lect.grades.values()
            for y in x:
                for i in y:
                    sum_all += i
                count_all += len(y)
    average_for_all = sum_all / count_all
    return average_for_all



print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(students, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lectureres, 'Python')}")

