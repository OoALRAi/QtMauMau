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
        port = self.view.port.text()
        ip = self.view.ip_address.text()
        if not port or not ip:
            self.mainWindow.init_server()
        else:
            self.mainWindow.init_server(port=int(port), ip=ip)

