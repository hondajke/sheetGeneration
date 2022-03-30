import unittest
from institute import Institute
from main import Specialization, Group

class TestGroupAdd(unittest.TestCase):
    
    def test_inst_group(self):
        sp = Specialization("ФИИТ")
        grp = Group("М-ФИИТ-21", 2021, sp)
        inst = Institute()
        inst.add_group(grp)
        self.assertEqual(len(inst.groups), 1)