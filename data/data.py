numTuple = (1,2,3,4,5,6)
# print(numTuple)
# print(type(numTuple))
numList = [1,2,3,4,5,6,7,8]
# print(numList)
# print(type(numList))
# print('-------------')
# print(numTuple[2])
# print(numList[2])
# print('-------------')
# print(numTuple[4])
# print(numList[4])
#
# print('-------------')
# print(numTuple[-4])
# print(numList[-4])
# print('-------------')
# print(numTuple[-1])
# print(numList[-1])
#
# print('-------------')
# num2list = [1]
# num2Tuple = (1,)
# print(num2Tuple)
# print(type(num2Tuple))
# print(num2list )
# print(type(num2list))

# print('-------------')
#
# print(max(numList))
# print(max(numTuple))
#
# print('-------------')
#
# print(min(numList))
# print(min(numTuple))
#
# print('-------------')
#
# print(len(numList))
# print(len(numTuple))




# print('-------------')
# myList = list(range(10))
# myTuple = tuple(range(10))
# myList[4] = 99
# print( myList )
# print(myTuple)
# print(99 in myList)
# print(9 in myTuple)

# print('-------------')
#
# print(919 not in myList)
# print(91 not in myTuple)
#
# for i in myList:
#     print(i)
# print('-------------')
# for i in myTuple:
#     print(i)



# print('-------------')
# myList = list(range(10))
# myTuple = tuple(range(10))
# print( myList )
# print(myTuple)

# myList.insert(2,100)
# print( myList )
#
# myList.append(110)
# print( myList )


# print(myTuple.count(1))
# print(myTuple.index(3))


# print(myList.count(1))
# print(myList.index(0))
#myList.remove(9)
# myList.extend(range(10))
# print(myList)


mydict = {1:"Muhammed",2:"Essa",3:"Hameed"}

# print(mydict)

mydict2 = dict(m="Muhammed",e="Essa",h="Hameed")
# print(mydict2)
#
# print('m' in mydict2)

# for x in mydict:
#     print(x)
#
# for x,n in mydict.items():
#     print(x,n)


# print(mydict2['m'])
#
# print(mydict.get(3,"not exist") )

# mydict.pop(2)
# print( mydict)
# mydict.pop(1)
# print( mydict)
# del mydict2['m']
# print( mydict2)


print( "--------------")

names = { "Muhammed", "Essa", "Hameed"}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# print( names)
# print( basket)
#
# a = set('abracadabra')
# print( a)
#
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print( a)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket2 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket3 = {  'orange', 'banana'}
basket4 = {  'oranges', 'bananas', 'pear'}

# checksets = basket.issubset(basket3)
# checksets1 = basket.issuperset(basket3)
# print(checksets)
# print(checksets1)
# checksets3 = basket3.issubset(basket)
# checksets4 = basket3.issuperset(basket)
# print(checksets3)
# print(checksets4)
print( "--------------")
# checksets2 = basket.union(basket4)
# print(checksets2)
# basket.intersection()

# print( "--------------")
# print(basket)
# basket.remove('apple')
# print(basket)

# basket.pop()
# print(basket)
# basket.pop()
# print(basket)



print(basket)
# basket5 = basket.intersection(basket3)
# print(basket5)

# basket6 = basket.difference(basket4)
# print(basket6)
basket.remove('apple')
print(basket)
basket.add('google')
print(basket)
# basket.update(basket4)
# print(basket)
basket7 = basket.union(basket4)
print(basket7)