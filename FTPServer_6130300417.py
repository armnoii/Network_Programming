from ftplib import FTP
try:
    input = open("Account.txt", encoding="utf-8")
except IOError:
    print("Can not find file")
else:
    ip, user, password = input.read().split(";")
    input.close()
    try:
        ftp = FTP(ip)
        ftp.login(user=user, passwd=password)
    except:
        print("Invalid username or code")

    else:
        def dowloadFile():
            filename = 'NetProScore.txt'
            localfile = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            localfile.close()

        dowloadFile()

        total_Score = []
        total_Score2 = []
        count = []
        sumScore = 0
        sumScore_2 = 0

        try:

            saveFile = open('NetProScore_6130300417.txt', 'w', encoding="utf-8")
            inputText = open("NetProScore.txt", 'r', encoding="utf-8")
            inputText2 = open("NetProScore.txt", 'r', encoding="utf-8")
            i = 0
        except IOError:
            print("Can not find file")
        else:
            for read in inputText:
                No_2, ID_2, Score_P1_2, Score_P2_2 = read.split()
                sumScore_2 = int(Score_P1_2) + int(Score_P2_2)
                total_Score2.append(sumScore_2)

                maxNum = max(total_Score2)
                minNum = min(total_Score2)

                i = i + 1

                if i == 47:
                    averageScore = sum(total_Score2)/len(total_Score2)
                    saveFile.write("คะแนนสูงสุด = " + str(max(total_Score2)) + "\n")
                    saveFile.write("คะแนนต่ำสุด = " + str(min(total_Score2)) + "\n")
                    saveFile.write("คะแนนเฉลี่ย = %.2f" % averageScore + "\n")
                    saveFile.write("\n")
                    for i in inputText2:
                        No, ID, Score_P1, Score_P2 = i.split()
                        sumScore = int(Score_P1) + int(Score_P2)
                        total_Score.append(sumScore)
                        maxNumber = int(maxNum) - int(sumScore)
                        minNumber = int(sumScore) - int(minNum)
                        avgNumber = int(sumScore) - int(averageScore)
                        saveFile.write("รหัส " + ID + " ได้คะแนนรวม " + str(sumScore) + "\n")
                        saveFile.write("ได้น้อยกว่าคะแนนสูงสุด " + str(maxNumber) + "\n")
                        saveFile.write("ได้มากกว่าคะแนนต่ำสุด " + str(minNumber) + "\n")
                        if avgNumber > 0:
                            saveFile.write("ได้มากกว่าคะแนนเฉลี่ย " + str(avgNumber) + "\n")
                        else:
                             saveFile.write("ได้มากกว่าคะแนนเฉลี่ย " + str(0) + "\n")
                        saveFile.write("\n")
            saveFile.close()

            def upLoadFile():
                fileName = 'NetProScore_6130300417.txt'
                ftp.storbinary('STOR ' + fileName, open(fileName, 'rb'))
            ftp.mkd('6130300417')
            ftp.cwd('6130300417')
            upLoadFile()

            ftp.pwd()
            ftp.retrlines('LIST')
            ftp.quit()