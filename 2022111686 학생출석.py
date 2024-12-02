class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True

class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, student_id):

        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)
        else:
            print(f"이미 학번 {student_id}을 가진 학생이 있습니다.")

    def mark_student_attendance(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()
                return
        print(f"학번 {student_id} 학생을 찾을 수 없습니다.")

    def get_attendance_summary(self):
        attendance_count = sum(student.attendance for student in self.students)
        absence_count = len(self.students) - attendance_count
        return {"출석": attendance_count, "결석": absence_count}

    def get_student_list(self):
        return (student.name for student in self.students if student.attendance)

attendance_book = AttendanceBook()

attendance_book.add_student("김철수", 101)
attendance_book.add_student("이영희", 102)
attendance_book.add_student("박민수", 103)
attendance_book.add_student("김철수", 101)


attendance_book.mark_student_attendance(101)
attendance_book.mark_student_attendance(103)

print("출석 요약:", attendance_book.get_attendance_summary())
print("출석한 학생 목록:", attendance_book.get_student_list())
