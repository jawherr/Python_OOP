class mySq:
    def __init__(self,value1=0,value2=0):
        self.value1 =value1
        self.value2 = value2
    def result(self):
        print( self.value1 * 4)


class myRec:
    def __init__(self,value1=0,value2=0):
        self.value1 =value1
        self.value2 = value2
    def result(self):
        print( (self.value1+self.value2) * 2)



m = mySq(2)
a = myRec(2,4)
# m.readBooks()
# m.writeArticle()
# a.watchMovies()
# a.ListenSong()


for i in (m,a):
    i.result()


# def personStatus(omer):
#     omer.result()
#
#
# def personStatus2(ali):
#     ali.result()
#
# personStatus(m)
# personStatus2(a)