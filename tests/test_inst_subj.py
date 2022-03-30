from institute import Institute
from main import Subject, Specialization
import unittest

class TestSubjAdd(unittest.TestCase):
    
    def test_inst_subj(self):
        sp = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', 1, 172, sp)
        inst = Institute()
        inst.add_subject(subj)
        self.assertEqual(len(inst.subjects), 1)