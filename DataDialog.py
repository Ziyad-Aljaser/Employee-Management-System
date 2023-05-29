from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import FuncFormatter, StrMethodFormatter, MaxNLocator

import pandas as pd
import matplotlib.pyplot as plt

class DataDialog(QDialog):
    def __init__(self, employees_list, parent=None):
        super(DataDialog, self).__init__(parent)
        self.employees_list = employees_list

        # Set up the figure and canvas for plotting
        self.figure = Figure(figsize=(7, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        # Convert the employee data to a DataFrame for easier plotting
        data = pd.DataFrame(self.employees_list)

        # Call the plotting function
        self.salary_distribution_plot(data)

    def country_representation_plot(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        data['country'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_title('Country Representation Among Employees')
        ax.set_ylabel('')  # Used to remove the y-axis label for a pie chart

        self.canvas.draw()

    def age_vs_salary_plot(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.scatter(data['age'], data['salary'])
        ax.set_title('Age vs Salary')

        # Used a custom function to format x and y-axis numbers
        age_formatter = FuncFormatter(lambda x, pos: '{:,.0f}'.format(x))
        salary_formatter = StrMethodFormatter('{x:,.0f}$')

        # Used to apply formatter to x-axis and y-axis
        ax.xaxis.set_major_formatter(age_formatter)
        ax.yaxis.set_major_formatter(salary_formatter)

        ax.set_xlabel('Age')
        ax.set_ylabel('Salary')

        self.canvas.draw()

    def salary_distribution_plot(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.hist(data['salary'], bins=10, color='skyblue', edgecolor='black')

        ax.set_title('Salary Distribution Among Employees')
        ax.set_xlabel('Salary')
        ax.set_ylabel('Frequency')

        # Used to format the y-axis
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        # Used to format the x-axis
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}$'))

        # Calculate average salary
        avg_salary = data['salary'].mean()

        # Add text annotation for average salary
        ax.text(0.02, 0.95, 'Avg Salary: {:,.0f}$'.format(avg_salary),
                transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        self.canvas.draw()

