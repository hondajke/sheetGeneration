import unittest
from institute import Institute
from main import Student

class TestStudentAdd(unittest.TestCase):
    
    def test_inst_student(self):
        st = Student(172544, 'Филиппов Петр')
        inst = Institute()
        inst.add_student(st)
        self.assertEqual(len(inst.students), 1)