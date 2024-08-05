# Lab#7: White-box testing using Branch and Condition Coverage
# นายชลพัฒน์ ปิ่นมุนี รหัส 653380126-0 sec1

import unittest
import sys
sys.path.append('./Lab 7.6 – Branch and Condition Coverage/source')
from CountClump import CountClump

class TestBranchAndConditionCoverage(unittest.TestCase):
    def setUp(self):
        self.count_clump = CountClump()
        self.test_data = {
            "empty_list": [],
            "none_input": None,
            "multiple_clumps": [1, 2, 2, 3, 4, 4],
            "all_same_numbers": [1, 1, 1]
        }
        testname = self.shortDescription()

        if testname == "Test empty list":
            self.data = self.test_data["empty_list"]
        elif testname == "Test None input":
            self.data = self.test_data["none_input"]
        elif testname == "Test multiple clumps":
            self.data = self.test_data["multiple_clumps"]
        elif testname == "Test all same numbers":
            self.data = self.test_data["all_same_numbers"]

    def tearDown(self):
        print('\nEnd of test', self.shortDescription())

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(self.count_clump.count_clumps(self.data), 0)

    def test_none_input(self):
        """Test None input"""
        self.assertEqual(self.count_clump.count_clumps(self.data), 0)

    def test_multiple_clumps(self):
        """Test multiple clumps"""
        self.assertEqual(self.count_clump.count_clumps(self.data), 2)

    def test_all_same_numbers(self):
        """Test all same numbers"""
        self.assertEqual(self.count_clump.count_clumps(self.data), 1)

    @staticmethod
    def make_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestBranchAndConditionCoverage("test_empty_list"))
        suite.addTest(TestBranchAndConditionCoverage("test_none_input"))
        suite.addTest(TestBranchAndConditionCoverage("test_multiple_clumps"))
        suite.addTest(TestBranchAndConditionCoverage("test_all_same_numbers"))
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = TestBranchAndConditionCoverage.make_suite()
    runner.run(test_suite)