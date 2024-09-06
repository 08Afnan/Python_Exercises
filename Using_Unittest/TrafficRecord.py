"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

class TrafficRecord:
    """
    A class to represent a traffic record.

    Attributes:
        section_id (str): The section ID.
        highway (str): The highway name.
        section (str): The section name.
        section_length (str): The length of the section.
        section_description (str): The description of the section.
        date (str): The date of the record.
        description (str): A brief description.
        group (str): The group category.
        type (str): The type category.
        county (str): The county name.
        pTrucks (str): The percentage of trucks.
        adt (str): The average daily traffic.
        aadt (str): The annual average daily traffic.
        direction (str): The direction.
        pct85 (str): The 85th percentile speed.
        priority_points (str): The priority points.
    """

    def __init__(self, section_id, highway, section, section_length, section_description, date, description, group,
                 type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Constructs all the necessary attributes for the traffic record object.

        Args:
            section_id (str): The section ID.
            highway (str): The highway name.
            section (str): The section name.
            section_length (str): The length of the section.
            section_description (str): The description of the section.
            date (str): The date of the record.
            description (str): A brief description.
            group (str): The group category.
            type (str): The type category.
            county (str): The county name.
            pTrucks (str): The percentage of trucks.
            adt (str): The average daily traffic.
            aadt (str): The annual average daily traffic.
            direction (str): The direction.
            pct85 (str): The 85th percentile speed.
            priority_points (str): The priority points.
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

    def __str__(self):
        """
        Returns a string representation of the traffic record object.

        Returns:
            str: A string that concatenates all the attributes of the traffic record.
        """
        return (f"{self.section_id} {self.highway} {self.section} {self.section_length} "
                f"{self.section_description} {self.date} {self.description} {self.group} {self.type} "
                f"{self.county} {self.pTrucks} {self.adt} {self.aadt} {self.direction} "
                f"{self.pct85} {self.priority_points}")
