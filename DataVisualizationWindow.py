from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, QDate


class DataVisualizationWindow(QDialog):

    def __init__(self):
        print("DataVisualizationWindow class is called")
        super(DataVisualizationWindow, self).__init__()
        loadUi("DataVisualizationGUI.ui", self)

        # self.BackButton.clicked.connect(self.switch_dialog)

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
