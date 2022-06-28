import os
import socket
import datetime


def code():
    #user input for code
    global code
    code = input('Enter Code:>')
    
    main()

def main():
    print('    ')
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
    print('Connected to server with code ', code)

    #send code to verify they both match
    client.send(code.encode('utf-8'))

    while True:
        message = input('Enter Message:>')
        
        #encrypt message with fernet cipher
        #send encrypted message
        client.send(message.encode('utf-8'))
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
            print('Code ', code)
            print('Session Created with' , addr)

            #check that code matches
            codie = conn.recv(1024)
            checker = codie.decode()
            if checker == code:
                print('Code verified')
                print('-------------------------------')
                print('Code for session is ', code)
                while True:
                    #recieving messages
                    message = conn.recv(1024)
                    current_time = datetime.datetime.now()
                    print('message recieved at ', current_time)
                    print('------------------------------------')
                    print('Message Content:> ', message.decode('utf-8'))
                    print(' ')
            else:
                print('Given code of ', checker, 'does not match')
                conn.close()
                print('Closed connection')





code()

