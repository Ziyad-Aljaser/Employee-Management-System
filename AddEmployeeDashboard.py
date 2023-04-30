from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView

class AddEmployeeDashboard(QDialog):

    def __init__(self, widget, func, emp_list):
        super(AddEmployeeDashboard, self).__init__()
        self.widget = widget
        self.id = 1000
        self.salary = None
        self.position = None
        self.name = None
        loadUi("AddEmployeesGUI.ui", self)
        self.display_employees_func = func
        self.emp_list = emp_list

        self.EmpButton.clicked.connect(self.new_employee)

        self.GoBackButton.clicked.connect(self.switch_dialog)

    def new_employee(self):
        self.id += 1
        self.name = self.EmpNameText.text()
        self.position = self.EmpPositionText.text()
        self.salary = int(self.EmpSalaryText.text())
        self.emp_list.append(self.get_employee())

        self.display_employees_func()

    def get_employee(self):
        return {"id": self.id, "name": self.name, "position": self.position,
                "salary": self.salary}

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)