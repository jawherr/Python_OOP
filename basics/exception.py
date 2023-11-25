# try:
#     myfile = open("aname.txt")
#     for i in myfile:
#         print(i,end="")
# except IOError as err:
#     print("please fix this error : {}".format(err))

while True:
     try:
        x = int(input("Please enter a number: "))
        print(x)
        break
     except ValueError:
        print("Oops!  That was no valid number.  Try again...")