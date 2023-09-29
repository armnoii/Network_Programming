import hashlib
import json

plainusername = input("Please input username: ")
plainpassword = input("Please input password: ")
hashpassword = hashlib.sha256(plainpassword.encode('utf-8')).hexdigest()

jsonDict = {
    "Username" : plainusername,
    "Password" : hashpassword,
    "Fullname" : "Nanthawat Songseeda",
    "Email" : "nanthawatsong@gmail.com",
    "TelNo" : "0945378034"}

with open('userdata.json', 'w') as file:
    json.dump(jsonDict, file)

with open('userdata.json', 'r') as j:
    userdata = json.load(j)
    while True:
        username = input("Please input username: ")
        plainpassword = input("Please input password: ")
        hashpassword = hashlib.sha256(plainpassword.encode('utf-8')).hexdigest()

        if(username == userdata["Username"] and hashpassword == userdata["Password"]):
            print(userdata["Fullname"])
            print(userdata["Email"])
            print(userdata["TelNo"])
            break
        else:
            print("Not correct\n")
