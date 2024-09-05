"""
Name: Afnan Islam
Course Code: CST8333
"""

from datetime import datetime

class TrafficRecord:
    def __init__(self,
                 section_id=None,
                 highway=None,
                 section=None,
                 section_length=None,
                 section_description=None,
                 date=None,
                 description=None,
                 group=None,
                 type=None,
                 county=None,
                 pTrucks=None,
                 adt=None,
                 aadt=None,
                 direction=None,
                 pct85=None,
                 priority_points=None,):
        """
        Initialize a TrafficRecord object with optional parameters for various traffic data attributes.

        """
        self.section_id = self.process_as_integer(section_id)
        self.highway = self.process_as_integer(highway)
        self.section = self.process_as_integer(section)
        self.section_length = self.process_as_double(section_length)
        self.section_description = self.process_as_string(section_description)
        self.date = self.process_as_local_date(date)
        self.description = self.process_as_string(description)
        self.group = self.process_as_string(group)
        self.type = self.process_as_string(type)
        self.county = self.process_as_string(county)
        self.pTrucks = self.process_as_integer(pTrucks)
        self.adt = self.process_as_double(adt)
        self.aadt = self.process_as_double(aadt)
        self.direction = self.process_as_string(direction)
        self.pct85 = self.process_as_integer(pct85)
        self.priority_points = self.process_as_integer(priority_points)

    def process_as_string(self, value):
        """
        Process the input value as a string.

        Args:
            value (str): The value to process.

        Returns:
            str: The processed string or None if invalid.
        """
        if value is None or value.strip() == '' or value.strip().lower() == 'null':
            return None
        return value.strip()

    def process_as_integer(self, value):
        """
        Process the input value as an integer.

        Args:
            value (str): The value to process.

        Returns:
            int: The processed integer or None if invalid.
        """
        result = self.process_as_string(value)
        return int(result) if result is not None else None

    def process_as_double(self, value):
        """
        Process the input value as a double (float).

        Args:
            value (str): The value to process.

        Returns:
            float: The processed float or None if invalid.
        """
        result = self.process_as_string(value)
        return float(result) if result is not None else None

    def process_as_boolean(self, value):
        """
        Process the input value as a boolean.

        Args:
            value (str): The value to process.

        Returns:
            bool: The processed boolean or False if invalid.
        """
        result = self.process_as_string(value)
        return result.lower() in ('1', 'yes', 'true', 'on') if result is not None else False

    def process_as_local_date(self, value):
        """
        Process the input value as a date.

        Args:
            value (str): The value to process.

        Returns:
            datetime.date: The processed date or None if invalid.
        """
        result = self.process_as_string(value)
        return datetime.strptime(result, '%m/%d/%Y').date() if result is not None else None

    def __str__(self):
        """
        Return a string representation of the TrafficRecord object.

        Returns:
            str: A string containing all the attributes of the TrafficRecord.
        """
        return f"SECTION ID: {self.section_id},HIGHWAY: {self.highway},SECTION: {self.section},SECTION LENGTH: {self.section_length}," \
               f"SECTION DESCRIPTION: {self.section_description},Date: {self.date.strftime('%m/%d/%Y') if self.date else None},DESCRIPTION: {self.description},GROUP: {self.group}," \
               f"TYPE: {self.type},COUNTY: {self.county},PTRUCKS: {self.pTrucks},ADT: {self.adt}," \
               f"ADT: {self.aadt},DIRECTION: {self.direction},85PCT: {self.pct85},PRIORITY_POINTS: {self.priority_points}"

