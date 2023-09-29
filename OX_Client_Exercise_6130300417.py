import socket
#import os
def print_table(msg):
    #os.system("cls")
    print("")
    print(" "+str(msg[0])+" | "+str(msg[1])+" | "+str(msg[2])+" ")
    print(" "+str(msg[3])+" | "+str(msg[4])+" | "+str(msg[5])+" ")
    print(" "+str(msg[6])+" | "+str(msg[7])+" | "+str(msg[8])+" ")
    print("")

def check():
    global count
    global msg
    global tmp

    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
        if msg[0] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[0] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        if msg[3] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[3] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10
        input()
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        if msg[6] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[6] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):        
        if msg[0] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
            
        if msg[0] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        if msg[1] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[1] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):        
        if msg[2] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
            
        if msg[2] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()

    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        if msg[0] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[0] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        if msg[2] == 'x':
            print("Client WIN !!!!!!!!!!!!!!")
        if msg[2] == 'o':
            print("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to XO Game")
print("")

server = input("Connect Server (ip address or hostname) : ")
port = int(input("Input port : "))

s.connect((server, port))

BUFFER_SIZE = 1024

def clientPlay():
    global msg    
    global count
    global tmp
    count += 1
    #print_table(msg)

    while True:
        try:
            tmp = int(input("Client (x) : "))
        except ValueError as e:
            print(e)
        else:
            se = set(msg)
            se2 = set(str(tmp))
            if se & se2:
                if tmp > 0 and tmp < 10:
                    (msg[int(tmp) - 1]) = 'x'
                    s.send(str(tmp).encode('ascii'))
                    print_table(msg)
                    check()
                    break


def serverPlay():
    global msg
    global count
    global tmp
    global che

    count += 1
    tmp = s.recv(20)
    (msg[int(tmp)-1]) = 'o'
    print_table(msg)
    check()

count = 0
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
s.close()
print("Draw")



