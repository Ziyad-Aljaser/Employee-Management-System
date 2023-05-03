from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Employee import Employee

class AddEmployeeDashboard(QDialog):

    def __init__(self, widget, func, emp_list):
        super(AddEmployeeDashboard, self).__init__()

        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list
        self.id = 1003

        loadUi("AddEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.new_employee)
        self.GoBackButton.clicked.connect(self.switch_dialog)

    def new_employee(self):
        print("new_employee() is called")
        self.new_employee = Employee(self.id)

        self.new_employee.name = self.EmpNameText.text()
        self.new_employee.position = self.EmpPositionText.text()
        self.new_employee.salary = int(self.EmpSalaryText.text())

        self.emp_list.append(self.new_employee.get_employee())
        self.id += 1

        # Clear the QLineEdit widgets
        self.EmpNameText.clear()
        self.EmpPositionText.clear()
        self.EmpSalaryText.clear()

        # Update the employees dashboard
        self.display_employees_func()


    def switch_dialog(self):
        self.widget.setCurrentIndex(0)