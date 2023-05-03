from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView,\
    QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget,\
    QTableWidget, QTableWidgetItem, QHBoxLayout, QAbstractItemView, QMessageBox


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

            # Create a new button for each row with specific style
            delete_button = QPushButton("X")
            delete_button.setStyleSheet("""
                QPushButton {
                    background-color: red; color: white;
                    font: 9pt 'Segoe UI Black'; margin: 8px;
                    margin-right: 25px; margin-left: 25px;
                    border: 2.4px solid; border-radius: 5px;
                }
                QPushButton::hover {
                    background-color: #9a1300;
                }
            """)

            # Passing the employee["id"] argument to the remove_employee method
            # when the button is clicked, using a lambda function as a wrapper.
            delete_button.clicked.connect(lambda _, employee_id=employee["id"]:
                                          self.confirm_deletion(employee_id))

            self.tableWidget.setCellWidget(row, 4, delete_button)

            row += 1

    # Remove the employee with the given ID from the employees_list
    def remove_employee(self, employee_id):
        print("remove_employee() is called")
        for employee in self.employees_list:
            if employee["id"] == employee_id:
                print(employee)
                self.employees_list.remove(employee)
                break
        self.display_employees()

    # An alert pops up to confirm the deletion of the employee
    def confirm_deletion(self, employee_id):
        confirmation_box = QMessageBox()
        confirmation_box.setIcon(QMessageBox.Warning)
        confirmation_box.setWindowTitle("Confirm Deletion")
        confirmation_box.setText("Are you sure you want to delete this employee?")
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirmation_box.exec()

        if result == QMessageBox.Yes:
            self.remove_employee(employee_id)