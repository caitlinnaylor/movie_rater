from tkinter import *
#25/04/21
#Caitlin Naylor
#Movie Rater

class Movies:
    def __init__(self, movie, rating):
        self.movie = movie
        self.rating = rating
        self.movie_info = [self.movie, self.rating]
        

class RatingGUI:
    def __init__(self, parent, Movies, default):
        f1 = Frame(parent)
        f1.configure(bg = "#d4a8ed")
        self.default = default
        self.i = 0
        self.movie_info = [Movies("The Hobbit", self.default),
                          Movies("Thor Ragnarok", self.default),
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

        self.movie_instruct = Label(f1, text = "Please Rate:", anchor = NW, bg = "black", fg = "white", font = ("Sans Serif", 20), width = 15, pady = 20, padx = 20)
        self.movie_instruct.grid(row = 0, column = 0)

        self.movie_title = Label(f1, text= self.movie_info[self.i].movie, bg = "black", fg = "white", font = ("Sans Serif", 20), anchor = NW, pady = 20, padx = 20, width = 18)
        self.movie_title.grid(row = 0, column = 1, columnspan = 3)

        self.rating_instruct = Label(f1, text = "Your Rating:", anchor = NW, fg = "black", font = ("Sans Serif", 18), pady = 20, bg = "#d4a8ed", padx = 20)
        self.rating_instruct.grid(row = 1, column = 0, sticky = NW)

        self.var = StringVar()
        self.var.set(0)
        self.num_radiobuttons = 6
        self.rbs = [Radiobutton(f1, text = self.default, value = self.default, variable = self.var, fg = "black", font = ("Sans Serif", 14), pady = 20, bg = "#d4a8ed")]

        self.space_holder= Label(f1, text = "", padx = 20, bg ="#d4a8ed" )
        self.space_holder.grid(row = 1, column = 1)

        for i in range(self.num_radiobuttons):
            self.rbs.append(Radiobutton(f1, text = f"{i+1}/5", value = f"{i+1}/5", variable = self.var, fg = "black", font = ("Sans Serif", 14), pady = 10, bg = "#d4a8ed"))
            self.rbs[i].grid(row = i+1, column = 2, sticky = NW)
        self.nextbtn = Button(f1, text = "Next", bg = "#801bb3", fg = "white", font = ("Sans Serif", 14), command = self.nextmovie)
        self.nextbtn.grid(row = 7, column = 3, sticky = NE)

        self.prevbtn = Button(f1, text = "Previous", bg = "#801bb3", fg = "white", font = ("Sans Serif", 14), command = self.prevmovie)
        self.prevbtn.grid(row = 7, column = 0, sticky = NW)

        f1.grid(column = 0, row = 0)

        f2 = Frame(parent)
        f2.configure(bg = "#500178", pady = 10)

        self.var_two = StringVar()
        self.var_two.set(0)

        self.search_instruct = Label(f2, text = "Search for movies with a rating of:", fg = "white", bg = "#500178", font = ("Sans Serif", 18), padx = 54, width = 36)
        self.search_instruct.grid(row = 0, column = 0, columnspan = 4, sticky  = NW)

        self.search_rbs = [Radiobutton(f2, text = self.default, value = self.default, variable = self.var_two, fg = "white", font = ("Sans Serif", 14), padx = 20,bg = "#500178", pady = 10)]

        self.num_search_radiobuttons = 3 #in in row
        for i in range(self.num_search_radiobuttons-1):
            self.search_rbs.append(Radiobutton(f2, text = f"{i+1}/5", value = f"{i+1}/5", variable = self.var_two, fg = "white", pady = 10, padx = 20, font = ("Sans Serif", 14), bg = "#500178"))

        for i in range(self.num_search_radiobuttons):
            self.search_rbs.append(Radiobutton(f2, text = f"{i+3}/5", value = f"{i+4}/5", variable = self.var_two, fg = "white", pady = 10, padx = 20, font = ("Sans Serif", 14), bg = "#500178"))

        for i in range(self.num_radiobuttons):
            if i <=2:
                self.search_rbs[i].grid(row = 1, column = i, sticky = NW)
            else:
                self.search_rbs[i].grid(row = 2, column = i-3, sticky = NW)

        self.searchbtn = Button(f2, text = "Go", bg = "white", fg = "black", font = ("Sans Serif", 14))
        self.searchbtn.grid(row = 11, column = 3, sticky = NW)

        f2.grid(column = 0, row = 8)
        
    def nextmovie(self):
        if self.var.get() != "0":
            self.movie_info[self.i].rating = self.var.get()
        if self.i != (len(self.movie_info)-1):
            self.i+=1
        else:
            self.i = 0
        self.var.set(0)
        self.movie_title.configure(text = self.movie_info[self.i].movie)


    def prevmovie(self):
        if self.var.get() != "0":
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
    root.mainloop()

