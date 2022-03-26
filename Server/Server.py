import socket
import threading
import Constants


class Server:

    def __init__(self, waiting_view_controller, playing_view_controller, mainView):
        self.server_socket = None
        self.clients = []
        self.is_running = False
        self.waiting_view_controller = waiting_view_controller
        self.playing_view_controller = playing_view_controller
        self.mainView = mainView
        self.init_server()
        self.thread = self.init_thread()

    def init_thread(self):
        return threading.Thread(target=self._start_thead, daemon=True)

    def init_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((Constants.IP, Constants.PORT))
        self.server_socket.listen(4)

    def _start_thead(self):
        while True:
            if len(self.clients) >= 4:
                self.is_running = True
                break
            self.waiting_view_controller.set_connected_players(len(self.clients))
            connection, client_address = self.server_socket.accept()
            self.clients.append((connection, client_address))
            print(connection, client_address)

    def start(self):
        self.thread.start()

    def _play(self):
        print("is playing")
