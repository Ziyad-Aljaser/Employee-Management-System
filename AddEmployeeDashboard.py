from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView

class AddEmployeeDashboard(QDialog):
    def __init__(self):
        super(AddEmployeeDashboard, self).__init__()
        loadUi("AddEmployeesGUI.ui", self)