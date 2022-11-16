import socket
import threading
active_client=[] #list of all active client

#send msg to one by one user
def send_msg_to_user(masg,client):
    client.sendall(masg.encode())


#send msg to all through list
def send_msg_to_all(massage):
    for i in active_client:
        send_msg_to_user(massage,i[1])

#listen for massage
def listen_for_msg(client,username):
    while True:
        rec_msg=client.recv(2040).decode()
        if rec_msg != "":
            final_massage=username + "~" + rec_msg 
            send_msg_to_all(final_massage)
        else:
            print("Massage is empty")

#client Hendel 
def client_hendel(client):
    d=1
    #listen client massage
    # 1st massage alway client name
    while d==1:
        username= client.recv(2040).decode() 
        if username != "":
            active_client.append((username,client))
            d=2
        else:
            print('client username is empty')
    threading.Thread(target=listen_for_msg, args=(client,username, )).start()

def main():
    #server scoket
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #bind socket
    try:
        server_socket.bind(('127.0.0.1',1234))
        print("Server Running")
    except:
        print("Failed to Bind")
    
    server_socket.listen(3)
    
    while True:
        #client accept
        client, address = server_socket.accept()
        print(f"connected to {address}")

        threading.Thread(target=client_hendel, args=(client, )).start()
if __name__ == "__main__":
    main()


