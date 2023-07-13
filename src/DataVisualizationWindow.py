from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

from DataDialog import DataDialog


class DataVisualizationWindow(QDialog):
    def __init__(self, widget, emp_list):
        super(DataVisualizationWindow, self).__init__()

        self.widget = widget
        self.emp_list = emp_list

        loadUi("DataVisualizationGUI.ui", self)

        self.CountryRepButton.clicked.connect(self.show_country_rep)
        self.SalaryDisButton.clicked.connect(self.show_salary_dis)
        self.AgeSalButton.clicked.connect(self.show_age_sal)

        self.GoBackButton.clicked.connect(self.switch_dialog)

    def show_country_rep(self):
        self.chart_dialog = DataDialog(self.emp_list, "country_rep")
        self.chart_dialog.show()

    def show_salary_dis(self):
        self.chart_dialog = DataDialog(self.emp_list, "salary_dis")
        self.chart_dialog.show()

    def show_age_sal(self):
        self.chart_dialog = DataDialog(self.emp_list, "age_sal")
        self.chart_dialog.show()

    def switch_dialog(self):
        self.widget.setCurrentIndex(0)
