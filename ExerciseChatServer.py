from socket import *

while True:
    try:
        HOST = input("Input hostname: ")
        PORT = int(input("Input port: "))

    except ValueError as e:
        print(e)

    else:
        BUFFER_SIZE = 1024
        ADDRESS = (HOST, PORT)
        server = socket(AF_INET, SOCK_STREAM)

        try:
            server.bind(ADDRESS)
            server.listen(5)

        except Exception as e:
            print(e)
        else:
            myaccount = "6130300417 Chat Server"
            print("Server Address : " + HOST + "\nServer Port : " + str(PORT))
            WelcomeMessage = "Welcome to " + myaccount + "\nTell me, who are you?"
            while True:
                print('waiting for connection...')
                client, address = server.accept()
                print('connected from: ', address)
                client.send(str.encode(WelcomeMessage))
                while True:
                    message = bytes.decode(client.recv(BUFFER_SIZE))
                    if not message:
                        print("client disconnected")
                        client.close()
                        break
                    else:
                        print("Client said :" + message)
                    client.send(str.encode(input(' > ')))
