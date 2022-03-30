import unittest
from institute import Institute
from main import ExamPoints, Student
from datetime import date

class TestExamPointsAdd(unittest.TestCase):
    
    def test_inst_exam_points(self):
        st = Student(172544, 'Филиппов Петр')
        examPo = ExamPoints(st, 55.5, 30.0)
        inst = Institute()
        inst.add_examPoints(examPo)
        self.assertEqual(len(inst.examPointsList), 1)