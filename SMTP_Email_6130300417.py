import smtplib
try:
    input = open("SMTP_Account.txt")
    account, password, receivers = input.read().split(";")
    input.close()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        try:
            server.login(account, password)
            msg = "Test SMTP Message"
            server.sendmail(account, receivers, msg)
            print("Send Mail Success")
        except:
            print("Incorrect account or password")
        finally:
            print("Quit Server")
            server.quit()
    except:
        print("server not found")
except:
    print("file not found")
