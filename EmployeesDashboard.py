from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QHeaderView,\
     QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import QCoreApplication, Qt

from DeleteButton import DeleteButton
from EditButton import EditButton

from UpdateEmployeeWindow import UpdateEmployeeWindow

class EmployeesDashboard(QDialog):

    def __init__(self):
        super(EmployeesDashboard, self).__init__()

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setFixedHeight(833)
        self.widget.setFixedWidth(1342)
        self.update_employee_window = None

        loadUi("EmployeesGUI.ui", self)

        self.edit_table_widget()

        self.employees_list = []

        # Fake Data
        self.employees_list = [{"id": 1000, "name": "Ziyad", "position": "CEO", "salary": 50000},
                                {"id": 1001, "name": "Fahad", "position": "CFO", "salary": 5000},
                                {"id": 1002, "name": "Ahmed", "position": "HR", "salary": 500}]
        self.display_employees()

        # Used when the "Add Employee" button is clicked, and it opens a new window
        self.addEmployeeButton.clicked.connect(self.switch_dialog_to_new_emp)

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

        self.update_employee_window.find_current_emp(current_emp)
        self.widget.setCurrentIndex(2)

    def edit_table_widget(self):
        # Used to stretch the columns
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        # Used to locate the delete/edit button index
        self.delete_col_index = self.tableWidget.columnCount() - 1
        self.edit_col_index = self.tableWidget.columnCount() - 2

        # Used to design the delete/edit buttons width
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.delete_col_index, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.edit_col_index, QHeaderView.Fixed)

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

    def mousePressEvent(self, event):
        # If there is no item at the clicked position, clear the selection
        self.tableWidget.clearSelection()
        # Call the superclass implementation to handle the event
        super().mousePressEvent(event)

