import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QHeaderView


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("EmployeesGUI.ui", self)

        self.loadData()

    def loadData(self):
        # Fake Data
        people = [
            {"id": 1000, "name": "EmploeeyA", "position": "CEO", "salary": 50000},
            {"id": 1001, "name": "EmploeeyB", "position": "CFO", "salary": 30000},
            {"id": 1002, "name": "EmploeeyC", "position": "CFO", "salary": 20000},
            {"id": 1003, "name": "EmploeeyD", "position": "CFO", "salary": 10000},
            {"id": 1004, "name": "EmploeeyE", "position": "CFO", "salary": 1000},
            {"id": 1005, "name": "EmploeeyF", "position": "CFO", "salary": 300},
            {"id": 1006, "name": "EmploeeyG", "position": "CFO", "salary": 3000},
            {"id": 1007, "name": "EmploeeyH", "position": "CFO", "salary": 400},
            {"id": 1008, "name": "EmploeeyJ", "position": "CFO", "salary": 6000},
            {"id": 1009, "name": "EmploeeyK", "position": "CFO", "salary": 7000},
            {"id": 1010, "name": "EmploeeyL", "position": "CFO", "salary": 9000},
        ]
        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0,
                                     QtWidgets.QTableWidgetItem(str(person["id"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(person["name"])))
            self.tableWidget.setItem(row, 2,
                                     QtWidgets.QTableWidgetItem(person["position"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(
                str(person["salary"])))
            row += 1


# main
app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(831)
widget.setFixedWidth(1361)
widget.show()
try:
    sys.exit(app.exec_())
finally:
    print("Exiting")
