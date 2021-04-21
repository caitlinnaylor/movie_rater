from tkinter import *
#21/04/21
#Caitlin Naylor
#Movie Rater

class Movies:
    def __init__(self, movie, rating):
        self.movie = movie
        self.rating = rating
        self.movie_info = [self.movie, self.rating]
        

class RatingGUI:
    def __init__(self, parent, Movies, default):
        self.default = default
        self.i = 0
        self.movie_info = [Movies("The Hobbit", self.default),
                          Movies("Captain America: The First Avenger", self.default),
                          Movies("Wonder", self.default),
                           Movies("The Lion King", self.default),
                           Movies("Mary Poppins", self.default),
                           Movies("Tangled", self.default),
                           Movies("Frozen", self.default),
                           Movies("High School Musical 1", self.default),
                           Movies("Life of Pi", self.default),
                           Movies("Titanic", self.default),
                           Movies("Jojo Rabbit", self.default),
                           Movies("The Martian", self.default),
                           Movies("Ant-Man", self.default)]

        self.movie_instruct = Label(parent, text = "Please Rate:", anchor = NW, bg = "black", fg = "white", font = ("Sans Serif", 20), pady = 20, padx = 20)
        self.movie_instruct.grid(row = 0, column = 0)

        self.movie_title = Label(parent, text= self.movie_info[self.i].movie, bg = "black", fg = "white", font = ("Sans Serif", 20), anchor = NE, pady = 20, padx = 70)
        self.movie_title.grid(row = 0, column = 1, columnspan = 3)

        self.rating_instruct = Label(parent, text = "Your Rating:", anchor = NW, fg = "black", font = ("Sans Serif", 18), pady = 20, bg = "#d4a8ed")
        self.rating_instruct.grid(row = 1, column = 0)

        self.var = StringVar()
        self.var.set(0)
        self.num_radiobuttons = 6
        self.rbs = [Radiobutton(parent, text = self.default, value = self.default, variable = self.var, fg = "black", font = ("Sans Serif", 14), pady = 20, bg = "#d4a8ed")]

        self.space_holder_temporary = Label(parent, text = "", padx = 20, bg ="#d4a8ed" )
        self.space_holder_temporary.grid(row = 1, column = 1)

        for i in range(self.num_radiobuttons):
            self.rbs.append(Radiobutton(parent, text = f"{i+1}/5", value = f"{i+1}/5", variable = self.var, fg = "black", font = ("Sans Serif", 14), pady = 10, bg = "#d4a8ed"))
            self.rbs[i].grid(row = i+1, column = 2, sticky = NW)
        self.nextbtn = Button(parent, text = "Next", bg = "#801bb3", fg = "white", font = ("Sans Serif", 14), command = self.nextmovie)
        self.nextbtn.grid(row = 7, column = 3, sticky = NE)

        self.prevbtn = Button(parent, text = "Previous", bg = "#801bb3", fg = "white", font = ("Sans Serif", 14), command = self.prevmovie)
        self.prevbtn.grid(row = 7, column = 0, sticky = NW)


    def nextmovie(self):
        self.movie_info[self.i].rating = self.var.get()
        if self.i != (len(self.movie_info)-1):
            self.i+=1
        else:
            self.i = 0
        self.var.set(0)
        self.movie_title.configure(text = self.movie_info[self.i].movie)

    def prevmovie(self):
        self.movie_info[self.i].rating = self.var.get()
        if self.i !=0:
            self.i-=1
        else:
            self.i = (len(self.movie_info)-1)
        self.var.set(0)
        self.movie_title.configure(text = self.movie_info[self.i].movie)
          
                            
#main
if __name__=="__main__":
    root= Tk()
    ratings = RatingGUI(root, Movies, "No Rating")
    root.title("Movie Rater")
    root.configure(bg = "#d4a8ed")
    root.mainloop()

