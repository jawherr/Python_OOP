# myfile = open("name.txt","r")
# myStr="Python3"
# list = ["10.0.0.1","10.0.0.11","10.0.0.21","10.0.0.31","10.0.0.111" ]
# myfile2 = open("name2.txt","w")
# for i in list:
#     print(i,file=myfile2 )
# print("Done !", end="")

# bufferSize = 70000
# myfile = open("name.txt","r")
# myfile2 = open("name3.txt","w")
# buffer = myfile.read(bufferSize)
# while len(buffer):
#     myfile2.write(buffer)
#     buffer = myfile.read(bufferSize)
# print("Done")








bufferSize = 70000
myfile = open("python.jpg","rb")
myfile2 = open("python3.jpg","wb")
buffer = myfile.read(bufferSize)
while len(buffer):
    myfile2.write(buffer)
    buffer = myfile.read(bufferSize)
print("Done")