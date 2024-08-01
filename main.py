from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QVBoxLayout,
                             QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog)
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        search_action = QAction("Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)


        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "name", "course", "mobile"))
        self.setCentralWidget(self.table)

    def load_Data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM Students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
        pass

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

class SearchDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        pass

app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
age_calculator.load_Data()
sys.exit(app.exec())
