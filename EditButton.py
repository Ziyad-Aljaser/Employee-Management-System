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

        self.widget.setCellWidget(self.row, 4, self.edit_button)
