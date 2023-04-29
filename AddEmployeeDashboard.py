import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView


class AddEmployeeDashboard(QDialog):
    def __init__(self):
        super(AddEmployeeDashboard, self).__init__()
        loadUi("AddEmployeesGUI.ui", self)
        self.EmpButton.clicked.connect(self.new_employee)


    def new_employee(self):
        self.name = self.EmpNameText.text()
        self.position = self.EmpPositionText.text()
        self.salary = self.EmpSalaryText.text()
        print(self.name, self.position, self.salary)