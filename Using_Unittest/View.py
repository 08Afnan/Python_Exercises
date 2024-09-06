"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
SCHOOL: ALGONQUIN COLLEGE
"""

from Model import Model


class View:
    """
    The View class handles user interaction, including displaying menus,
    prompting for input, and displaying results. It interacts with the Model
    class to perform data operations.
    """

    def __init__(self):
        """
        Initializes the View class by displaying an ASCII box and creating an
        instance of the Model class.
        """
        self.display_ascii_box()
        self.model = Model()

    def display_ascii_box(self):
        """
        Displays an ASCII box with information about the traffic volumes project,
        the developer's name, student number, and the college.
        """
        lines = [
            "TRAFFIC VOLUMES - PROVINCIAL HIGHWAY SYSTEM",
            "DEVELOPED BY AFNAN ISLAM",
            "STUDENT NUMBER 041082073",
            "==========ALGONQUIN COLLEGE==========",
        ]
        max_length = max(len(line) for line in lines)
        box_width = max_length + 2

        print("+" + "=" * box_width + "+")
        for line in lines:
            centered_line = line.center(max_length)
            print("| " + centered_line + " |")
        print("+" + "=" * box_width + "+")

    def display_menu_name(self):
        """
        Displays the main menu name and information about the project and developer.
        """
        lines = [
            "",
            "Traffic Volumes - Provincial Highway System",
            "----------------------------------------",
            "========DEVELOPED BY AFNAN ISLAM========",
            "----------------------------------------",
            "===MAIN MENU==="
        ]

        max_length = max(len(line) for line in lines)

        for line in lines:
            centered_line = line.center(max_length)
            print(centered_line)

    def main_menu(self):
        """
        Displays the main menu and prompts the user to select an option.
        Handles user input and calls the appropriate method based on the selection.
        """
        menu_text = """
    CHOOSE WHAT YOU WOULD LIKE TO DO:
    1. Reload the data from the dataset
    2. Write to a new file
    3. Select and display one record or all records
    4. Create and store a new record
    5. Edit a record in the dataset
    6. Delete a record in the dataset
    
    To quit the program, enter Q/q
    """
        while True:
            self.display_menu_name()
            print(menu_text)
            try:
                option = input(">>> OPTION SELECT: ")
                if option.lower() == 'q':
                    break
                option = int(option)
                self.handle_option(option)
            except ValueError:
                print("Invalid input, please enter a number between 1 and 6, or 'Q/q' to quit.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def handle_option(self, option):
        """
        Handles the user's menu selection by calling the appropriate method.

        Args:
            option (int): The user's menu selection.
        """
        if option == 1:
            self.model.reload_dataset()
        elif option == 2:
            self.model.create_file()
        elif option == 3:
            self.display_records()
        elif option == 4:
            self.create_record()
        elif option == 5:
            self.edit_record()
        elif option == 6:
            self.delete_record()
        else:
            print("Invalid input, please enter a number between 1 and 6, or 'Q/q' to quit.")

    def display_records(self):
        """
        Prompts the user to select a row number between 1 and 5000 or 0 to view all records.
        Continues to ask for input until a valid number is entered.
        Displays the selected dataset.
        """
        choice = -1  # Initialize choice to an invalid number outside the desired range

        while choice < 0 or choice > 5000:
            try:
                choice = int(input("To display a single record, select a row number between 1 and 5000.\n"
                                   "To view all the records, enter 0: "))
                if choice < 0 or choice > 5000:
                    print("Invalid choice. Please enter a number between 0 and 5000.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Call the model's display_dataset method with the validated choice
        self.model.display_dataset(choice)

    def create_record(self):
        """
        Collects data from the user and creates a new traffic record using the Model class.
        Handles and prints any exceptions that occur during the process.
        """
        try:
            data = self.collect_data()
            self.model.create_trafficRecord(*data)
        except Exception as e:
            print(f"An error occurred while creating the record: {e}")

    def edit_record(self):
        """
        Prompts the user to enter a row number to edit. Collects new data from the user
        and updates the traffic record using the Model class.
        Handles and prints any exceptions that occur during the process.
        """
        try:
            selected_trafficRecord = int(input("Enter the row desired to edit: "))
            data = self.collect_data()
            self.model.update_trafficRecordList(selected_trafficRecord, *data)
        except ValueError:
            print("Invalid input, please enter a valid row number.")
        except Exception as e:
            print(f"An error occurred while editing the record: {e}")

    def delete_record(self):
        """
        Prompts the user to enter a row number to delete. Continues to ask for input until
        a valid number between 0 and 5000 is entered. Calls the Model's delete_trafficRecord
        method to delete the specified record.
        """
        delete_trafficRecord = -1  # Initialize to an invalid number outside the desired range

        while delete_trafficRecord < 0 or delete_trafficRecord > 5000:
            try:
                delete_trafficRecord = int(input("Enter the row desired to delete (between 0 and 5000): "))
                if delete_trafficRecord < 0 or delete_trafficRecord > 5000:
                    print("Invalid choice. Please enter a number between 0 and 5000.")
            except ValueError:
                print("Invalid input. Please enter a valid row number.")

        try:
            # Call the Model's delete_trafficRecord method with the validated choice
            self.model.delete_trafficRecord(delete_trafficRecord)
        except Exception as e:
            print(f"An error occurred while deleting the record: {e}")

    def collect_data(self):
        """
        Collects traffic record data from the user.

        Returns:
            tuple: A tuple containing the collected data.
        """
        section_id = input("Enter the section ID (e.g., 001, A12): ")
        highway = input("Enter the highway number/name (e.g., Highway 401, I-95): ")
        section = input("Enter the section name/number (e.g., Section 5, Segment A): ")
        section_length = input("Enter the section length in kilometers (e.g., 10.5): ")
        section_description = input("Enter a brief description of the section (e.g., Main Street to Elm Street): ")
        date = input("Enter the date of the record (MM/DD/YYY): ")
        description = input("Enter a description of the traffic record (e.g., Peak traffic, Construction zone): ")
        group = input("Enter the group classification (e.g., Urban, Rural): ")
        type = input("Enter the type of road (e.g., Arterial, Collector): ")
        county = input("Enter the county name (e.g., Orange County): ")
        pTrucks = input("Enter the percentage of trucks (e.g., 12.5): ")
        adt = input("Enter the Average Daily Traffic (ADT) count (e.g., 15000): ")
        aadt = input("Enter the Annual Average Daily Traffic (AADT) count (e.g., 18000): ")
        direction = input("Enter the traffic direction (e.g., Northbound, Southbound): ")
        pct85 = input("Enter the 85th percentile speed in km/h (e.g., 120): ")
        priority_points = input("Enter the priority points (e.g., 3): ")

        return (
            section_id, highway, section, section_length, section_description, date, description, group,
            type, county, pTrucks, adt, aadt, direction, pct85, priority_points
        )


if __name__ == "__main__":
    v = View()
    v.main_menu()
