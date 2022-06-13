
from cryptography.fernet import *
from Crypto.Cipher import AES
from tkinter import *
import io
import PIL.Image
import os


print("\nENTER 1 FOR TEXT ENCRYPTION AND DECRYPTION \nENTER 2 FOR IMAGE ENCRYPTION AND DECRYPTION")
while True:
    N = int(input("\nENTER THE NUMBER:"))
    if N==1:
        print("TEXT ENCRYPTION AND TEXT DECRYPTION")
        def a():
            x= Fernet.generate_key()
            with open("key.file", "wb") as y:
                y.write(x)
        def b():
            return open("key.file", "rb").read()
        a()
        z= b()
        text=input("ENTER TEXT :")
        f = Fernet(z)
        print("\nENCRYPTION OF TEXT  :",f.encrypt(text.encode()))
        print("DECRYPTION OF TEXT  :",f.decrypt(f.encrypt(text.encode())))
    elif N==2:
        print("IMAGE ENCRYPTION AND DECRYPTION")
        key = b'1234567890987654'
        inivectr = b'9876543210876543'

        def encryptimage():
            global key, inivectr, folder, x
            path = str(folder.get())
            if (path == "" or path[0] == " "):
                path = os.getcwd()
            file = []
            for root, dir, filess in os.walk(path):
                for files in filess:
                    if ((('.JPG' in files) or ('.jpg' in files)) and ('.enc' not in files)):
                        file.append(os.path.join(root, files))
            for filename in file:
                inptfile = open(filename, "rb")
                data = inptfile.read()
                inptfile.close()
                cipher = AES.new(key, AES.MODE_CFB, inivectr)
                encddata = cipher.encrypt(data)
                encdfile = open(filename + ".enc", "wb")
                encdfile.write(encddata)
                encdfile.close()
            x.destroy()
            x = Tk()
            x.title("Encryption is done successfully ")
            x.geometry("400x400")
            label = Label(text="Encryption is done successfully", height=55,width=55,font=(NONE,20))
            label.pack(anchor=CENTER, pady=52)
            x.mainloop()
        def decryptimage():
            global key, inivectr, folder, x
            path = str(folder.get())
            if (path == "" or path[0] == " "):
                path = os.getcwd()
            file = []
            for root, dir, filess in os.walk(path):
                for files in filess:
                    if '.enc' in files:
                        file.append(os.path.join(root, files))
            for filename in file:
                encdfile2 = open(filename, "rb")
                encddata2 = encdfile2.read()
                encdfile2.close()

                decipher = AES.new(key, AES.MODE_CFB, inivectr)
                plaintext =decipher.decrypt(encddata2)

                imgstream = io.BytesIO(plaintext)
                imgfile = PIL.Image.open(imgstream)
                if ('.jpg' in filename):
                    imgfile.save((filename[:-8]) + ".JPG")
                elif ('.JPG' in filename):
                    imgfile.save((filename[:-8]) + ".jpg")
            x.destroy()
            x = Tk()
            x.title("Decryption is done successfully ")
            x.geometry("400x400")
            label = Label(text="Decryption is done Successfully ", height=55, width=55,font=(None,20))
            label.pack(anchor=CENTER, pady=54)
            x.mainloop()
        x=Tk()
        x.title( "Encryption nd Decryption of Images")
        folderdirlabel = Label(text="Enter directry")
        folderdirlabel.pack()
        folder = Entry(x)
        folder.pack()
        encrypt = Button(text="Encrypt All", command=encryptimage)
        encrypt.pack()
        label = Label(text="Give Blank space for Current Working Directory")
        label.pack()
        decrypt = Button(text="Decrypt All", command=decryptimage)
        decrypt.pack()

        x.mainloop()
    print("\nPRESS 'Y' TO CONTINUE,  'N'  TO EXIT ")
    x=input("ENTER A KEY:")
    if x=='Y'or x=='y':
        continue
    else:
        break
