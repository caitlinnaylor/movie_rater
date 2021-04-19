from tkinter import *
#19/04/21
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
        self.movie_info = [Movies("The Hobbit", self.default),
                          Movies("Captain America: The First Avenger", self.default),
                          Movies("Wonder", self.default)]

        self.movie_instruct = Label(parent, text = "Please Rate:", anchor = NW)
        self.movie_instruct.grid(row = 0, column = 0)

        self.movie_title = Label(parent, text= self.movie_info[0].movie)
        self.movie_title.grid(row = 0, column = 2)

        self.rating_instruct = Label(parent, text = "Your Rating:", anchor = NW)
        self.rating_instruct.grid(row = 1, column = 0)

        self.var = StringVar()
        self.var.set(0)
        self.num_radiobuttons = 6
        self.rbs = [Radiobutton(parent, text = self.default, value = self.default, variable = self.var)]

        for i in range(self.num_radiobuttons):
            self.rbs.append(Radiobutton(parent, text = f"{i+1}/5", value = f"{i+1}/5", variable = self.var))
            self.rbs[i].grid(row = i+1, column = 2, sticky = NW)

        self.nextbtn = Button(parent, text = "Next")
        self.nextbtn.grid(row = 7, column = 3)

        self.prevbtn = Button(parent, text = "Previous")
        self.prevbtn.grid(row = 7, column = 0)

        
              
                            
#main
if __name__=="__main__":
    root= Tk()
    quiz = RatingGUI(root, Movies, "No Rating")
    root.title("Movie Rater")
    root.mainloop()

