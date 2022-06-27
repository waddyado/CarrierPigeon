import os
import socket
import datetime
from cryptography.fernet import Fernet
import base64

def code():
    #user input for code
    global a
    global b
    global c
    global code
    a = input('Code 1 :>')
    b = input('Code 2 :>')
    c = input('Code 3 :>')
    code = a + b + c
    
    main()

def main():
    print('     Carrier Pigeon     ')
    print(' Covert communications')
    print('Type 1 to send')
    print('Type 2 to listen')
    poop = input(':>')
    
    if poop == '1':
        send()
        
    elif poop == '2':
        recieve()
    

    
def send():
    print('Send a Message')
    listenerip = input('Listener IP:>')
    listenerport = input('Listener port:>')

    #connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((listenerip, int(listenerport)))
    print('Connected to server with code ', a, b, c)

    #send code to verify they both match
    code = a + b + c
    client.send(code.encode('utf-8'))

    #Define encryption Key
    enckey = str('v-A9qmAhCdwb3aAAOyzPtGG5jfHtXJ1Rt5JS4OS5eVw=')
    fernet = Fernet(enckey)
    #send messages
    while True:
        message = input('Enter Message:>')
        
        #encrypt message with fernet cipher
        encrypt = fernet.encrypt(message.encode())
        encrypted = str(encrypt)
        #send encrypted message
        client.send(encrypted.encode('utf-8'))
        current_time = datetime.datetime.now()
        print('Message sent at ', current_time)
        print(' ')


def recieve():
    print('Recieve a Message')
    ip = input('Enter IP address:>')
    port = input('Enter Port:>')
    #initialize server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, int(port)))
    serv.listen()
    print('Listening on Port:', port,'with IP:', ip)
    while True:
        conn, addr = serv.accept()
        from_client = ''

        #event handler
        with conn:
            print('Connection Established')
            print('Code ', a, b, c)
            print('Session Created with' , addr)

            #check that code matches
            codie = conn.recv(1024)
            checker = codie.decode()
            if checker == code:
                print('Code verified')
                #after code is verified the encryption key is defined
                fernet = 'v-A9qmAhCdwb3aAAOyzPtGG5jfHtXJ1Rt5JS4OS5eVw='
                fernetkey = Fernet(fernet)
                print('Key for session is ', fernetkey)
                while True:
                    #recieving messages
                    message = conn.recv(1024)
                    current_time = datetime.datetime.now()
                    print('message recieved at ', current_time)
                    missage = message.decode()
                    print('Encrypted message:> ', message)
                    print(' ')
            else:
                print('Given code of ', checker, 'does not match')
                conn.close()
                print('Closed connection')

            #keyman = conn.recv(1024)
            #key = keyman.decode()
            #key = bytes(key)
            
            



code()

