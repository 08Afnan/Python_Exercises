"""
COURSE: CST8333 Programming Language Research Project
STUDENT NAME: AFNAN ISLAM
STUDENT NUMBER: 041082073
SCHOOL: ALGONQUIN COLLEGE
"""

from Model import Model

class View:
    """
    View class responsible for displaying menus and handling user interaction.
    
    Attributes:
        model (Model): An instance of the Model class to interact with the dataset.
    """
    def __init__(self):
        """
        Initialize a View instance, display the ASCII box, and load the model.
        """
        self.display_ascii_box()
        self.model = Model()

    def display_ascii_box(self):
        """
        Display an ASCII art box with project and developer information.
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
        Display the main menu name and header information.
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
        Display the main menu and handle user input for various options.
        """
        menu_text = """
    CHOOSE WHAT YOU WOULD LIKE TO DO:
    1. Reload the data from the dataset
    2. Write to a new file
    3. Select and display one record or all records
    4. Create and store a new record
    5. Edit a record in the dataset
    6. Delete a record in the dataset
    7. Display records in detailed format

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
                print("Invalid input. Please enter a number between 1 and 7 or Q to quit.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def handle_option(self, option):
        """
        Handle the selected menu option.
        
        Parameters:
            option (int): The selected menu option.
        """
        if option == 1:
            print("Loading Dataset ...")
            self.model.load_dataset()
        elif option == 2:
            print("Creating file ...")
            self.model.create_file()
        elif option == 3:
            number = int(input("Enter record number (0 for all): "))
            self.model.display_dataset(number)
        elif option == 4:
            self.add_traffic_record()
        elif option == 5:
            self.edit_traffic_record()
        elif option == 6:
            self.delete_traffic_record()
        elif option == 7:
            number = int(input("Enter record number (0 for all): "))
            self.model.display_dataset(number, format='detailed')
        else:
            print("Invalid option.")

    def add_traffic_record(self):
        """
        Prompt the user to enter details for a new traffic record and add it to the dataset.
        """
        section_id = input("Enter Section ID: ")
        highway = input("Enter Highway: ")
        section = input("Enter Section: ")
        section_length = float(input("Enter Section Length: "))
        section_description = input("Enter Section Description: ")
        date = input("Enter Date: ")
        description = input("Enter Description: ")
        group = input("Enter Group: ")
        type = input("Enter Type: ")
        county = input("Enter County: ")
        pTrucks = float(input("Enter Percentage of Trucks: "))
        adt = int(input("Enter ADT: "))
        aadt = int(input("Enter AADT: "))
        direction = input("Enter Direction: ")
        pct85 = float(input("Enter 85th Percentile Speed: "))
        priority_points = int(input("Enter Priority Points: "))

        self.model.add_trafficRecord(section_id, highway, section, section_length, section_description, date, description,
                                     group, type, county, pTrucks, adt, aadt, direction, pct85, priority_points)

    def edit_traffic_record(self):
        """
        Prompt the user to enter new details for an existing traffic record and update it in the dataset.
        """
        selected_record = int(input("Enter the number of the record to edit: "))
        section_id = input("Enter new Section ID: ")
        highway = input("Enter new Highway: ")
        section = input("Enter new Section: ")
        section_length = float(input("Enter new Section Length: "))
        section_description = input("Enter new Section Description: ")
        date = input("Enter new Date: ")
        description = input("Enter new Description: ")
        group = input("Enter new Group: ")
        type = input("Enter new Type: ")
        county = input("Enter new County: ")
        pTrucks = float(input("Enter new Percentage of Trucks: "))
        adt = int(input("Enter new ADT: "))
        aadt = int(input("Enter new AADT: "))
        direction = input("Enter new Direction: ")
        pct85 = float(input("Enter new 85th Percentile Speed: "))
        priority_points = int(input("Enter new Priority Points: "))

        self.model.edit_trafficRecord(selected_record, section_id, highway, section, section_length, section_description,
                                      date, description, group, type, county, pTrucks, adt, aadt, direction, pct85,
                                      priority_points)

    def delete_traffic_record(self):
        """
        Prompt the user to enter the number of a record to delete and remove it from the dataset.
        """
        selected_record = int(input("Enter the number of the record to delete: "))
        self.model.delete_trafficRecord(selected_record)

if __name__ == "__main__":
    v = View()
    v.main_menu()
