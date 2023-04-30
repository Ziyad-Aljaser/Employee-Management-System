import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView
from AddEmployeeDashboard import AddEmployeeDashboard

class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()
        loadUi("EmployeesGUI.ui", self)

        self.second_dialog = None
        self.employees_list = []

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.go_to_add_new_employee)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

    def go_to_add_new_employee(self):
        # Used to ensure the AddEmployeeDashboard class is initialized only once
        if self.second_dialog is None:
            # Passing display_employees function to update the employees list every
            # time a new employee entered
            self.second_dialog = AddEmployeeDashboard(widget, self.display_employees, self.employees_list)
            widget.addWidget(self.second_dialog)
        widget.setCurrentIndex(1)

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
        print("test")
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


# main
app = QApplication(sys.argv)
mainWindow = EmployeesDashboard()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(833)
widget.setFixedWidth(1342)
widget.show()
try:
    sys.exit(app.exec_())
finally:
    print("Exiting")
