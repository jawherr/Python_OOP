# num1 = 0
# num2 = [1,2,3,4,5,6,7,8,9,10]
# mystr = "Muhammed Essa"
# mystr2 = """
# Muhammed Essa
# ahmed essa
# osama essa
# """

# while num1 <30 :
#     print(num1)
#     num1+=2  # num1 = num1+1
#
# myfile = open('name.txt')
#
# for i in myfile:
#     print(i ,end="")


# myfile = open('name.txt')
#
# for num,i in  enumerate(myfile):
#     print(num+1,i ,end="")

# for  i in   "Muhammed Essa Hameed" :
#     # if i == "M":
#     #   print("index {} for value {}".format(i,num)  )
#     if i == "m":
#       break
#     print(" value {}".format(i ) ,end="" )

num1 = 0
mystr = "Muhammed Essa Hameed"
while(num1 < len(mystr)):
    print(mystr[num1],end="")
    num1+=1
else:
    print("Ahmed Usama Hameed")