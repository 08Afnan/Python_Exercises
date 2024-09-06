"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

from Controller import Controller

class Model:
    """
    Model class that interfaces with the Controller to manage traffic records.
    
    Attributes:
        controller (Controller): An instance of the Controller class.
    """
    
    def __init__(self):
        """
        Initialize a Model instance and load the dataset through the controller.
        """
        self.controller = Controller()
        self.controller.load_dataset()

    def load_dataset(self):
        """
        Load the dataset through the controller.
        """
        self.controller.load_dataset()

    def create_file(self):
        """
        Create a new file with the traffic records through the controller.
        """
        self.controller.create_file()

    def display_dataset(self, number, format='basic'):
        """
        Display the dataset through the controller.
        
        Parameters:
            number (int): Number of records to display. If 0, display all records.
            format (str): Format to display records, either 'basic' or 'detailed'.
        """
        self.controller.display_dataset(number, format)

    def add_trafficRecord(self, section_id, highway, section, section_length, section_description, date, description, group,
                          type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Add a new traffic record through the controller.
        
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
        self.controller.add_trafficRecord(
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        )

    def edit_trafficRecord(self, selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
                           type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Edit an existing traffic record through the controller.
        
        Parameters:
            selected_trafficRecord (int): Index of the traffic record to edit.
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
        self.controller.edit_trafficRecord(
            selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        )

    def delete_trafficRecord(self, delete_trafficRecord):
        """
        Delete a traffic record through the controller.
        
        Parameters:
            delete_trafficRecord (int): Index of the traffic record to delete.
        """
        self.controller.delete_trafficRecord(delete_trafficRecord)

    def display_trafficRecordData(self, x):
        """
        Display a specified number of traffic records through the controller.
        
        Parameters:
            x (int): Number of records to display.
        """
        self.controller.display_trafficRecordData(x)

    def search_records(self, search_criteria):
        """
        Search for records based on multiple columns.

        Parameters:
            search_criteria (dict): Dictionary where keys are column names and values are the search values.

        Returns:
            list: List of traffic records that match the search criteria.
        """
        return self.controller.search_records(search_criteria)

 