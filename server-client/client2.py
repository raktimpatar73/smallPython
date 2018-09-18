import socket
import time

PORT = 12345
s = socket.socket()
try:
    s.connect(('127.0.0.1',PORT))

    print("Server: %s" %(s.recv(1024).decode('utf-8')))
    while True:
        
        message = input("Enter your message: ")
        s.sendto(message.encode('utf-8'),('127.0.0.1',PORT))
        recieved_mess=s.recv(1024).decode('utf-8')
        print("Server: %s" %(recieved_mess))

        if recieved_mess.lower()=="goodbye":
            print("Closing client2.....")
            time.sleep(1)
            s.close()
            break
except ConnectionRefusedError:
    print("Connection Failed....!")
    print("Please start your server!")
    
       


    

    

