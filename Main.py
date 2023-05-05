import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from EmployeesDashboard import EmployeesDashboard
from AddEmployeeWindow import AddEmployeeWindow


class Main:
    # main window
    app = QApplication(sys.argv)
    employees_window = EmployeesDashboard()
    employees_window.widget.addWidget(employees_window)

    # Adding new window
    add_employee_window = AddEmployeeWindow(employees_window.widget,
                                               employees_window.display_employees,
                                               employees_window.employees_list)
    employees_window.widget.addWidget(add_employee_window)

    employees_window.widget.show()
    try:
        sys.exit(app.exec_())
    finally:
        print("Exiting")
