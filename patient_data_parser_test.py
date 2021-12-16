import unittest
from patient_data_parser import (parse_my_data)

class PatientDataTest(unittest.TestCase):
    def test(self):
        self.assertEqual(len(parse_my_data("./sample-data/patient.json")), 2)

if __name__ == '__main__':
    unittest.main()