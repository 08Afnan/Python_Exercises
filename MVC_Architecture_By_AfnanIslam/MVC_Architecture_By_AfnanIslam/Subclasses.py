"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
STUDENT NUMBER: 041082073
SCHOOL: ALGONQUIN COLLEGE
"""

from TrafficRecordDisplay import TrafficRecord

class TrafficRecordBasic(TrafficRecord):
    """
    Basic traffic record class inheriting from TrafficRecord.
    
    Methods:
        display(): Prints basic traffic record information.
    """
    
    def display(self):
        """
        Display basic traffic record information.
        """
        print(f"ID: {self.section_id}, Highway: {self.highway}, Section: {self.section}, Length: {self.section_length} km")

class TrafficRecordDetailed(TrafficRecord):
    """
    Detailed traffic record class inheriting from TrafficRecord.
    
    Methods:
        display(): Prints detailed traffic record information.
    """
    
    def display(self):
        """
        Display detailed traffic record information.
        """
        print(f"ID: {self.section_id}, Highway: {self.highway}, Section: {self.section}, Length: {self.section_length} km, "
              f"Description: {self.section_description}, Date: {self.date}, Group: {self.group}, Type: {self.type}, "
              f"County: {self.county}, Trucks: {self.pTrucks}%, ADT: {self.adt}, AADT: {self.aadt}, "
              f"Direction: {self.direction}, 85th Percentile: {self.pct85} km/h, Priority Points: {self.priority_points}")
