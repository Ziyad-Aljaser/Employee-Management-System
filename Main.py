import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from EmployeesDashboard import EmployeesDashboard
from AddEmployeeDashboard import AddEmployeeDashboard

class Main:
    # main
    app = QApplication(sys.argv)
    mainWindow = EmployeesDashboard()
    mainWindow.widget.addWidget(mainWindow)
    second_dialog = AddEmployeeDashboard(mainWindow.widget, mainWindow.display_employees,
                                              mainWindow.employees_list)
    mainWindow.widget.addWidget(second_dialog)
    mainWindow.widget.show()
    try:
        sys.exit(app.exec_())
    finally:
        print("Exiting")