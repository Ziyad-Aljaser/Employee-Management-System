from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, QDate

from datetime import date
import random

from Employee import Employee


class AddEmployeeWindow(QDialog):

    def __init__(self, widget, func, emp_list):
        super(AddEmployeeWindow, self).__init__()

        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list
        self.id = self.generate_id()

        loadUi("AddEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.new_employee)
        self.GoBackButton.clicked.connect(self.switch_dialog)

        # Used to apply a regular expression to restrict the input to String
        regEx = QRegExp("[a-z A-Z]+")
        string_validator = QRegExpValidator(regEx)
        # Used to restrict the input to int values only
        int_validator = QIntValidator()

        # Apply the validators:
        self.EmpNameText.setValidator(string_validator)
        self.EmpPositionText.setValidator(string_validator)
        self.EmpSalaryText.setValidator(int_validator)
        self.EmpCountryText.setValidator(string_validator)

    def new_employee(self):

        if self.check_emp():
            new_emp = Employee(self.id)

            new_emp.name = self.EmpNameText.text().strip()
            new_emp.position = self.EmpPositionText.text().strip()
            new_emp.salary = int(self.EmpSalaryText.text())
            new_emp.country = self.EmpCountryText.text().strip()
            new_emp.age = self.calculate_age(self.EmpAgeText.date())

            self.emp_list.append(new_emp.get_employee())
            self.id += 1

            # Clear the QLineEdit widgets
            self.EmpNameText.clear()
            self.EmpPositionText.clear()
            self.EmpSalaryText.clear()
            self.EmpCountryText.clear()

            self.show_success_alert(new_emp.name)

            # Update the employees dashboard
            self.display_employees_func()
        else:
            self.show_error_alert()

    # Used to check if all fields have data and the salary is not negative
    def check_emp(self):
        name = self.EmpNameText.text()
        position = self.EmpPositionText.text()
        salary = self.EmpSalaryText.text()
        country = self.EmpCountryText.text()

        # Used to add all text data to this list
        fields = [name, position, salary, country]
        for field in fields:
            # Checks if the text is empty or contains only whitespace
            if not field.strip():
                return False

        if int(salary) < 0:
            return False

        return True

    def calculate_age(self, qdate):
        birth_date = date(qdate.year(), qdate.month(), qdate.day())
        today = date.today()
        age = today.year - birth_date.year - (
                    (today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def generate_id(self):
        while True:
            id = random.randint(100000, 999999)  # Generate a random 6-digit number
            if id not in self.emp_list:
                break
        return id

    # An alert pops up to confirm that the employee is added successfully
    def show_success_alert(self, new_emp):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(new_emp + " Added Successfully")
        msg.setWindowTitle("SUCCESS")
        msg.exec_()

    # An alert pops up to indicate that the data entered is invalid
    def show_error_alert(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Please Enter Valid Data")
        msg.setWindowTitle("ERROR")
        msg.exec_()

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
