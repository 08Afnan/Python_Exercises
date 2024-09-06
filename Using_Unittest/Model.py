"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

from Controller import Controller

class Model:
    """
    The Model class interacts with the Controller class to perform various
    operations such as reloading datasets, creating files, displaying datasets,
    and managing traffic records.

    Attributes:
        controller (Controller): An instance of the Controller class.
    """

    def __init__(self):
        """
        Initializes the Model class by creating an instance of the Controller class.
        """
        # Instance created
        self.controller = Controller()

    def reload_dataset(self):
        """
        Reloads the dataset using the Controller's load_dataset method.
        Prints a success message upon successful reloading.
        Handles and prints any exceptions that occur during the process.
        """
        try:
            self.controller.load_dataset()
            print("***Dataset reloaded successfully***")
        except Exception as e:
            print(f"An error occurred while reloading the dataset: {e}")

    def create_file(self):
        """
        Creates a new file using the Controller's create_file method.
        Prints a success message upon successful file creation.
        Handles and prints any exceptions that occur during the process.
        """
        try:
            self.controller.create_file()
            print("***New file written successfully***")
        except Exception as e:
            print(f"An error occurred while writing the file: {e}")

    def display_dataset(self, user_input):
        """
        Displays the dataset based on user input using the Controller's display_dataset method.
        Prints a success message upon successful display.
        Handles and prints any exceptions that occur during the process.

        Args:
            user_input: The input provided by the user to filter the dataset.
        """
        try:
            self.controller.display_dataset(user_input)
            print("***Record displayed successfully***")
        except Exception as e:
            print(f"An error occurred while displaying the record: {e}")

    def create_trafficRecord(self, section_id, highway, section, section_length, section_description, date, description, group,
                             type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Creates a new traffic record using the Controller's add_trafficRecord method.
        Prints a success message upon successful creation.
        Handles and prints any exceptions that occur during the process.

        Args:
            section_id (str): The section ID.
            highway (str): The highway name or number.
            section (str): The section name or number.
            section_length (float): The length of the section.
            section_description (str): A description of the section.
            date (str): The date of the record.
            description (str): A description of the record.
            group (str): The group associated with the record.
            type (str): The type of record.
            county (str): The county where the record is located.
            pTrucks (int): The number of trucks.
            adt (int): The average daily traffic.
            aadt (int): The annual average daily traffic.
            direction (str): The direction of traffic.
            pct85 (float): The 85th percentile speed.
            priority_points (int): The priority points assigned to the record.
        """
        try:
            self.controller.add_trafficRecord(section_id, highway, section, section_length, section_description, date, description, group,
                                              type, county, pTrucks, adt, aadt, direction, pct85, priority_points)
            print("***New record created successfully***")
        except Exception as e:
            print(f"An error occurred while creating a new record: {e}")

    def update_trafficRecordList(self, selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
                                 type, county, pTrucks, adt, aadt, direction, pct85, priority_points):
        """
        Updates an existing traffic record using the Controller's edit_trafficRecord method.
        Prints a success message upon successful update.
        Handles and prints any exceptions that occur during the process.

        Args:
            selected_trafficRecord (str): The selected traffic record to be updated.
            section_id (str): The section ID.
            highway (str): The highway name or number.
            section (str): The section name or number.
            section_length (float): The length of the section.
            section_description (str): A description of the section.
            date (str): The date of the record.
            description (str): A description of the record.
            group (str): The group associated with the record.
            type (str): The type of record.
            county (str): The county where the record is located.
            pTrucks (int): The number of trucks.
            adt (int): The average daily traffic.
            aadt (int): The annual average daily traffic.
            direction (str): The direction of traffic.
            pct85 (float): The 85th percentile speed.
            priority_points (int): The priority points assigned to the record.
        """
        try:
            self.controller.edit_trafficRecord(selected_trafficRecord, section_id, highway, section, section_length, section_description, date, description, group,
                                               type, county, pTrucks, adt, aadt, direction, pct85, priority_points)
            print("***Record edited successfully***")
        except Exception as e:
            print(f"An error occurred while editing the record: {e}")

    def delete_trafficRecord(self, delete_trafficRecord):
        """
        Deletes a traffic record using the Controller's delete_trafficRecord method.
        Prints a success message upon successful deletion.
        Handles and prints any exceptions that occur during the process.

        Args:
            delete_trafficRecord (str): The traffic record to be deleted.
        """
        try:
            self.controller.delete_trafficRecord(delete_trafficRecord)
            print("***Record successfully deleted***")
        except Exception as e:
            print(f"An error occurred while deleting the data: {e}")

    def display_choice(self, choice):
        """
        Displays a specific choice of traffic record data using the Controller's display_trafficRecordData method.
        Handles and prints any exceptions that occur during the process.

        Args:
            choice (str): The choice of traffic record data to be displayed.
        """
        try:
            self.controller.display_trafficRecordData(choice)
        except Exception as e:
            print(f"An error occurred while displaying the choice: {e}")
