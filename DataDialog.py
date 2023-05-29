from PyQt5.QtWidgets import QVBoxLayout, QDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import FuncFormatter, StrMethodFormatter, MaxNLocator

import pandas as pd


class DataDialog(QDialog):
    def __init__(self, employees_list, plot_type, parent=None):
        super(DataDialog, self).__init__(parent)
        print("DataDialog class is called")

        self.employees_list = employees_list
        self.plot_type = plot_type

        # Used to set up the figure and canvas for plotting
        self.figure = Figure(figsize=(9, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        # Convert the employee data to a DataFrame for easier plotting
        data = pd.DataFrame(self.employees_list)

        if self.plot_type == "country_rep":
            self.country_representation_plot(data)
        elif self.plot_type == "salary_dis":
            self.salary_distribution_plot(data)
        elif self.plot_type == "age_sal":
            self.age_vs_salary_plot(data)

    def country_representation_plot(self, data):
        print("country_representation_plot() is called")
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        data['country'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_title('Country Representation Among Employees')
        ax.set_ylabel('')  # Used to remove the y-axis label for a pie chart

        self.canvas.draw()

    def salary_distribution_plot(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.hist(data['salary'], bins=10, color='skyblue', edgecolor='black')

        ax.set_title('Salary Distribution Among Employees')
        ax.set_xlabel('Salary')
        ax.set_ylabel('Employees')

        # Used to format the y-axis
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        # Used to format the x-axis
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}$'))

        # Calculate average salary
        avg_salary = data['salary'].mean()

        # Used to add text annotation for average salary
        ax.text(0.02, 0.95, 'Avg Salary: {:,.0f}$'.format(avg_salary),
                transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

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