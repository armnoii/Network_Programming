NumberList = []
while True:
    try:
        number = input("Please input number (press enter to exit) : ")
        while number > '':
            NumberList.append(int(number))
            number = input("Please input number (press enter to exit) : ")
    except ValueError as e:
        print(e)
    else:
        print("Number List :", NumberList)
        print("Length of Number List :", len(NumberList))
        print("Minimum Number :", min(NumberList))
        print("Maximum Number :", max(NumberList))
        print("Total Number :", sum(NumberList))
        print("Average Number :", sum(NumberList) / len(NumberList))
        break