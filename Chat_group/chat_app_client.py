import socket
import threading

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send_massage(client_socket):
    while True:
        your_mass=input("Massage= ")
        if your_mass != "":
            client_socket.sendall(your_mass.encode())
        else:
            print("Enter some thing")
            exit(0)


def listen_from_server(client_socket):
    while True:
        massage=client_socket.recv(1024).decode()
        if massage != "":
            username=massage.split('~')[0]
            msg=massage.split('~')[1]
            print(f"[{username}] {msg}")
        else:
            print("Massage empty")

def send_username_to_server(client_socket):
    username=input("Enter username= ")

    if username != '':
        client_socket.sendall(username.encode())
    else:
        print("Usre Name not empty")
        exit(0)
    threading.Thread(target=listen_from_server,args=(client_socket, )).start()
    
    

    threading.Thread(target=send_massage,args=(client_socket, )).start()
 
def main():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client_socket.connect(('127.0.0.1',1234))
        print("Connected to server")
    except:
        print("Server not reach")
    
    send_username_to_server(client_socket)

if __name__ == '__main__':
    main()