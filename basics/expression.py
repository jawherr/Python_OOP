import re

mystring = """
Lorem Ipsum is Essa simply dummy text of the printing 
and typesetting industry. Essa Lorem Ipsum has been the industry's 
standard dummy text ever Essa since the 1500s, when an unknown printer 
took a galley of type and Essa scrambled it to make a type specimen book. 
It has survived not only Essa five centuries, but also the leap into 
electronic typesetting, Essa remaining essentially unchanged. It was 
popularised in the 1960s Essa with the release of Letraset sheets 
containing Lorem Ipsum passages, and more recently with desktop 
publishing software like Aldus PageMaker including versions of 
Lorem Ipsum.

"""

# for i in mystring:
#     if re.search('E',i):
#         print(i,end="")

# myfile = open('name.txt')
#
# for i in myfile:
#     if re.search('(E|e)ssa',i):
#         print(i,end="")


# myfile = open('name.txt')
#
# for i in myfile:
#     match = re.search('(E|e)i',i)
#     if match:
#         print(match.group() )





# myfile = open('name.txt')
#
# for i in myfile:
#     print ( re.sub('(E|e)ssa',"Omer",i))




# myfile = open('name.txt')
#
# for i in myfile:
#     if re.search('(E)ssa',i,re.IGNORECASE):
#         print(i,end="")


myfile = open('name.txt')
pattern = re.compile('(E|e)ssa',re.IGNORECASE)
for i in myfile:
    if re.search(pattern,i ):
        print(i,end="")



myfile = open('name.txt')
pattern = re.compile('(E|e)ssa',re.IGNORECASE)
for i in myfile:
    if re.search(pattern,i ):
        print(pattern.sub("Omer",i),end="")