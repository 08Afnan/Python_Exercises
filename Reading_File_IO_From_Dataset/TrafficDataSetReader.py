"""
Name: Afnan Islam
Course Code: CST8333
"""

import csv
from TrafficRecord import TrafficRecord


class TrafficDataSetReader:
    def main(self):
        """
        Main method to execute the workflow of loading and printing traffic data.
        """
        trafficList = []
        self.load_list(trafficList)
        self.print_list(trafficList)
        print("Program by AFNAN ISLAM")

    def load_list(self, list):
        """
        Loads traffic data from a CSV file into the provided list.

        Args:
            list (list): The list to populate with TrafficRecord objects.
        """
        try:
            print("Program by AFNAN ISLAM")
            with self.open_file("Traffic_Volumes_-_Provincial_Highway_System.csv") as csv_file:
                if csv_file:  # Ensure the file is successfully opened
                    reader = csv.DictReader(csv_file)
                    for record in reader:
                        traffic = TrafficRecord(
                            record.get("SECTION ID"),
                            record.get("HIGHWAY"),
                            record.get("SECTION"),
                            record.get("SECTION LENGTH"),
                            record.get("SECTION DESCRIPTION"),
                            record.get("Date"),
                            record.get("DESCRIPTION"),
                            record.get("GROUP"),
                            record.get("TYPE"),
                            record.get("COUNTY"),
                            record.get("PTRUCKS"),
                            record.get("ADT"),
                            record.get("ADT"),  # Duplicate entry?
                            record.get("DIRECTION"),
                            record.get("85PCT"),
                            record.get("PRIORITY_POINTS"),
                        )
                        list.append(traffic)
        except IOError as ex:
            print(ex)

    def print_list(self, list):
        """
        Prints each TrafficRecord object in the provided list.

        Args:
            list (list): The list containing TrafficRecord objects to print.
        """
        for traffic in list:
            print(traffic)
            print()

    def open_file(self, file_name):
        """
        Opens a file and returns the file object.

        Args:
            file_name (str): The name of the file to open.

        Returns:
            file object: The opened file object, or None if an error occurs.
        """
        try:
            return open(file_name, mode='r', encoding='utf-8-sig')
        except FileNotFoundError as ex:
            print(f"File not found: {ex}")
        except IOError as ex:
            print(f"Problem opening file: {ex}")
        return None


if __name__ == "__main__":
    TrafficDataSetReader().main()