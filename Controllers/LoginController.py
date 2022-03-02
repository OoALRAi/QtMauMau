from Components.LoginView import LoginView


class LoginController:
    def __init__(self, view: LoginView, mainWindow):
        self.mainWindow = mainWindow
        self.view = view
        self.init_actions()

    def init_actions(self):
        self.view.server_button.clicked.connect(self.server_button_click)
        self.view.client_button.clicked.connect(self.client_button_click)

    def client_button_click(self):
        print("client button click")
        self.mainWindow.show_client_init_view()

    def server_button_click(self):
        print("server button click")
        self.mainWindow.show_server_init_view()
