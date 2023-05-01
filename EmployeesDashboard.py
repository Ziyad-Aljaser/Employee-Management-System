import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QAbstractItemView


class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setFixedHeight(833)
        self.widget.setFixedWidth(1342)
        self.second_window = None

        loadUi("EmployeesGUI.ui", self)

        self.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                 QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.employees_list = []

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

    # Used to switch the window to the AddEmployeeDashboard class
    def switch_dialog(self):
        print("switch_dialog() is called")
        self.widget.setCurrentIndex(1)

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
        print("display_employees() is called")
        print(self.employees_list)
        row = 0
        self.tableWidget.setRowCount(len(self.employees_list))
        for employee in self.employees_list:
            self.tableWidget.setItem(row, 0,
                                     QtWidgets.QTableWidgetItem(
                                         str(employee["id"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(employee["name"])))
            self.tableWidget.setItem(row, 2,
                                     QtWidgets.QTableWidgetItem(
                                         employee["position"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(
                str(employee["salary"])))

            # Create a new button for each row
            delete_button = QPushButton("X")
            # Passing the employee["id"] argument to the remove_employee method
            # when the button is clicked, using a lambda function as a wrapper.
            delete_button.clicked.connect(lambda: self.remove_employee(employee["id"]))
            self.tableWidget.setCellWidget(row, 4, delete_button)

            row += 1

    # Remove the employee with the given ID from the employees_list
    def remove_employee(self, employee_id):
        print("remove_employee() is called")
        for employee in self.employees_list:
            if employee["id"] == employee_id:
                self.employees_list.remove(employee)
                break
        self.display_employees()