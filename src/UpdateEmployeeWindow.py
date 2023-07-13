from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, QDate

from datetime import date


class UpdateEmployeeWindow(QDialog):

    def __init__(self, widget, func, emp_list):
        super(UpdateEmployeeWindow, self).__init__()
        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list

        loadUi("UpdateEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.update_employee)
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

        self.employee_to_modify = None

    # Used to locate the chosen employee
    def find_current_emp(self, employee_id):
        for employee in self.emp_list:
            if employee["id"] == employee_id:
                self.employee_to_modify = employee
                self.EmpNameText.setText(employee["name"])
                self.EmpPositionText.setText(employee["position"])
                self.EmpSalaryText.setText(str(employee["salary"]))
                self.EmpCountryText.setText(employee["country"])
                break

    # Used to update the chosen employee with the new data
    def update_employee(self):
        if self.check_emp():
            self.employee_to_modify["name"] = self.EmpNameText.text().strip()
            self.employee_to_modify["position"] = self.EmpPositionText.text().strip()
            self.employee_to_modify["salary"] = int(self.EmpSalaryText.text())
            self.employee_to_modify["country"] = self.EmpCountryText.text().strip()
            self.employee_to_modify["age"] = self.calculate_age(self.EmpAgeText.date())

            self.show_success_alert(self.employee_to_modify["name"])

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

        # Uesd to add all text data to this list
        fields = [name, position, salary, country]
        for field in fields:
            # Checks if the text is empty or contains only whitespace
            if not field.strip():
                return False

        if int(salary) < 0 and int(age) < 0:
            return False

        return True

    def calculate_age(self, qdate):
        birth_date = date(qdate.year(), qdate.month(), qdate.day())
        today = date.today()
        age = today.year - birth_date.year - (
                    (today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    # An alert pops up to confirm that the employee is added successfully
    def show_success_alert(self, update_emp):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(update_emp + " Updated Successfully")
        msg.setWindowTitle("Success")
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
