from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QHeaderView,\
     QTableWidgetItem, QAbstractItemView, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, Qt
import csv

from Buttons import EditButton, DeleteButton

from UpdateEmployeeWindow import UpdateEmployeeWindow
from DataVisualizationWindow import DataVisualizationWindow


class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setFixedHeight(833)
        self.widget.setFixedWidth(1342)
        self.update_employee_window = None
        self.data_visualization_window = None
        self.index = 1  # Used to organize the data_visualization/update_employee windows
        self.update_emp_index = None
        self.data_vis_index = None

        loadUi("EmployeesGUI.ui", self)

        # Used to add new features to the employee table
        self.format_table_widget()

        self.employees_list = []

        # # Fake Data
        # self.employees_list = [
        #     {"id": 1000, "name": "Hans", "position": "CEO",
        #      "salary": 125000, "country": "Germany", "age": 54},
        #     {"id": 1001, "name": "Hiroshi", "position": "CFO",
        #      "salary": 115000, "country": "Japan", "age": 52},
        #     {"id": 1002, "name": "Carlos", "position": "CTO",
        #      "salary": 112000, "country": "Brazil", "age": 49},
        #     {"id": 1003, "name": "Giovanni", "position": "COO",
        #      "salary": 109000, "country": "Italy", "age": 50},
        #     {"id": 1004, "name": "Liam", "position": "Human Resources",
        #      "salary": 86000, "country": "Australia", "age": 45},
        #     {"id": 1005, "name": "José", "position": "Product Manager",
        #      "salary": 96000, "country": "Brazil", "age": 41},
        #     {"id": 1006, "name": "Friedrich", "position": "Product Manager",
        #      "salary": 92000, "country": "Germany", "age": 43},
        #     {"id": 1007, "name": "Kenji", "position": "Software Engineer",
        #      "salary": 89000, "country": "Japan", "age": 36},
        #     {"id": 1008, "name": "Oscar", "position": "Software Engineer",
        #      "salary": 84000, "country": "Australia", "age": 35},
        #     {"id": 1009, "name": "Francesco", "position": "Software Engineer",
        #      "salary": 82000, "country": "Italy", "age": 38},
        #     {"id": 1010, "name": "Klaus", "position": "Software Engineer",
        #      "salary": 81000, "country": "Germany", "age": 34},
        #     {"id": 1011, "name": "Luiz", "position": "Software Engineer",
        #      "salary": 80000, "country": "Brazil", "age": 33},
        #     {"id": 1012, "name": "Leonardo", "position": "Software Engineer",
        #      "salary": 79000, "country": "Italy", "age": 32},
        #     {"id": 1013, "name": "Jack", "position": "Software Engineer",
        #      "salary": 78000, "country": "Australia", "age": 35},
        #     {"id": 1014, "name": "Takeshi", "position": "Software Engineer",
        #      "salary": 77000, "country": "Japan", "age": 36},
        #     {"id": 1015, "name": "Johannes", "position": "Data Analyst",
        #      "salary": 70000, "country": "Germany", "age": 28},
        #     {"id": 1016, "name": "Oliver", "position": "Data Analyst",
        #      "salary": 69000, "country": "United Kingdom", "age": 29},
        #     {"id": 1017, "name": "Olivia", "position": "Data Analyst",
        #      "salary": 68000, "country": "United States", "age": 31},
        #     {"id": 1018, "name": "Sophia", "position": "Data Analyst",
        #      "salary": 67000, "country": "United States", "age": 30},
        #     {"id": 1019, "name": "Amelia", "position": "Data Analyst",
        #      "salary": 66000, "country": "United Kingdom", "age": 29},
        #     {"id": 1020, "name": "Emma", "position": "Data Analyst",
        #      "salary": 65000, "country": "Canada", "age": 27},
        #     {"id": 1021, "name": "Liam", "position": "Graphic Designer",
        #      "salary": 62000, "country": "United States", "age": 30},
        #     {"id": 1022, "name": "Isabella", "position": "Graphic Designer",
        #      "salary": 61000, "country": "United Kingdom", "age": 28},
        #     {"id": 1023, "name": "Aiden", "position": "Graphic Designer",
        #      "salary": 60000, "country": "Canada", "age": 31},
        #     {"id": 1024, "name": "Mia", "position": "Sales Manager",
        #      "salary": 95000, "country": "United States", "age": 39},
        #     {"id": 1025, "name": "Ava", "position": "Sales Manager",
        #      "salary": 90000, "country": "United Kingdom", "age": 37},
        #     {"id": 1026, "name": "Jackson", "position": "Sales Manager",
        #      "salary": 88000, "country": "Canada", "age": 40},
        #     {"id": 1027, "name": "Madison", "position": "Marketing Manager",
        #      "salary": 105000, "country": "United States", "age": 42},
        #     {"id": 1028, "name": "Sophie", "position": "Marketing Manager",
        #      "salary": 98000, "country": "United Kingdom", "age": 38},
        #     {"id": 1029, "name": "Lucas", "position": "Marketing Manager",
        #      "salary": 94000, "country": "Canada", "age": 41},
        #     {"id": 1030, "name": "Charlotte", "position": "Human Resources Manager",
        #      "salary": 100000, "country": "United States", "age": 46},
        #     {"id": 1031, "name": "Jack", "position": "Human Resources Manager",
        #      "salary": 93000, "country": "United Kingdom", "age": 44},
        #     {"id": 1032, "name": "Emily", "position": "Human Resources Manager",
        #      "salary": 91000, "country": "Canada", "age": 43},
        #     {"id": 1033, "name": "Noah", "position": "Project Manager",
        #      "salary": 107000, "country": "United States", "age": 47},
        #     {"id": 1034, "name": "Grace", "position": "Project Manager",
        #      "salary": 102000, "country": "United Kingdom", "age": 39},
        #     {"id": 1035, "name": "Logan", "position": "Project Manager",
        #      "salary": 98000, "country": "United States", "age": 41}
        # ]

        self.display_employees()

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog_to_new_emp)

        self.dataVisualizationButton.clicked.connect(self.switch_dialog_to_data_vis)

        self.CSV_Import.clicked.connect(self.import__csv)

        self.CSV_Download.clicked.connect(self.download_csv)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

    # Used to switch the window to the AddEmployeeWindow class
    def switch_dialog_to_new_emp(self):
        print("switch_dialog_to_new_emp() is called")
        self.widget.setCurrentIndex(1)

    # Used to switch the window to the UpdateEmployeeWindow class
    def switch_dialog_to_update_emp(self, current_emp):
        print("switch_dialog_to_update_emp() is called")
        if self.update_employee_window is None:
            # New window for updating employees
            self.update_employee_window = UpdateEmployeeWindow(self.widget,
                                                          self.display_employees,
                                                          self.employees_list)
            self.widget.addWidget(self.update_employee_window)

            self.index = self.index + 1
            self.update_emp_index = self.index

        self.update_employee_window.find_current_emp(current_emp)
        self.widget.setCurrentIndex(self.update_emp_index)

    # Used to switch the window to the DataVisualization class
    def switch_dialog_to_data_vis(self):
        print("switch_dialog_to_data_visualization() is called")
        if self.data_visualization_window is None:
            self.data_visualization_window = DataVisualizationWindow(self.widget,
                                                          self.employees_list)
            self.widget.addWidget(self.data_visualization_window)

            self.index = self.index + 1
            self.data_vis_index = self.index

        self.widget.setCurrentIndex(self.data_vis_index)

    def format_table_widget(self):
        # Used to stretch the columns
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        # Used to locate the id column index
        self.id_col_index = 0

        # Used to locate the delete/edit column index
        self.delete_col_index = self.tableWidget.columnCount() - 1
        self.edit_col_index = self.tableWidget.columnCount() - 2

        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.id_col_index, QHeaderView.Fixed)

        # Used to design the delete/edit buttons width
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.delete_col_index, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.edit_col_index, QHeaderView.Fixed)

        self.tableWidget.horizontalHeader().resizeSection(self.id_col_index, 100)

        self.tableWidget.horizontalHeader().resizeSection(self.delete_col_index, 80)
        self.tableWidget.horizontalHeader().resizeSection(self.edit_col_index, 80)

        # Used to remove the highlight when the row is selected
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        # Used to highlight the item on inside the table
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)

        # Used to set focus on the item only when it is clicked
        self.tableWidget.setFocusPolicy(Qt.ClickFocus)

    # Sort the employees by using sorting box
    def sort_employees(self, index):
        if index == 0:  # Sort by ID
            self.employees_list.sort(key=lambda x: x["id"])
        elif index == 1:  # Sort by Name
            self.employees_list.sort(key=lambda x: x['name'])
        elif index == 2:  # Sort by Salary: High to Low
            self.employees_list.sort(key=lambda x: x['salary'], reverse=True)
        elif index == 3:  # Sort by Salary: Low to High
            self.employees_list.sort(key=lambda x: x['salary'])

        # Used to update the displayed employees
        self.display_employees()

    # Update the displayed employees
    def display_employees(self):
        # print("display_employees() is called")
        # print(self.employees_list)

        # Used to check if employee list is empty or not
        if not self.employees_list:
            self.tableWidget.hideRow(0)
            self.tableWidget.clearContents()
            self.tableWidget.horizontalHeader().hideSection(self.delete_col_index)
            self.tableWidget.horizontalHeader().hideSection(self.edit_col_index)
            self.noDataLabel.show()
        else:
            self.tableWidget.showRow(0)
            self.tableWidget.horizontalHeader().showSection(self.delete_col_index)
            self.tableWidget.horizontalHeader().showSection(self.edit_col_index)
            self.noDataLabel.hide()

            row = 0
            self.tableWidget.setRowCount(len(self.employees_list))

            # Used to iterate over the employees and display them
            for employee in self.employees_list:
                id_item = QtWidgets.QTableWidgetItem(str(employee["id"]))
                id_item.setToolTip(str(employee["id"]))
                self.tableWidget.setItem(row, 0,id_item)

                name_item = QtWidgets.QTableWidgetItem(str(employee["name"]))
                name_item.setToolTip(str(employee["name"]))
                self.tableWidget.setItem(row, 1, name_item)

                position_item = QtWidgets.QTableWidgetItem(str(employee["position"]))
                position_item.setToolTip(str(employee["position"]))
                self.tableWidget.setItem(row, 2, position_item)

                salary_converted = self.format_salary(employee["salary"])
                salary_item = QtWidgets.QTableWidgetItem(salary_converted)
                salary_item.setToolTip(salary_converted)
                self.tableWidget.setItem(row, 3, salary_item)

                country_item = QtWidgets.QTableWidgetItem(
                    str(employee["country"]))
                country_item.setToolTip(str(employee["country"]))
                self.tableWidget.setItem(row, 4, country_item)

                age_item = QtWidgets.QTableWidgetItem(
                    str(employee["age"]))
                age_item.setToolTip(str(employee["age"]))
                self.tableWidget.setItem(row, 5, age_item)

                # Create a fix/delete buttons
                edit_button = EditButton(self.tableWidget,
                                             self.display_employees,
                                             self.employees_list, row, employee)

                delete_button = DeleteButton(self.tableWidget, self.display_employees,
                                             self.employees_list, row, employee)

                # Passing the employee["id"] argument to the remove_employee method
                # when the button is clicked, using a lambda function as a wrapper.
                delete_button.del_button.clicked.connect(
                    lambda _, employee_id=employee["id"]:
                    delete_button.confirm_deletion(employee_id))

                edit_button.edit_button.clicked.connect(
                    lambda _, employee_id=employee["id"]:
                    self.switch_dialog_to_update_emp(employee_id)
                    )

                row += 1

    def import__csv(self):
        print("import__csv is called")
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fileName:
            try:
                self.employees_list = []
                with open(fileName, 'r') as f:
                    csvReader = csv.DictReader(f)
                    for row in csvReader:
                        row["id"] = int(row["id"])
                        row["salary"] = int(row["salary"])
                        row["age"] = int(row["age"])
                        self.employees_list.append(row)
            except Exception as e:
                QMessageBox.warning(self, 'Error',
                                    'Failed to Import The File: ' + fileName)

        self.display_employees()

    def download_csv(self):
        # Open a save file dialog and get the chosen file path and name
        filename, _ = QFileDialog.getSaveFileName(self, "Save CSV", "",
                                                  "CSV Files (*.csv)")

        # Used to check if a file name was selected (cancel was not clicked)
        if filename != '':
            # If the file does not end in .csv, append .csv
            if not filename.endswith('.csv'):
                filename += '.csv'

            # Column names of the data
            fields = ["id", "name", "position", "salary", "country", "age"]

            # Used to write to the CSV file
            with open(filename, mode='w', newline='') as csvfile:
                # Creating a CSV writer object
                csvwriter = csv.writer(csvfile)

                # Used to write the column headers
                csvwriter.writerow(fields)

                # Used to write the data rows
                for row in self.employees_list:
                    csvwriter.writerow([row["id"], row["name"], row["position"], row["salary"], row["country"], row["age"]])

            self.show_success_alert(filename)

    # An alert pops up to confirm that the file is saved successfully
    def show_success_alert(self, filename):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"CSV file has been saved to: {filename}")
        msg.setWindowTitle("SUCCESS")
        msg.exec_()

    def format_salary(self, salary):
        return "{:,.0f}$".format(salary)

    def mousePressEvent(self, event):
        # If there is no item at the clicked position, clear the selection
        self.tableWidget.clearSelection()
        # Call the superclass implementation to handle the event
        super().mousePressEvent(event)
