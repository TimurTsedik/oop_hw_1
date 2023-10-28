class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
    def avg_grade(self):
        all_grades = list(self.grades.values())
        summ_grades = 0
        for grades_ in all_grades:
            for grade_ in grades_:
                summ_grades += grade_
        return  round(summ_grades / len(grades_), 1)
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: "
                f"{self.avg_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")
    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}
    def avg_rate(self):
        all_rates = list(self.rates.values())
        summ_rates = 0
        for rates_ in all_rates:
            for rate_ in rates_:
                summ_rates += rate_
        return round(summ_rates / len(rates_), 1)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}"
    def __gt__(self, other):
        return self.avg_rate() > other.avg_rate()


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_course_grade(students, CourseTitle):
    gradeSumm = 0
    for student_ in students:
        if CourseTitle in student_.courses_in_progress:
            gradeSumm += student_.avg_grade()
    return gradeSumm / len(students)

def average_course_lector_rate(lecteurs, CourseTitle):
    rateSumm = 0
    for lecteur_ in lecteurs:
        if CourseTitle in lecteur_.courses_attached:
            rateSumm += lecteur_.avg_rate()
    return rateSumm / len(lecteurs)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Advanced Python']

good_student = Student('Demis', 'Karibidis', 'male')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Advanced Python']


cool_reviewer = Reviewer('Some', 'Body')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Merry', 'Christmas')
cool_lecturer.courses_attached += ['Advanced Python']
good_lecturer = Lecturer('Santa', 'Baby')
good_lecturer.courses_attached += ['Advanced Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 7)
cool_reviewer.rate_hw(good_student, 'Python', 6)

best_student.rate_lecture(cool_lecturer, 'Advanced Python', 9)
best_student.rate_lecture(cool_lecturer, 'Advanced Python', 10)
best_student.rate_lecture(cool_lecturer, 'Advanced Python', 10)
good_student.rate_lecture(good_lecturer, 'Advanced Python', 8)
good_student.rate_lecture(good_lecturer, 'Advanced Python', 10)
good_student.rate_lecture(good_lecturer, 'Advanced Python', 7)




print(cool_reviewer)
print(cool_lecturer)
print(best_student.avg_grade())
print(best_student)
print(good_student)

print(good_student > best_student)

print(average_course_grade([best_student, good_student], 'Python'))
print(average_course_lector_rate([cool_lecturer, good_lecturer], 'Advanced Python'))
