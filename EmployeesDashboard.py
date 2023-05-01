import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView

class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setFixedHeight(833)
        self.widget.setFixedWidth(1342)


        loadUi("EmployeesGUI.ui", self)

        self.employees_list = []

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

    # Used to switch the window to the AddEmployeeDashboard class
    def switch_dialog(self):
        self.widget.setCurrentIndex(1)

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

    def display_employees(self):
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
            row += 1
