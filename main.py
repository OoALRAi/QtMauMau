from PyQt5.QtWidgets import QApplication
import sys

from Components.MainWindow import MainWindow


app = QApplication(sys.argv)
window = MainWindow()
app.exec()



