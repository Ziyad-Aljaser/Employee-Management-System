import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView

class AddEmployeeDashboard(QDialog):

    def __init__(self, widget):
        super(AddEmployeeDashboard, self).__init__()
        self.widget = widget
        self.salary = None
        self.position = None
        self.name = None
        loadUi("AddEmployeesGUI.ui", self)

        self.EmpButton.clicked.connect(self.new_employee)

        self.GoBackButton.clicked.connect(self.switch_dialog)

    def new_employee(self):
        self.name = self.EmpNameText.text()
        self.position = self.EmpPositionText.text()
        self.salary = self.EmpSalaryText.text()

    def get_employee(self):
        return {"id": 0000, "name": self.name, "position": self.position,
                "salary": self.salary}

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)