import os
import urllib.request
from ftplib import FTP
import socket

# myDir = os.getcwd()
# print(myDir)

#makeDirectory = os.mkdir("newFolder")

#renamemyFolder = os.rename("Muhammed","Ahmed")

# myUrl = urllib.request.urlopen("https://www.facebook.com")
# print(myUrl.read())



# ftp = FTP('172.0.0.1')
# ftp.login(user="jawher",passwd="kalle")
# ftp.cwd('/')



so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

targ = input("what is your ip :")

def portScan(port):
    try:
        con = so.connect((targ,port))

        return  True
    except  :
        return False

for i in range(31):
    if portScan(i):
        print("Post number : {} is open :)".format(i))









