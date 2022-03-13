import socket
import threading

IP = 'localhost'
PORT = 1234
ADDRESS = (IP, PORT)


def server(waiting_view_controller, mainView):
    print('starting server')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS)
    server_socket.listen(4)
    print('server started')
    print('accepting...')
    while True:
        waiting_view_controller.set_connected_players(0)
        connection, client_address = server_socket.accept()
        print(connection, client_address)


def start_server(waiting_view_controller, mainView):
    print('init thread')
    thread = init_thread(waiting_view_controller, mainView)
    print('starting thread')
    thread.start()
    print('thread started')


def init_thread(waiting_view_controller, mainView):
    return threading.Thread(target=server, daemon=True, args=(waiting_view_controller, mainView))
