import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from EmployeesDashboard import EmployeesDashboard
from AddEmployeeWindow import AddEmployeeWindow

class Main:
    # main window
    app = QApplication(sys.argv)
    emps_window = EmployeesDashboard()
    emps_window.widget.addWidget(emps_window)

    # New window for adding new employee
    add_employee_window = AddEmployeeWindow(emps_window.widget,
                                            emps_window.display_employees,
                                            emps_window.employees_list)
    emps_window.widget.addWidget(add_employee_window)

    emps_window.widget.show()
    try:
        sys.exit(app.exec_())
    finally:
        print("Exiting")
