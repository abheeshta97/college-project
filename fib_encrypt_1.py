from tkinter import Tk, messagebox
import creationANDopening as note
#---INITIALIZATION OF LOWER AND UPPER ASCII LIMIT
ASCII_MIN = 33
ASCII_MAX = 126

#---FUNCTION TO CONVERT LIST TO STRING---
def convertToString(s):

    #---INITIALIZATION OF STRING---
    new = ""

    #---TRAVERSES THE STRING---
    for x in s:
        new += x

    return new

#---FUNCTION TO REVERSE STRING---
def reverse_string(s):
    """Return a reversed copy of `s`"""
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

#---FUNCTION TO ENCRYPT MESSAGE FROM FILE---
def encrypt(inputMessage):
    try:
        file_1 = open(inputMessage, "r")
        fileMessage = file_1.read()
        file_1.close()
        reversedMessage=[]
        fileMessage=fileMessage.split()

        for i in fileMessage:
            reversedChar=reverse_string(i)
            reversedMessage.append(reversedChar)

        fileMessage=reversedMessage
        #print('\nThe reversed Message in list format=',fileMessage)
        message=fileMessage
        dataAppend=[]  #IS DEFINED TO HOLD THE ENCRYPTED MESSAGE IN LIST TYPE

        for word in message:
            counter=True
            n1=0
            n2=1

            for letter in word:
                loopLetter = letter
                if counter==True:
                    data_num = ord(loopLetter)
                    for num in range(0, len(word)):  #LOOP TO RUN N TIMES FOR EACH CHAR

                        for i in range(0, n2):         #LOOP TO INCREMENT THE POSITION
                            if(data_num == ASCII_MAX):
                                data_num = ASCII_MIN    #CHECKS UPPER LIMIT

                            else:
                                data_num += 1
                        data = chr(data_num)

                        temp = n1
                        n1 = n2
                        n2 = temp + n1

                    counter = False
                    n1 = 0
                    n2 = 1

                else:
                    data_num = ord(loopLetter)
                    for num in range(0, len(word)):  # LOOP TO RUN

                        for j in range(0, n2):  # LOOP TO DECREMENT THE POSITION
                            if (data_num == ASCII_MIN):
                                data_num = ASCII_MAX  # CHECKS LOWER LIMIT

                            else:
                                data_num -= 1

                        data = chr(data_num)
                        temp = n1
                        n1 = n2
                        n2 = temp + n1

                    counter = True
                    n1 = 0
                    n2 = 1

                dataAppend += data
            dataAppend += " "
        #print(dataAppend)

        newMessage=convertToString(dataAppend)  #ENCRYPTED LIST CONVERTED TO STRING
        return(newMessage)
    except:
        messagebox.showwarning("ERROR", ".txt FILE REQUIRED")

def encrypted(encryptedmessage):
    encryptedData=encrypt(encryptedmessage)
    messagebox.showinfo("Information", "ENTER IN THE NAME FOR FILE TO ENCRYPT ")
    note.save_as(encryptedData)
