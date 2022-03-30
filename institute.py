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
        self.examPointsList = []
           
    def add_specialization(self, special: Specialization):
        if special == None:
            raise Exception("Specialization is null")
        self.specs.append(special)
        
    def add_subject(self, subj: Subject):
        if subj == None:
            raise Exception("Subject is null")
        self.subjects.append(subj)
        
    def add_student(self, stud: Student):
        if stud == None:
            raise Exception("Student is null")
        self.students.append(stud)
        
    def add_group(self, group: Group):
        if group == None:
            raise Exception("Group is null")
        self.groups.append(group)
        
    def add_exam(self, exam: Exam):
        if exam == None:
            raise Exception("Exam is null")
        self.exams.append(exam)
        
    def add_examPoints(self, examPoint: ExamPoints):
        if examPoint == None:
            raise Exception("Exam points is null")
        self.examPointsList.append(examPoint)
