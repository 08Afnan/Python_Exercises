"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

from abc import ABC, abstractmethod

class TrafficRecordDisplay(ABC):
    """
    Abstract base class for displaying traffic records.
    
    Methods:
        display(): Abstract method to display traffic record information.
    """
    @abstractmethod
    def display(self):
        """
        Abstract method to display traffic record information.
        """
        pass

class TrafficRecord(TrafficRecordDisplay):
    """
    Traffic record class that stores various attributes of a traffic record.
    
    Attributes:
        section_id (str): Section ID.
        highway (str): Highway name.
        section (str): Section name.
        section_length (float): Section length.
        section_description (str): Section description.
        date (str): Date.
        description (str): Description.
        group (str): Group.
        type (str): Type.
        county (str): County.
        pTrucks (float): Percentage of trucks.
        adt (int): Average daily traffic.
        aadt (int): Annual average daily traffic.
        direction (str): Direction.
        pct85 (float): 85th percentile speed.
        priority_points (int): Priority points.
    
    Methods:
        display(): Abstract method to display traffic record information.
    """
    def __init__(self, section_id, highway, section, section_length, section_description, date, description, group,
                 type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Initialize a TrafficRecord instance with the provided attributes.
        
        Parameters:
            section_id (str): Section ID.
            highway (str): Highway name.
            section (str): Section name.
            section_length (float): Section length.
            section_description (str): Section description.
            date (str): Date.
            description (str): Description.
            group (str): Group.
            type (str): Type.
            county (str): County.
            pTrucks (float): Percentage of trucks.
            adt (int): Average daily traffic.
            aadt (int): Annual average daily traffic.
            direction (str): Direction.
            pct85 (float): 85th percentile speed.
            priority_points (int): Priority points.
        """
        self.section_id = section_id
        self.highway = highway
        self.section = section
        self.section_length = section_length
        self.section_description = section_description
        self.date = date
        self.description = description
        self.group = group
        self.type = type
        self.county = county
        self.pTrucks = pTrucks
        self.adt = adt
        self.aadt = aadt
        self.direction = direction
        self.pct85 = pct85
        self.priority_points = priority_points

    @abstractmethod
    def display(self):
        """
        Abstract method to display traffic record information.
        """
        pass
