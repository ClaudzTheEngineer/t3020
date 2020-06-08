import unittest
from io import StringIO 
from unittest import TestCase 
from unittest.mock import patch 
from code.datamunger import calc_total
from code.datamunger import check_row
from code.datamunger import check_monotonic

class DataMungerTest(unittest.TestCase):
    

    def test_calcTotal(self):
        data = [0,1,2,3,4,5,6,7,8,9]
        total2 = calc_total(data)

        self.assertEqual(36,total2)

    def test_check_monotonic_correct(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        curr = [44,2,3,4,5,6,7,8,9,10]
        expectedOutput = ""

        with patch('sys.stdout', new = StringIO()) as fake_out: 
                check_monotonic(0,prev,curr)
                self.assertEqual(fake_out.getvalue(), expectedOutput)

    def test_check_monotonic_correctT8declining(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        curr = [44,2,3,4,5,6,7,8,7,10]
        expectedOutput = ""

        with patch('sys.stdout', new = StringIO()) as fake_out: 
                check_monotonic(0,prev,curr)
                self.assertEqual(fake_out.getvalue(), expectedOutput)

    def test_check_monotonic_correctTALLdeclining(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        curr = [23,2,3,4,5,6,7,8,9,10]
        expectedOutput = ""

        with patch('sys.stdout', new = StringIO()) as fake_out: 
                check_monotonic(0,prev,curr)
                self.assertEqual(fake_out.getvalue(), expectedOutput)

    def test_check_monotonic_incorrect(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        curr = [44,2,1,4,5,6,7,8,9,10]
        expectedOutput = "Monotonic error at column 2 comparing lines -1 and 0   values 1 and 2\n"

        with patch('sys.stdout', new = StringIO()) as fake_out: 
                check_monotonic(0,prev,curr)
                self.assertEqual(fake_out.getvalue(), expectedOutput)

    

    def test_check_row_allPopulated(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        data = ["44","2","3","4","5","6","7","8","9","10"]

        ok = check_row(0,prev,data)

        self.assertTrue(ok)

    def test_check_row_noOther(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        data = ["44","2","3","4","5","6","7","8","9",""]

        ok = check_row(0,prev,data)

        self.assertTrue(ok)

    def test_check_row_missingT(self):
        prev = [36,1,2,3,4,5,6,7,8,9]
        data = ["44","2","","4","5","6","7","8","9","10"]

        ok = check_row(0,prev,data)

        self.assertFalse(ok)


if __name__ == '__main__':
    unittest.main()