class Muhammed:
    def readBooks(self):
        print("Muhammed is reading books")
    def writeArticle(self):
        print("Muhammed is writing article")
    def watchMovies(self):
        print("Muhammed is watching Movies")
    def ListenSong(self):
        print("Muhammed is Listening to Song")

class Ahmed:
    def watchMovies(self):
        print("Ahmed is watching Movies")
    def ListenSong(self):
        print("Ahmed is Listening to Song")
    def readBooks(self):
        print("Ahmed is reading books")
    def writeArticle(self):
        print("Ahmed is writing article")


m = Muhammed()
a = Ahmed()
# m.readBooks()
# m.writeArticle()
# a.watchMovies()
# a.ListenSong()


# for i in (m,a):
#     i.ListenSong()
#     i.watchMovies()
#     i.writeArticle()
#     i.readBooks()

def personStatus(omer):
    omer.writeArticle()
    omer.readBooks()

def personStatus2(ali):
    ali.ListenSong()
    ali.watchMovies()

personStatus(a)
personStatus2(m)