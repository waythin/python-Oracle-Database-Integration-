import tkinter as tk
import tkinter.font as tkFont
from models.Order import Order

class OrderQuantity:
    def __init__(self):
        self.root = tk.Tk()
        #setting title
        self.root.title("undefined")
        #setting window size
        width=545
        height=170
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_303=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=18)
        GLabel_303["font"] = ft
        GLabel_303["fg"] = "#333333"
        GLabel_303["justify"] = "center"
        GLabel_303["text"] = "Find Order Price"
        GLabel_303.place(x=190,y=10,width=160,height=30)

        self.bread_id=tk.Entry(self.root)
        self.bread_id["borderwidth"] = "1px"
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.bread_id["font"] = ft
        self.bread_id["fg"] = "#333333"
        self.bread_id["justify"] = "left"
        self.bread_id.place(x=30,y=80,width=372,height=39)

        GButton_428=tk.Button(self.root)
        GButton_428["bg"] = "#a71010"
        ft = tkFont.Font(self.root, family='Times',size=16)
        GButton_428["font"] = ft
        GButton_428["fg"] = "#ffffff"
        GButton_428["justify"] = "center"
        GButton_428["text"] = "Find"
        GButton_428.place(x=410,y=80,width=105,height=39)
        GButton_428["command"] = self.GButton_428_command

        self.result_view=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.result_view["font"] = ft
        self.result_view["fg"] = "#333333"
        self.result_view["justify"] = "left"
        self.result_view["text"] = ""
        self.result_view.place(x=30,y=130,width=300,height=25)

        GLabel_631=tk.Label(self.root)
        ft = tkFont.Font(self.root, family='Times',size=10)
        GLabel_631["font"] = ft
        GLabel_631["fg"] = "#333333"
        GLabel_631["text"] = "Find order by id"
        GLabel_631.place(x=30,y=50,width=116,height=30)

    def GButton_428_command(self):
        id = self.bread_id.get()
        order = Order()
        order_n = len(order.find(value=id, column="BREADID"))
        self.result_view["text"] = "Number of orders: "+str(order_n)

        
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":    
    app = OrderQuantity()
    app.start()
