from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

from Constants import IP_ADDRESS


class ServerInitView(QWidget):
    def __init__(self):
        super().__init__()
        self.start_server = None
        self.port = None
        self.ip_address = None
        self.main_container = None
        self.create_main_container()
        self.create_content()

    def create_main_container(self):
        self.main_container = QVBoxLayout()
        self.main_container.setAlignment(Qt.AlignVCenter)
        self.setLayout(self.main_container)

    def create_content(self):
        self.ip_address = QLineEdit()
        self.ip_address.setPlaceholderText("IP Address")
        self.main_container.addWidget(self.ip_address)
        self.port = QLineEdit()
        self.port.setPlaceholderText("Port")
        self.main_container.addWidget(self.port)
        self.start_server = QPushButton("Start server")
        self.main_container.addWidget(self.start_server)
