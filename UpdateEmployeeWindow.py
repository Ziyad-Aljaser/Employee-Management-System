from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox


class UpdateEmployeeWindow(QDialog):

    def __init__(self, widget, func, emp_list):
        print("UpdateEmployeeWindow class is called")
        super(UpdateEmployeeWindow, self).__init__()
        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list

        loadUi("UpdateEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.update_employee)
        self.GoBackButton.clicked.connect(self.switch_dialog)

        self.employee_to_modify = None

    def find_current_emp(self, employee_id):
        print("find_current_emp() is called")
        for employee in self.emp_list:
            if employee["id"] == employee_id:
                self.employee_to_modify = employee
                self.EmpNameText.setText(employee["name"])
                self.EmpPositionText.setText(employee["position"])
                self.EmpSalaryText.setText(str(employee["salary"]))
                break

    def update_employee(self):
        print("update_employee() is called")
        self.employee_to_modify["name"] = self.EmpNameText.text().strip()
        self.employee_to_modify["position"] = self.EmpPositionText.text().strip()
        self.employee_to_modify["salary"] = int(self.EmpSalaryText.text())

        self.show_success_alert(self.employee_to_modify["name"])

        # Update the employees dashboard
        self.display_employees_func()

    # An alert pops up to confirm that the employee is added successfully
    def show_success_alert(self, update_emp):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(update_emp + " Updated Successfully")
        msg.setWindowTitle("Success")
        msg.exec_()


    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
