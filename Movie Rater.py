from tkinter import *
from tkinter.scrolledtext import *
#25/04/21
#Caitlin Naylor
#Movie Rater

class Movies:
    def __init__(self, movie, rating):
        self.movie = movie
        self.rating = rating
        self.movie_info = [self.movie, self.rating]
        

class MovieRaterGUI:
    def __init__(self, parent, Movies, default):
        #Frame One
        self.f1 = Frame(parent)
        self.f1.configure(bg = "#d4a8ed")
        self.default = default
        self.summary_rating = ""
        self.i = 0 #which movie is being rated
        #List of movies that the user can rate
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
        #Labels

        self.movie_instruct = Label(self.f1, text = "Please Rate:", anchor = NW, bg = "black",
                                    fg = "white", font = ("Sans Serif", 16), width = 15,
                                    pady = 20, padx = 20)
        self.movie_instruct.grid(row = 0, column = 0)

        self.movie_title = Label(self.f1, text= self.movie_info[self.i].movie, bg = "black",
                                 fg = "white", font = ("Sans Serif", 16), anchor = NW,
                                 pady = 20, padx = 20, width = 18)
        self.movie_title.grid(row = 0, column = 1, columnspan = 3)

        self.rating_instruct = Label(self.f1, text = "Your Rating:", anchor = NW, fg = "black",
                                     font = ("Sans Serif", 14), pady = 16, bg = "#d4a8ed",
                                     padx = 20)
        self.rating_instruct.grid(row = 1, column = 0, sticky = NW)

        #Radiobuttons of what rating the movie is

        self.var = StringVar()
        self.var.set(0)
        self.num_radiobuttons = 7
        self.rbs = [Radiobutton(self.f1, text = self.default, value = self.default,
                                variable = self.var, fg = "black", font = ("Sans Serif", 10),
                                pady = 20, bg = "#d4a8ed",activebackground = "#d4a8ed"),
                    Radiobutton(self.f1, text = "Unsure", value = "Unsure",
                                variable = self.var, fg = "black", font = ("Sans Serif", 10),
                                pady = 10, bg = "#d4a8ed",activebackground = "#d4a8ed")]

        self.space_holder= Label(self.f1, text = "", padx = 20, bg ="#d4a8ed" )
        self.space_holder.grid(row = 1, column = 1)

        for i in range(self.num_radiobuttons):
            self.rbs.append(Radiobutton(self.f1, text = f"{i+1}/5 Stars", value = f"{i+1}/5 Stars",
                                        variable = self.var, fg = "black",
                                        font = ("Sans Serif", 10), pady = 10, bg = "#d4a8ed",
                                        activebackground = "#d4a8ed"))
            self.rbs[i].grid(row = i+1, column = 2, sticky = NW)

        #Save Rating Button
        self.savebtn = Button(self.f1, text = "Save Rating", bg = "black", fg = "white",
                              font = ("Sans Serif", 10), command = self.saverating)
        self.savebtn.grid(row = 8, column = 2, sticky = NW)

        #Next and Previous Buttons
            
        self.nextbtn = Button(self.f1, text = "Next", bg = "#801bb3", fg = "white",
                              font = ("Sans Serif", 10), command = self.nextmovie)
        self.nextbtn.grid(row = 9, column = 3, sticky = NE)

        self.prevbtn = Button(self.f1, text = "Previous", bg = "#801bb3", fg = "white",
                              font = ("Sans Serif", 10), command = self.prevmovie)
        self.prevbtn.grid(row = 9, column = 0, sticky = NW)

        self.f1.grid(column = 0, row = 0)

        #Frame Two
        f2 = Frame(parent)
        f2.configure(bg = "#500178", pady = 10)

        #Instruction Label

        self.search_instruct = Label(f2, text = "Search for movies with a rating of:",
                                     fg = "white", bg = "#500178", font = ("Sans Serif", 14),
                                     padx = 58, width = 33)
        self.search_instruct.grid(row = 0, column = 0, columnspan = 4, sticky  = NW)

        #Radiobuttons of what rating to search for movies in

        self.var_two = StringVar()
        self.var_two.set(0)

        self.search_rbs = [Radiobutton(f2, text = self.default, value = self.default,
                                       variable = self.var_two, fg = "white", font = ("Sans Serif", 10),
                                       padx = 10,bg = "#500178", pady = 10, selectcolor = "#500178",
                                       activebackground = "#500178", activeforeground = "white"),
                           Radiobutton(f2, text = "Unsure", value = "Unsure",
                                       variable = self.var_two, fg = "white", font = ("Sans Serif", 10),
                                       padx = 10,bg = "#500178", pady = 10, selectcolor = "#500178",
                                       activebackground = "#500178", activeforeground = "white")]
        
        for i in range(self.num_radiobuttons):
            self.search_rbs.append(Radiobutton(f2, text = f"{i+1}/5 Stars", value = f"{i+1}/5 Stars",
                                               variable = self.var_two, fg = "white", pady = 10, padx = 10,
                                               font = ("Sans Serif", 10), bg = "#500178", selectcolor = "#500178",
                                               activebackground = "#500178", activeforeground = "white"))
            if i <=3:
                self.search_rbs[i].grid(row = 1, column = i, sticky = NW)
            else:
                self.search_rbs[i].grid(row = 2, column = i-4, sticky = NW)


        #Search Button

        self.searchbtn = Button(f2, text = "Search", bg = "white", fg = "black", font = ("Sans Serif", 10),
                                command = self.get_to_summary_frame)
        self.searchbtn.grid(row = 2, column = 3, sticky = SW)

        f2.grid(column = 0, row = 10)

        self.f3 = Frame(parent)

    #Methods - each correlates to a button

    def saverating(self):
        if self.var.get() != "0":
            self.movie_info[self.i].rating = self.var.get()
    def nextmovie(self):
        if self.i != (len(self.movie_info)-1):
            self.i+=1
        else:
            self.i = 0
        self.var.set(0)
        self.movie_title.configure(text = self.movie_info[self.i].movie)


    def prevmovie(self):
        if self.i !=0:
            self.i-=1
        else:
            self.i = (len(self.movie_info)-1)
        self.var.set(0)
        self.movie_title.configure(text = self.movie_info[self.i].movie)

        
    def get_to_summary_frame(self):
        if self.var_two.get()!= "0":
            if self.summary_rating == self.default:
                self.rating_label.configure(text = "")
            self.summary_rating = self.var_two.get()
        else:
            self.summary_rating = self.default
        self.f1.grid_remove()

        self.summary()


    def summary(self):
        self.f3.configure(bg = "#d4a8ed", padx = 43, pady = 40)
        self.var_two.set(0)
        #Label identifying which rating has been searched for
        self.rating_label = Label(self.f3, text = self.summary_rating, bg = "#d4a8ed", fg = "black",
                                  font = ("Sans Serif", 24))
        self.rating_label.grid(row = 0, column = 1, sticky = NW)

        #Back button to rate more movies

        backbtn = Button(self.f3, text = "Rate more movies", bg = "#801bb3", fg = "white", font = ("Sans Serif", 14),
                         command = self.back_to_rater)
        backbtn.grid(row = 0, column = 0, sticky = NW)

        #Scrolled Text Box of movies under that rating

        self.rated_movie_list = [] #list of movies in that rating
        
        self.rated_movies = ScrolledText(self.f3, wrap = 'word', font = ("Sans Serif", 20), width = 34, height = 10) #Text Box

        for i in range(len(self.movie_info)): #adding movies that have been rated to the list
                if self.movie_info[i].rating == self.summary_rating:
                    self.rated_movie_list.append(self.movie_info[i].movie)
       

        for i in range(len(self.rated_movie_list)):        
            self.rated_movies.insert('1.0', """
""")#each movie on seperate lines
            self.rated_movies.insert('1.0',self.rated_movie_list[i]) #Inserting rated movies into Text Box
        self.rated_movies.configure(state = 'disabled') #Disabling so the box is not typable in
        self.rated_movies.grid(row = 1, column = 0, columnspan = 2)
            
        self.f3.grid(row = 0, column = 0)

    def back_to_rater(self):
        self.f3.grid_remove()
        self.f1.grid(row = 0, column = 0)

                                         
#Main Routine
if __name__=="__main__":
    root= Tk()
    ratings = MovieRaterGUI(root, Movies, "Unrated")
    root.title("Movie Rater")
    root.geometry("483x589+0+0")
    root.mainloop()

