import socket


def start_server():
    print('starting server...')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    while True:
        connection, client_address = server_socket.accept()
        print(connection, client_address)
