import socket
import os


def server_program():
    host = socket.gethostname()
    port = 4376

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)#c or s ki amount
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(2408).decode()
        print(data)
        if not data:
           print("No data recieved")
           #break
        #print("Connection Established to " + str(data))
        data = input(' -> ')
        if data == 'exit':
            print("exiting")
            conn.send(data.encode())
            break
        conn.send(str(data).encode('UTF-8'))

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()