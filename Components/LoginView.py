from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

from Constants import CARDS_PATH


class LoginView(QWidget):
    def __init__(self):
        super().__init__()

        self.foto = None
        self.client_button = None
        self.server_button = None
        self.main_container = None
        self.create_main_container()
        self.create_buttons()

    def create_main_container(self):
        self.main_container = QVBoxLayout()
        self.main_container.setAlignment(Qt.AlignVCenter)
        self.setLayout(self.main_container)

    def create_buttons(self):
        self.server_button = QPushButton("Server")
        self.client_button = QPushButton("Client")
        self.main_container.addWidget(self.server_button)
        self.main_container.addWidget(self.client_button)
