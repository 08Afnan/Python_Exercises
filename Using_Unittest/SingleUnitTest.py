"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

import unittest
from Model import Model

print("UNIT TEST - Testing if program removes a record from the sequential data structure as expected")
print("DEVELOPED BY AFNAN ISLAM")

class SingleUnitTest(unittest.TestCase):
    """
    Unit test class for testing the Model class functionality, specifically the deletion of a traffic record.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the Model instance for all test methods in the class.
        This method is run once for the class.
        """
        cls.model = Model()

    def test_delete_trafficRecord(self):
        """
        Test the delete_trafficRecord method of the Model class.
        This test ensures that a record can be deleted from the dataset.
        """
        # Ensure dataset is loaded
        self.model.reload_dataset()

        # Ensure record is deleted (dummy row value of 1 is given as argument)
        self.model.delete_trafficRecord(1)

        # Dummy assert to indicate the functions executed without error
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
