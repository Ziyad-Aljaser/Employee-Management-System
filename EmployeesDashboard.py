from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QHeaderView,\
     QTableWidgetItem, QAbstractItemView, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, Qt
import csv

from DeleteButton import DeleteButton
from EditButton import EditButton

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

        # Fake Data
        self.employees_list = [{"id": 10000000000, "name": "Ziyad", "position": "CEO", "salary": 50000, "country": "Saudi Arabia", "age": 23},
                                {"id": 1001, "name": "Fahad", "position": "CFO", "salary": 5000, "country": "Saudi Arabia", "age": 25},
                                {"id": 1002, "name": "Ahmed", "position": "HR", "salary": 500, "country": "Saudi Arabia", "age": 24}]
        self.display_employees()

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog_to_new_emp)

        self.dataVisualizationButton.clicked.connect(self.switch_dialog_to_data_visualization)

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
    def switch_dialog_to_data_visualization(self):
        print("switch_dialog_to_data_visualization() is called")
        if self.data_visualization_window is None:
            self.data_visualization_window = DataVisualizationWindow()
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
            fields = ["id", "name", "position", "salary"]

            # Used to write to the CSV file
            with open(filename, mode='w', newline='') as csvfile:
                # Creating a CSV writer object
                csvwriter = csv.writer(csvfile)

                # Used to write the column headers
                csvwriter.writerow(fields)

                # Used to write the data rows
                for row in self.employees_list:
                    csvwriter.writerow([row["id"], row["name"], row["position"], row["salary"]])

            self.show_success_alert(filename)

    def format_salary(self, salary):
        return "{:,.0f}$".format(salary)

    # An alert pops up to confirm that the file is saved successfully
    def show_success_alert(self, filename):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"CSV file has been saved to: {filename}")
        msg.setWindowTitle("SUCCESS")
        msg.exec_()

    def mousePressEvent(self, event):
        # If there is no item at the clicked position, clear the selection
        self.tableWidget.clearSelection()
        # Call the superclass implementation to handle the event
        super().mousePressEvent(event)

