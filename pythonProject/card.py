def Card():
    Card_no = input("Enter your Card no : ")
    length = len(Card_no)
    if(length<10 or length>10 or length==''):
        print("The Credit or Debit card number must be 10 digits ")
        print("Re-enter it : ")
    else:
        date = input("Enter expiry Month : ")
        dlen = len(date)
        year = input("Enter expiry Year : ")
        ylen = len(year)
        if(dlen<2 or dlen>2 or dlen==""):
            print("Please Enter Correct month !")
        elif(ylen<4 or ylen>4 or ylen==""):
            print("Please Enter Correct Year !")
        else:
            return True

if __name__ == '__main__':
    Card()

