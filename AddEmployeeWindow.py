from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from Employee import Employee


class AddEmployeeWindow(QDialog):

    def __init__(self, widget, func, emp_list):
        super(AddEmployeeWindow, self).__init__()

        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list
        self.id = 1003

        loadUi("AddEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.new_employee)
        self.GoBackButton.clicked.connect(self.switch_dialog)

    def new_employee(self):
        print("new_employee() is called")

        if(self.check_emp()):
            new_emp = Employee(self.id)

            new_emp.name = self.EmpNameText.text().strip()
            new_emp.position = self.EmpPositionText.text().strip()
            new_emp.salary = int(self.EmpSalaryText.text())

            self.emp_list.append(new_emp.get_employee())
            self.id += 1

            # Clear the QLineEdit widgets
            self.EmpNameText.clear()
            self.EmpPositionText.clear()
            self.EmpSalaryText.clear()

            self.show_success_alert(new_emp.name)

            # Update the employees dashboard
            self.display_employees_func()
        else:
            self.show_error_alert()

    # Used to insure all the data entered is pure
    def check_emp(self):
        name = self.EmpNameText.text()
        position = self.EmpPositionText.text()
        salary = self.EmpSalaryText.text()
        if (name.replace(' ', '').isalpha() and position.replace(' ', '').isalpha()
                and salary):
            try:
                if (int(salary) > 0):
                    return True
            except:
                return False
        return False

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