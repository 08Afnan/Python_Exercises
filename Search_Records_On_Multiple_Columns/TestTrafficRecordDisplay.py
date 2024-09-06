"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout
from Subclasses import TrafficRecordBasic, TrafficRecordDetailed

print("UNIT TEST - Testing concept of inheritance to format records, checking if the overridden output format correct")
print("DEVELOPED BY AFNAN ISLAM")

class TestTrafficRecordDisplay(unittest.TestCase):
    """
    Unit test class to test the display functionality of TrafficRecordBasic and TrafficRecordDetailed.
    """

    def setUp(self):
        """
        Set up the test cases with instances of TrafficRecordBasic and TrafficRecordDetailed.
        """
        # Create a basic traffic record instance
        self.basic_record = TrafficRecordBasic(
            section_id="001",
            highway="Highway 1",
            section="Section A",
            section_length=10.5,
            section_description="Main section",
            date="2022-01-01",
            description="Description A",
            group="Group 1",
            type="Type A",
            county="County A",
            pTrucks=12.5,
            adt=15000,
            aadt=14000,
            direction="North",
            pct85=85.0,
            priority_points=10
        )

        # Create a detailed traffic record instance
        self.detailed_record = TrafficRecordDetailed(
            section_id="002",
            highway="Highway 2",
            section="Section B",
            section_length=20.0,
            section_description="Secondary section",
            date="2022-02-01",
            description="Description B",
            group="Group 2",
            type="Type B",
            county="County B",
            pTrucks=15.0,
            adt=20000,
            aadt=19000,
            direction="South",
            pct85=90.0,
            priority_points=15
        )

    def test_basic_record_display(self):
        """
        Test the display method of TrafficRecordBasic.
        """
        # Capture stdout output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            self.basic_record.display()

        # Check if the output is correct
        self.assertEqual(
            captured_output.getvalue().strip(),
            "ID: 001, Highway: Highway 1, Section: Section A, Length: 10.5 km"
        )

    def test_detailed_record_display(self):
        """
        Test the display method of TrafficRecordDetailed.
        """
        # Capture stdout output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            self.detailed_record.display()

        # Check if the output is correct
        self.assertEqual(
            captured_output.getvalue().strip(),
            "ID: 002, Highway: Highway 2, Section: Section B, Length: 20.0 km, "
            "Description: Secondary section, Date: 2022-02-01, Group: Group 2, Type: Type B, "
            "County: County B, Trucks: 15.0%, ADT: 20000, AADT: 19000, "
            "Direction: South, 85th Percentile: 90.0 km/h, Priority Points: 15"
        )


if __name__ == '__main__':
    unittest.main()
