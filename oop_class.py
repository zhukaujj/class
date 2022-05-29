class Student:
    all_student = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_student.append(self)

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_from_student:
                lecturer.grades_from_student[course] += [grade]
            else:
                lecturer.grades_from_student[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades:
            all_grades = [i for j in self.grades.values() for i in j]
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {self.average_grade()}\n'\
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нету"}'
        return res

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        print('Только ревьюреры могут оценивать студентов')


class Lecturer(Mentor):
    all_lecturer = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_student = {}
        Lecturer.all_lecturer.append(self)

    def average_score_from_students(self):
        if self.grades_from_student:
            all_grades = [i for j in self.grades_from_student.values() for i in j]
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score_from_students()}'
        return res

    def __lt__(self, other):
        return self.average_score_from_students() < other.average_score_from_students()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_students_grade(all_students, searched_course):
    all_grades = []
    for student in all_students:
        if searched_course in student.grades:
            all_grades += student.grades[searched_course]
    if not all_grades:
        return 'Такой курс не оценивали'
    return sum(all_grades) / len(all_grades)


def average_lecturers_grade(all_lecturers, searched_course):
    all_grades = []
    for lecturer in all_lecturers:
        if searched_course in lecturer.grades_from_student:
            all_grades += lecturer.grades_from_student[searched_course]
    if not all_grades:
        return 'Такой курс не оценивали'
    return sum(all_grades) / len(all_grades)


first_student = Student('Evgeniy', 'Zhukov', 'gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Java']

best_reviewer = Reviewer('Oleg', 'Ivanov')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']

best_lecturer = Lecturer('Vasya', 'Petrov')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

best_reviewer.rate_hw(first_student, 'Python', 7)
best_reviewer.rate_hw(first_student, 'Python', 8)
best_reviewer.rate_hw(first_student, 'Git', 9)
best_reviewer.rate_hw(first_student, 'Git', 6)


best_lecturer.rate_hw(first_student, 'Python', 10)


dishonest_student = Student('Dishonest', 'student', 'gender')
dishonest_student.courses_in_progress += ['Python']
dishonest_student.courses_in_progress += ['Git']

best_reviewer.rate_hw(dishonest_student, 'Python', 1)
best_reviewer.rate_hw(dishonest_student, 'Python', 3)
best_reviewer.rate_hw(dishonest_student, 'Git', 2)
best_reviewer.rate_hw(dishonest_student, 'Git', 3)


dishonest_lecturer = Lecturer('Andrei', 'Pumpkin')

print('-' * 30)

print(first_student.grades)

first_student.rate(best_lecturer, 'Python', 8)
first_student.rate(best_lecturer, 'Python', 10)
first_student.rate(best_lecturer, 'Git', 9)
first_student.rate(best_lecturer, 'Git', 6)

print('-' * 30)
print(best_lecturer.grades_from_student)

print('-' * 30)
print(best_reviewer)
print('-' * 30)
print(best_lecturer)
print('-' * 30)
print(first_student)
print('-' * 30)

is_lt = (dishonest_student < first_student)
dishonest_lecturer.__lt__(best_lecturer)


print(average_students_grade(Student.all_student, 'Python'))
print(average_lecturers_grade(Lecturer.all_lecturer, 'Python'))










