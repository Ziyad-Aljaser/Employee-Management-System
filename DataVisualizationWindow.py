from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator

from DataDialog import DataDialog

class DataVisualizationWindow(QDialog):
    def __init__(self, widget, emp_list):
        print("DataVisualizationWindow Class is called")
        super(DataVisualizationWindow, self).__init__()

        self.widget = widget
        self.emp_list = emp_list

        loadUi("DataVisualizationGUI.ui", self)

        self.CountryRepButton.clicked.connect(self.show_chart)
        self.SalaryDisButton.clicked.connect(self.show_chart)
        self.AgeSalButton.clicked.connect(self.show_chart)

        self.GoBackButton.clicked.connect(self.switch_dialog)

    def show_chart(self):
        self.chart_dialog = DataDialog(self.emp_list)
        self.chart_dialog.show()

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
