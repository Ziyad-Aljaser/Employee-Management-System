from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd


class DataDashboard(QWidget):
    def __init__(self, parent=None):
        super(DataDashboard, self).__init__(parent)

        self.figure = Figure(figsize=(7, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

    def country_representation_plot(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        data['country'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')

        ax.set_title('Country Representation Among Employees')
        ax.set_ylabel('')  # We remove the y-axis label for a pie chart

        self.canvas.draw()



class DataDialog(QDialog):
    def __init__(self, employees_list, parent=None):
        super(DataDialog, self).__init__(parent)
        self.employees_list = employees_list

        self.dashboard = DataDashboard(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.dashboard)

        data = pd.DataFrame(self.employees_list)
        self.dashboard.country_representation_plot(data)
