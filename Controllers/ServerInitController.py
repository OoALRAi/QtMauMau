from Components.ServerInitView import ServerInitView


class ServerInitController:
    def __init__(self, view: ServerInitView, mainWindow):
        self.view = view
        self.mainWindow = mainWindow
        self.init_actions()

    def init_actions(self):
        self.view.start_server.clicked.connect(self.start_server_action)

    def start_server_action(self):
        print("start server...")
        self.mainWindow.enter_game()
