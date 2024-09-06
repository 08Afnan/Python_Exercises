"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

import csv
import TrafficRecord as TrafficRecord
import pandas as pd


class Controller(object):
    """
    The Controller class handles the loading, manipulation, and saving of traffic records.
    """

    def __init__(self):
        """Initializes the Controller with an empty list of traffic records."""
        self.trafficRecordList = []

    def load_dataset(self):
        """
        Loads the dataset from a CSV file into the trafficRecordList.
        Limits the number of records to 5000 if there are more in the dataset.
        """
        try:
            columns = ["SECTION_ID", "HIGHWAY", "SECTION", "SECTION_LENGTH", "SECTION_DESCRIPTION", "Date", "DESCRIPTION",
                       "GROUP", "TYPE", "COUNTY", "PTRUCKS", "ADT", "AADT",
                       "DIRECTION", "PCT85", "PRIORITY_POINTS"]
            dataframe = pd.read_csv('Traffic_Volumes_-_Provincial_Highway_System.csv', skiprows=1, names=columns)
            self.trafficRecordList = [
                TrafficRecord.TrafficRecord(
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
        Creates a new CSV file from the current trafficRecordList.
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

    def display_dataset(self, number):
        """
        Displays records from the trafficRecordList.

        Args:
            number (int): If 0, displays all records. Otherwise, displays the specified record number.
        """
        header = ("SECTION ID", "HIGHWAY", "SECTION", "SECTION LENGTH", "SECTION DESCRIPTION", "Date", "DESCRIPTION",
                  "GROUP", "TYPE", "COUNTY", "PTRUCKS", "ADT", "AADT",
                  "DIRECTION", "85PCT", "PRIORITY_POINTS")
        print(f"{'':>30} {' '.join(header)}")

        if number == 0:
            for idx, row in enumerate(self.trafficRecordList):
                print(f"{idx:>30}", row)
                # Print "DEVELOPED BY AFNAN ISLAM" after every 10 rows
                if (idx + 1) % 10 == 0:
                    print(f"{'':>25} {"========================================================================DEVELOPED BY AFNAN ISLAM========================================================================"}")
        else:
            print(f"Displaying record number {number}:\n                              ", self.trafficRecordList[number - 1])

    def add_trafficRecord(self, section_id, highway, section, section_length, section_description, date, description, group,
                          type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Adds a new traffic record to the trafficRecordList.

        Args:
            section_id (str): The section ID.
            highway (str): The highway name.
            section (str): The section name.
            section_length (str): The section length.
            section_description (str): The section description.
            date (str): The date.
            description (str): The description.
            group (str): The group.
            type (str): The type.
            county (str): The county.
            pTrucks (str): The percentage of trucks.
            adt (str): The average daily traffic.
            aadt (str): The annual average daily traffic.
            direction (str): The direction.
            pct85 (str): The 85th percentile speed.
            priority_points (str): The priority points.
        """
        self.trafficRecordList.append(TrafficRecord.TrafficRecord(
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        ))

    def edit_trafficRecord(self, selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
                           type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Edits an existing traffic record in the trafficRecordList.

        Args:
            selected_trafficRecord (int): The index of the traffic record to edit (1-based).
            section_id (str): The section ID.
            highway (str): The highway name.
            section (str): The section name.
            section_length (str): The section length.
            section_description (str): The section description.
            date (str): The date.
            description (str): The description.
            group (str): The group.
            type (str): The type.
            county (str): The county.
            pTrucks (str): The percentage of trucks.
            adt (str): The average daily traffic.
            aadt (str): The annual average daily traffic.
            direction (str): The direction.
            pct85 (str): The 85th percentile speed.
            priority_points (str): The priority points.
        """
        self.trafficRecordList[selected_trafficRecord - 1] = TrafficRecord.TrafficRecord(
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        )

    def delete_trafficRecord(self, delete_trafficRecord):
        """
        Deletes a traffic record from the trafficRecordList.

        Args:
            delete_trafficRecord (int): The index of the traffic record to delete (1-based).
        """
        if 0 < delete_trafficRecord <= len(self.trafficRecordList):
            del self.trafficRecordList[delete_trafficRecord - 1]
        else:
            print(f"Invalid index: {delete_trafficRecord}")

    def display_trafficRecordData(self, x):
        """
        Displays a subset of the trafficRecordList as a DataFrame.

        Args:
            x (int): The number of records to display.
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
