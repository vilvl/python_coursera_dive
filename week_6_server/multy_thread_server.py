import socket
import threading

pair = ('127.0.0.1', 2222)


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data or data.decode('utf8') == 'close':
                break
            conn.sendall(data)


def main():
    with socket.socket() as sock:
        sock.bind(pair)
        sock.listen()
        while True:
            conn, addr = sock.accept()
            th = threading.Thread(target=process_request, args=(conn, addr))
            th.start()


def client_send(querry):
    sock = socket.create_connection(pair)
    sock.sendall(querry.encode('utf8'))
    answer = sock.recv(1024)
    print(answer.decode('utf8'))


if __name__ == '__main__':
    main()
