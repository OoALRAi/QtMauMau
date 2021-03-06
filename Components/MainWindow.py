from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QStackedWidget

from Controllers.WaitingViewController import WaitingViewController
from Server.Server import Server
from Components.LoginView import LoginView
from Components.ServerInitView import ServerInitView
from Constants import *
from Controllers.ClilentInitController import ClientInitController
from Controllers.LoginController import LoginController
from Controllers.ServerInitController import ServerInitController


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.waiting_view = None
        self.waiting_view_controller = None
        self.thread_pool = None
        self.server = None
        self.login_view = None
        self.login_view_controller = None
        self.server_view = None
        self.server_view_controller = None
        self.client_view = None
        self.client_view_controller = None
        self.resize(WIDTH, HEIGHT)
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self.init_stack_view()
        self.setWindowTitle(GAME_TITLE)
        self.show()

    def init_stack_view(self):
        self.login_view = LoginView()
        self.login_view_controller = LoginController(self.login_view, self)
        self.addWidget(self.login_view)

    def show_server_init_view(self):
        print("show server view")
        if not self.server_view:
            self.server_view = ServerInitView()
            self.server_view_controller = ServerInitController(self.server_view, self)
            self.addWidget(self.server_view)
        self.setCurrentWidget(self.server_view)

    def show_client_init_view(self):
        print("show client view")
        if not self.client_view:
            self.client_view = uic.loadUi(f'{COMPONENTS_UI_PATH}ClientView.ui')
            self.client_view_controller = ClientInitController(self.client_view)
            self.addWidget(self.client_view)
        self.setCurrentWidget(self.client_view)

    def show_waiting_view(self):
        if not self.waiting_view:
            self.waiting_view = uic.loadUi(f'{COMPONENTS_UI_PATH}WaitingView.ui')
            self.waiting_view_controller = WaitingViewController(self.waiting_view, self)
            self.waiting_view_controller.set_ip(IP)
            self.waiting_view_controller.set_port(PORT)
            self.addWidget(self.waiting_view)
        self.setCurrentWidget(self.waiting_view)

    def init_server(self, port=PORT, ip=IP):
        print('init server')

