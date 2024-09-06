"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

import csv
import pandas as pd
from Subclasses import TrafficRecordBasic, TrafficRecordDetailed

class Controller(object):
    """
    Controller class for managing traffic records.
    
    Attributes:
        trafficRecordList (list): A list to store traffic records.
    """
    
    def __init__(self):
        """
        Initialize a Controller instance with an empty traffic record list.
        """
        self.trafficRecordList = []

    def load_dataset(self):
        """
        Load the dataset from a CSV file and populate the traffic record list.
        Truncates the list to 5000 records if it exceeds this number.
        
        If the file is not found, an error message is printed.
        """
        try:
            columns = ["SECTION_ID", "HIGHWAY", "SECTION", "SECTION_LENGTH", "SECTION_DESCRIPTION", "Date", "DESCRIPTION",
                       "GROUP", "TYPE", "COUNTY", "PTRUCKS", "ADT", "AADT",
                       "DIRECTION", "PCT85", "PRIORITY_POINTS"]
            dataframe = pd.read_csv('Traffic_Volumes_-_Provincial_Highway_System.csv', skiprows=1, names=columns)
            self.trafficRecordList = [
                TrafficRecordBasic(
                    row.SECTION_ID, row.HIGHWAY, row.SECTION, row.SECTION_LENGTH, row.SECTION_DESCRIPTION, row.Date,
                    row.DESCRIPTION, row.GROUP, row.TYPE, row.COUNTY, row.PTRUCKS,
                    row.ADT, row.AADT, row.DIRECTION, row.PCT85, row.PRIORITY_POINTS
                ) for row in dataframe.itertuples(index=False)
            ]
            if len(self.trafficRecordList) > 5000:
                self.trafficRecordList = self.trafficRecordList[:5000]
        except FileNotFoundError:
            print("File not found / unavailable")

    def create_file(self):
        """
        Create a new CSV file and write the traffic records to it.
        """
        with open('NewTrafficRecordDataSet.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "SECTION ID", "HIGHWAY", "SECTION", "SECTION LENGTH", "SECTION DESCRIPTION", "Date", "DESCRIPTION",
                "GROUP", "TYPE", "COUNTY", "PTRUCKS", "ADT", "AADT",
                "DIRECTION", "85PCT", "PRIORITY_POINTS"
            ])
            writer.writerows([
                [
                    trafficRecord.section_id, trafficRecord.highway, trafficRecord.section, trafficRecord.section_length, trafficRecord.section_description,
                    trafficRecord.date, trafficRecord.description, trafficRecord.group, trafficRecord.type,
                    trafficRecord.county, trafficRecord.pTrucks, trafficRecord.adt, trafficRecord.aadt,
                    trafficRecord.direction, trafficRecord.pct85, trafficRecord.priority_points
                ] for trafficRecord in self.trafficRecordList
            ])

    def display_dataset(self, number, format='basic'):
        """
        Display the dataset.
        
        Parameters:
            number (int): Number of records to display. If 0, display all records.
            format (str): Format to display records, either 'basic' or 'detailed'.
        """
        if format == 'detailed':
            records = [TrafficRecordDetailed(*record.__dict__.values()) for record in self.trafficRecordList]
        else:
            records = self.trafficRecordList

        if number == 0:
            for idx, record in enumerate(records):
                record.display()
                if (idx + 1) % 10 == 0:
                    print("================================================================DEVELOPED BY AFNAN ISLAM================================================================")
        else:
            records[number - 1].display()

    def add_trafficRecord(self, section_id, highway, section, section_length, section_description, date, description, group,
                          type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Add a new traffic record to the list.
        
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
        self.trafficRecordList.append(TrafficRecordBasic(
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        ))

    def edit_trafficRecord(self, selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
                           type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Edit an existing traffic record in the list.
        
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
        self.trafficRecordList[selected_trafficRecord - 1] = TrafficRecordBasic(
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        )

    def delete_trafficRecord(self, delete_trafficRecord):
        """
        Delete a traffic record from the list.
        
        Parameters:
            delete_trafficRecord (int): Index of the traffic record to delete.
        """
        if 0 < delete_trafficRecord <= len(self.trafficRecordList):
            del self.trafficRecordList[delete_trafficRecord - 1]
        else:
            print(f"Invalid index: {delete_trafficRecord}")

    def display_trafficRecordData(self, x):
        """
        Display a specified number of traffic records.
        
        Parameters:
            x (int): Number of records to display.
        """
        self.load_dataset()
        if x < len(self.trafficRecordList):
            self.trafficRecordList = self.trafficRecordList[:x]
        data = pd.DataFrame([{
            'section_id': t.section_id, 'highway': t.highway, 'section': t.section, 'section_length': t.section_length,
            'section_description': t.section_description, 'date': t.date, 'description': t.description,
            'group': t.group, 'type': t.type, 'county': t.county, 'pTrucks': t.pTrucks, 'adt': t.adt,
            'aadt': t.aadt, 'direction': t.direction, 'pct85': t.pct85, 'priority_points': t.priority_points
        } for t in self.trafficRecordList])
        print(data)
        
    def search_records(self, search_criteria):
        """
        Search for records based on multiple columns.

        Parameters:
            search_criteria (dict): Dictionary where keys are column names and values are the search values.

        Returns:
            list: List of traffic records that match the search criteria.
        """
        filtered_records = self.trafficRecordList
        for key, value in search_criteria.items():
            filtered_records = [record for record in filtered_records if str(getattr(record, key)) == str(value)]
        return filtered_records
