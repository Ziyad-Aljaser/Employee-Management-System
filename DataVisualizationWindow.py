from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, QDate

from DataDialog import DataDialog

class DataVisualizationWindow(QDialog):

    def __init__(self):
        print("DataVisualizationWindow class is called")
        super(DataVisualizationWindow, self).__init__()
        loadUi("DataVisualizationGUI.ui", self)

        self.CountryRepButton.clicked.connect(self.show_chart)

    def show_chart(self):
        employees_list = [
            {"id": 1000, "name": "Ziyad", "position": "CEO", "salary": 50000,
             "country": "Saudi Arabia", "age": 23},
            {"id": 1001, "name": "Fahad", "position": "CFO", "salary": 5000,
             "country": "USA", "age": 35},
            {"id": 1002, "name": "Ahmed", "position": "HR", "salary": 500,
             "country": "UK", "age": 40},
            # Add more employees...
        ]
        self.chart_dialog = DataDialog(employees_list)
        self.chart_dialog.exec_()

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
