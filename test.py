import unittest

class TestGeneration(unittest.TestCase):
    
    def test_student_class(self):
        self.assertEqual('Филиппов Петр', fio)
        self.assertEqual(172544, code)
        
    def test_group_class(self):
        self.assertEqual('М-ФИИТ-21', name)
        self.assertEqual(2021, year)
        self.assertEqual(spec, specialization)
        
    def test_exam_class(self):
        self.assertEqual(sub, subject)
        self.assertEqual(date, examDate)
        self.assertEqual("2021", year)
        self.assertEqual("Эверстов Владимир Васильевич", lecturer_fio)
        
    def test_exampoints_class(self):
        self.assertEqual(student, student)
        self.assertEqual(55.5, inPoints)
        self.assertEqual(30.0, examPoints)
        
    def test_subject_class(self):
        self.assertEqual('Б1.', code)
        self.assertEqual('Основы программирования', name)
        self.assertEqual(1, semester)
        self.assertEqual(172, hours)
        self.assertEqual(spec, specialization)
        
    def test_specialization_class(self):
        self.assertEqual("ФИИТ", name)