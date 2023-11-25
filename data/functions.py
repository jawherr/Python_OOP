# def usama():
#     pass
# def ahmed(name):
#         print("ahmed  {}".format(name))
#
# def muhammed():
#         print("Muhammed Essa")
#
# def sum(a,b):
#     print(a+b)
#
# ahmed("Essa Hameed")
# muhammed()
# sum(1,2)

# def numbers(num1,num2,num3):
#     print(num1+num2*num3)
#
# def personInfo(fname,lname,age,salary):
#     print("person info : fname {}  lname {} age {} salary {}".format(fname,lname,age,salary))
#
#
# numbers(1,2,3)
#
# personInfo("muhammed","essa",33,2000)


#
# def personInfo(fname,lname,age =0,salary=2000):
#     print("person info : fname {}  lname {} age {} salary {}".format(fname,lname,age,salary))
#
#
# personInfo("muhammed","essa" )



# print("-------------------")
#
# def personInfo(fname,lname=None,age =0,salary=2000):
#     if lname == None:
#        lname = "default"
#     print("person info : fname {}  lname {} age {} salary {}".format(fname,lname,age,salary))
#
#
# personInfo("muhammed" )





# print("-------------------")
#
# def personInfo(*args):
#      print("person info : fname {}  lname {} age {} salary {}".format(*args))
#
#
# personInfo("muhammed","essa",33,2000 )


def personInfo(name,lname,age,*args ):

    for  i in args :
        print(i,end="")
    print(*args ,name,lname,age)


personInfo("muhammed", "essa", 33, 2000,"muhammed", "essa", 33, 2000)


















