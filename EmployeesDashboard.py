from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QHeaderView,\
     QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import QCoreApplication
from DeleteButton import DeleteButton

class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setFixedHeight(833)
        self.widget.setFixedWidth(1342)

        loadUi("EmployeesGUI.ui", self)

        # Used to stretch the buttons
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Used to design the delete_button width
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.tableWidget.columnCount() - 1, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().resizeSection(
            self.tableWidget.columnCount() - 1, 80)

        # self.tableWidget.verticalHeader().setVisible(False)

        # Used to remove the highlight when the row is selected
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.employees_list = []

        # Fake Data
        self.employees_list = [{"id": 1000, "name": "Ziyad", "position": "CEO", "salary": 50000},
                                {"id": 1001, "name": "Fahad", "position": "CFO", "salary": 5000},
                                {"id": 1002, "name": "Ahmed", "position": "HR", "salary": 500}]
        self.display_employees()

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog)

        # Used to connect sorting box to sort by the selected option
        self.sortComboBox.currentIndexChanged.connect(self.sort_employees)

        self.noDataLabel.hide()

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
        if not self.employees_list:
            self.tableWidget.clearContents()
            self.noDataLabel.show()
        else:
            self.noDataLabel.hide()
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

                # Create a delete button class
                delete_button = DeleteButton(self.tableWidget, self.display_employees,
                                             self.employees_list, row, employee)

                # Passing the employee["id"] argument to the remove_employee method
                # when the button is clicked, using a lambda function as a wrapper.
                delete_button.del_button.clicked.connect(lambda _, employee_id=employee["id"]:
                                              delete_button.confirm_deletion(employee_id))

                row += 1
