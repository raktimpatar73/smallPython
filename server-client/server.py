import socket
import time
import os

PORT = 12345
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', PORT))
print('Socket is binded to:',PORT)
s.listen(100)
print("Socket is listening.....")

while 1:
    conn, addr = s.accept()    
    child_pid = os.fork() 
    

    if child_pid==0:
        print('Got connection from', addr)
        conn.sendto("Welcome to the server!".encode('utf-8'),addr)
    
        while True:
            recieved_mess=conn.recv(1024).decode()
            print("Client: ",recieved_mess)
            if recieved_mess.lower() == "bye":
                message = "Goodbye"
                conn.sendto(message.encode('utf-8'),addr)
                print("Server closing connection from addr",addr," ...")
                
                time.sleep(1)
                conn.close()
                break
            else:
                message = "OK"
                conn.sendto(message.encode('utf-8'),addr)
        print("Socket is listening.....")
        break

s.close()




