import unittest
from institute import Institute
from main import Specialization

class TestSpecAdd(unittest.TestCase):
    
    def test_inst_spec(self):
        sp = Specialization("ФИИТ")
        inst = Institute()
        inst.add_specialization(sp)
        self.assertEqual(len(inst.specs), 1)
        