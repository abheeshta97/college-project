from tkinter import messagebox

import fib_encrypt_1 as f
import creationANDopening as note
ASCII_MIN = 33
ASCII_MAX = 126

def decrypt(inputMessage):
    file_1 = open(inputMessage, "r")
    fileMessage = file_1.read()
    file_1.close()
    revMessageList = []
    originalMessage = []
    fileMessage = fileMessage.split()
    message=fileMessage

    for word in message:
        counter=True
        n1=0
        n2=1

        for letter in word:
            loopLetter = letter
            if counter==False:
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

                counter = True
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

                counter = False
                n1 = 0
                n2 = 1

            revMessageList += data
        revMessageList += " "
    #print("revMessageList: ", revMessageList)

    newMessage = f.convertToString(revMessageList)
    newMessage = newMessage.split()
    #print("New Message = ", newMessage)
    for i in newMessage:                         #REVERSES THE MESSAGE
        originalChar=f.reverse_string(i)
        originalMessage.append(originalChar)

    #print('\nThe reversed Message in list format=',originalMessage)
    finalMessage = " ".join(originalMessage)

    return(finalMessage)

def decrypted(decryptedMessage):
    decryptedData = decrypt(decryptedMessage)
    messagebox.showinfo("Information", "ENTER IN FILE NAME TO HOLD DECRYPTED CONTENTS")

    note.save_as(decryptedData)
