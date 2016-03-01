import time
import pygame
from tkinter import *
from tkinter.ttk import *

class BubbleSort:

    def __init__(self,canvas,sort_grid):
        self.canvas = canvas
        self.sort_grid = sort_grid
        
        colour_list = []
        for i in range(5):
            fill_colour = canvas.itemcget(sort_grid[(i,0)],"fill")
            if fill_colour == "red":
                colour_list.append(1)
            elif fill_colour == "blue":
                colour_list.append(2)
            else:
                colour_list.append(0)

        for i in range(0,len(colour_list)):
            for j in range(0, len(colour_list)-1):
                if colour_list[j]>colour_list[j+1]:
                    x = colour_list[j]
                    colour_list[j]=colour_list[j+1]
                    colour_list[j+1]=x

                self.fill_square(colour_list[j],j)
                self.fill_square(colour_list[j+1],j+1)
                self.canvas.update_idletasks()
                time.sleep(0.1)

    def fill_square(self,colour,j):
        if colour == 1:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="red")
        elif colour == 2:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="blue")
        else:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="")

class sort_options:

    __instance = 0
    
    def __init__(self):

        self.button_accept = pygame.mixer.Sound("./audio/bgs/menu_confirm_1_dry.wav")
        self.button_deny = pygame.mixer.Sound("./audio/bgs/menu_deny_1_dry.wav")

        #Layout & Window
        if sort_options.__instance > 0: # Prevents more than one overlay opening at anytime.
            pass
        else:
            sort_options.__instance += 1 # Increments private attribute __instance.
            pygame.mixer.Sound.play(self.button_accept)
            
            self.overlay = Toplevel()
            self.overlay.title("Sort Options")
            self.overlay.geometry("500x120")
            self.overlay.wm_iconbitmap("./images/logo.ico")
            self.overlay.protocol("WM_DELETE_WINDOW",self.instance) # Sets event to when window is being closed.

            #Attributes
            self.frame01 = Frame(self.overlay)
            self.frame01.pack(fill=BOTH,pady=10)

            self.frame02 = Frame(self.overlay)
            self.frame02.pack(fill=BOTH,pady=10)

            self.sorting = Label(self.frame01, text="Sort: ",font=("Fixedsys",17))
            self.sorting.pack(side=LEFT, fill=X,expand=True,padx=10)

            var1 = StringVar()
            options = ["Test1", "Test2"]
            self.sort_selection = OptionMenu(self.frame01, var1, *options)
            self.sort_selection.pack(side=LEFT, fill=X,expand=True,padx=10)

            self.speed = Label(self.frame02, text="Speed: ",font=("Fixedsys",17))
            self.speed.pack(side=LEFT, fill=X,expand=True,padx=10)

            self.speed_scale = Scale(self.frame02,from_=-50,to=50,orient=HORIZONTAL)
            self.speed_scale.pack(side=LEFT,fill=X,expand=True,padx=10)
            self.speed_scale.set(0)
            
    def instance(self, event=None):
        pygame.mixer.Sound.play(self.button_deny)
        sort_options.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()
    
