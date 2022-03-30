import unittest
from institute import Institute
from main import Exam, Specialization, Subject
from datetime import date

class TestExamAdd(unittest.TestCase):
    
    def test_inst_exam(self):
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 1)