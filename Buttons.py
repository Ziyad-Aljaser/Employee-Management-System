from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon


class EditButton(QDialog):
    def __init__(self, widget, func, emp_list, row, emp):
        super(EditButton, self).__init__()
        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list
        self.row = row
        self.emp = emp

        # Create a new button for each row with specific style
        self.edit_button = QPushButton()
        self.edit_button.setIcon(QIcon('pics/Edit_Icon.png'))
        self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                margin: 5px;
                margin-right: 25px; margin-left: 25px;
                border-radius: 5px;
            }
            QPushButton::hover {
                background-color: #60746E;
            }
        """)

        self.widget.setCellWidget(self.row, 6, self.edit_button)


class DeleteButton(QDialog):
    def __init__(self, widget, func, emp_list, row, emp):
        super(DeleteButton, self).__init__()
        self.widget = widget
        self.display_employees_func = func
        self.emp_list = emp_list
        self.row = row
        self.emp = emp

        # Create a new button for each row with specific style
        self.del_button = QPushButton("X")
        self.del_button.setStyleSheet("""
            QPushButton {
                background-color: red; color: white;
                font: 9pt 'Segoe UI Black'; margin: 7px;
                margin-right: 25px; margin-left: 25px;
                border: 3px solid; border-radius: 5px;
            }
            QPushButton::hover {
                background-color: #9a1300;
            }
        """)

        self.widget.setCellWidget(self.row, 7, self.del_button)

    # Remove the employee with the given ID from the emp_list
    def remove_employee(self, employee_id):
        print("remove_employee() is called")
        for employee in self.emp_list:
            if employee["id"] == employee_id:
                print(employee)
                self.emp_list.remove(employee)
                break
        self.display_employees_func()

    # An alert pops up to confirm the deletion of the employee
    def confirm_deletion(self, employee_id):
        confirmation_box = QMessageBox()
        confirmation_box.setIcon(QMessageBox.Warning)
        confirmation_box.setWindowTitle("Confirm Deletion")
        confirmation_box.setText(
            "Are you sure you want to delete this employee?")
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirmation_box.exec()

        if result == QMessageBox.Yes:
            self.remove_employee(employee_id)
