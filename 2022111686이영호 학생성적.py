class Student:
    def __init__(self, name, student_id,):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

class GradeBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, student_id):
        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)

    def add_student_score(self, student_id, score):
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                return
        print(f"학번 {student_id} 학생이 없습니다.")

    def get_top_students(self, n):
        sorted_students = sorted(self.students, key=lambda s: s.calculate_average(), reverse=True)
        return [(student.name, student.calculate_average()) for student in sorted_students[:n]]

grade_book = GradeBook()

grade_book.add_student("김철수", 101)
grade_book.add_student("이영희", 102)
grade_book.add_student("박민수", 103)
grade_book.add_student_score(101, 88)
grade_book.add_student_score(101, 92)
grade_book.add_student_score(102, 75)
grade_book.add_student_score(102, 80)
grade_book.add_student_score(103, 95)
grade_book.add_student_score(103, 90)

top_students = grade_book.get_top_students(2)
print("상위 2명 학생의 성적:", top_students)
