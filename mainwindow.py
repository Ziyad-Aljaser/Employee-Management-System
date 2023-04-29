import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView
from AddEmployeeDashboard import AddEmployeeDashboard

class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()
        loadUi("EmployeesGUI.ui", self)
        self.employees_test = []
        self.load_data()

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.go_to_add_new_employee)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

    def go_to_add_new_employee(self):
        add_new_employee = AddEmployeeDashboard()
        widget.addWidget(add_new_employee)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def load_data(self):
        # Fake Data
        self.employees = [
            {"id": 9000, "name": "EmploeeyZ", "position": "CEO", "salary": 50000},
            {"id": 1001, "name": "EmploeeyB", "position": "CFO", "salary": 30000},
            {"id": 1002, "name": "EmploeeyC", "position": "CFO", "salary": 20000},
            {"id": 1003, "name": "EmploeeyD", "position": "CFO", "salary": 10000},
            {"id": 1004, "name": "EmploeeyE", "position": "CFO", "salary": 1000},
            {"id": 1005, "name": "EmploeeyF", "position": "CFO", "salary": 300},
            {"id": 1006, "name": "EmploeeyG", "position": "CFO", "salary": 3000},
            {"id": 1007, "name": "EmploeeyH", "position": "CFO", "salary": 400},
            {"id": 1008, "name": "EmploeeyJ", "position": "CFO", "salary": 6000},
            {"id": 1009, "name": "EmploeeyK", "position": "CFO", "salary": 7000},
            {"id": 1010, "name": "EmploeeyL", "position": "CFO", "salary": 9000},
        ]
        self.display_employees()

    def sort_employees(self, index):
        if index == 0:  # Sort by ID
            self.employees.sort(key=lambda x: x["id"])
        elif index == 1:  # Sort by Name
            print(len(self.employees))
            self.employees.sort(key=lambda x: x['name'])
            print(len(self.employees))
        elif index == 2:  # Sort by Salary: High to Low
            self.employees.sort(key=lambda x: x['salary'], reverse=True)
        elif index == 3:  # Sort by Salary: Low to High
            self.employees.sort(key=lambda x: x['salary'])

        # Used to update the displayed employees
        self.display_employees()

    def display_employees(self):
        row = 0
        self.tableWidget.setRowCount(len(self.employees))
        for employee in self.employees:
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
widget.setFixedHeight(831)
widget.setFixedWidth(1361)
widget.show()
try:
    sys.exit(app.exec_())
finally:
    print("Exiting")
