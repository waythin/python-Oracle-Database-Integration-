import tkinter as tk
import tkinter.font as tkFont
from models.Bread import Bread

class AddBread:
    breadName = ""
    calories = ""
    price = ""
    def __init__(self):
        self.root = tk.Tk()
        #setting title
        self.root.title("Add Item")
        #setting window size
        width=526
        height=287
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_692=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=16)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["text"] = "Add New Item"
        GLabel_692.place(x=0,y=10,width=142,height=30)

        self.breadName =tk.Entry(self.root)
        self.breadName["borderwidth"] = "1px"
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.breadName["font"] = ft
        self.breadName["fg"] = "#333333"
        
        self.breadName.place(x=10,y=70,width=505,height=30)

        GLabel_339=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=10)
        GLabel_339["font"] = ft
        GLabel_339["fg"] = "#333333"
        GLabel_339["text"] = "Bread Name"
        GLabel_339.place(x=10,y=40,width=70,height=25)

        GLabel_571=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=10)
        GLabel_571["font"] = ft
        GLabel_571["fg"] = "#333333"
        GLabel_571["text"] = "Calories Per Loaf"
        GLabel_571.place(x=10,y=100,width=96,height=30)

        self.calories =tk.Entry(self.root)
        self.calories ["borderwidth"] = "1px"
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.calories ["font"] = ft
        self.calories ["fg"] = "#333333"
        
        self.calories .place(x=10,y=130,width=504,height=30)

        self.price=tk.Entry(self.root)
        self.price["borderwidth"] = "1px"
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.price["font"] = ft
        self.price["fg"] = "#333333"
        
        self.price.place(x=10,y=190,width=505,height=30)

        GLabel_276=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=10)
        GLabel_276["font"] = ft
        GLabel_276["fg"] = "#333333"
        GLabel_276["text"] = "Loaf Price (in Pence)"
        GLabel_276.place(x=10,y=160,width=117,height=30)

        GButton_805=tk.Button(self.root)
        GButton_805["bg"] = "#efefef"
        ft = tkFont.Font(self.root, family='Times',size=10)
        GButton_805["font"] = ft
        GButton_805["fg"] = "#000000"
        GButton_805["text"] = "Add Item"
        GButton_805.place(x=140,y=240,width=253,height=30)
        GButton_805["command"] = self.GButton_805_command

    def GButton_805_command(self):
        bread = Bread()
        result = bread.add([self.breadName.get(), self.calories.get(), self.price.get()])
        print(result)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    addBreadView = AddBread()
    addBreadView.start()