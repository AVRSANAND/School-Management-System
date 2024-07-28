from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QVBoxLayout,
                             QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QMainWindow, QTableWidget)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "name", "course", "mobile"))
        self.setCentralWidget(self.table)


    def load_Data(self):
        self.table
        pass


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
sys.exit(app.exec())
