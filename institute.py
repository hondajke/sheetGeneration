from main import *
from dataclasses import dataclass

@dataclass
class Institute:
      
    def __init__(self):
        self.specs = []
        self.subjects = []
        self.students = []
        self.groups = []
        self.exams = []
        self.exam_points = []
           
    def add_spec(self, special: Specialization):
        if special == None:
            raise Exception("Specialization is null")
        if type(special) != Specialization:
            raise Exception("Wrong type")
        if special.name == '':
            raise Exception("Specialization name is null")
        for i in self.specs:
            if i == special:
                raise Exception("Specialization already exist")
        self.specs.append(special)
        
    def add_subject(self, subj: Subject):
        if subj == None:
            raise Exception("Subject is null")
        if type(subj) != Subject:
            raise Exception("Wrong type")
        for i in self.subjects:
            if i == subj:
                raise Exception("Subject already exist")
        if subj.name == '':
            raise Exception("Subject name is null")
        if subj.code == '':
            raise Exception("Subject code is null")
        if subj.semester < 1:
            raise Exception("Subject semester can not be negative")
        if subj.hours < 1:
            raise Exception("Subject hour can not be negative")
        self.subjects.append(subj)
        
    def add_student(self, stud: Student):
        if stud == None:
            raise Exception("Student is null")
        if type(stud) != Student:
            raise Exception("Wrong type")
        for i in self.students:
            if i == stud:
                raise Exception("Student already exist")
            if i.code == stud.code:
                raise Exception("Student code already exist")
        if stud.code > 999999 or stud.code < 100000:
            raise Exception("Wrong student code")
        if stud.fio == '':
            raise Exception("Student fio is null")
        self.students.append(stud)
        
    def add_group(self, group: Group):
        if group == None:
            raise Exception("Group is null")
        if type(group) != Group:
            raise Exception("Wrong type")
        for i in self.groups:
            if i == group:
                raise Exception("Group already exist")
        if group.name == "":
            raise Exception("Group name is null")
        if group.year < 1:
            raise Exception("Group year is negative")
        self.groups.append(group)
        
    def add_exam(self, exam: Exam):
        if exam == None:
            raise Exception("Exam is null")
        if type(exam) != Exam:
            raise Exception("Wrong type")
        if type(exam.lecturer_fio) != str:
            raise Exception("Wrong lecturer type")
        if type(exam.year) != str:
            raise Exception("Wrong year type")
        for i in self.exams:
            if i == exam:
                raise Exception("Exam already exist")
        if exam.lecturer_fio == '':
            raise Exception("Lecturer fio is null")
        if exam.year == '':
            raise Exception("Year is null")
        self.exams.append(exam)
        
    def add_examPoints(self, examPoint: ExamPoints):
        if examPoint == None:
            raise Exception("Exam points is null")
        if type(examPoint) != ExamPoints:
            raise Exception("Wrong type")
        if type(examPoint.student) != Student:
            raise Exception("Wrong student type")
        if type(examPoint.inPoints) != float:
            raise Exception("Wrong in points type")
        if type(examPoint.examPoints) != float:
            raise Exception("Wrong exam points type")
        for i in self.exam_points:
            if i == examPoint:
                raise Exception("Exam point already exist")
        if examPoint.inPoints < 0 or examPoint.inPoints > 70.0:
            raise Exception("Wrong in points")
        if examPoint.examPoints < 0 or examPoint.examPoints > 30.0:
            raise Exception("Wrong exam points")

        self.exam_points.append(examPoint)
        
    def get_spec(self, name: str):
        if type(name) != str:
            raise Exception("Wrong type")
        if name == '':
            raise Exception("Name is null")
        for i in self.specs:
            if i.name == name:
                return i
    
    def get_subject(self):
        return self.subjects
    
    def get_student(self, student_code: int):
        if type(student_code) != int:
            raise Exception("Wrong type")
        for i in self.students:
            if i.code == student_code:
                return i
        
    def get_group(self, name: str):
        if type(name) != str:
            raise Exception("Wrong type")
        for i in self.groups:
            if i.name == name:
                return i

    def get_exam(self):
        return self.exams
    
    def get_exam_result(self):
        return self.examPointsList