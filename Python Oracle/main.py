import tkinter as tk
import tkinter.font as tkFont
from views.AddBread import *
from views.OrderPrice import OrderPrice
from views.OrderQuantity import OrderQuantity

class App:
    def __init__(self, root):
        #setting title
        root.title("Bread Store")
        #setting window size
        width=510
        height=162
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        add_bread=tk.Button(root)
        add_bread["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        add_bread["font"] = ft
        add_bread["fg"] = "#000000"
        add_bread["justify"] = "center"
        add_bread["text"] = "Add Bread"
        add_bread.place(x=40,y=90,width=116,height=45)
        add_bread["command"] = self.add_bread_command

        order_price=tk.Button(root)
        order_price["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        order_price["font"] = ft
        order_price["fg"] = "#000000"
        order_price["justify"] = "center"
        order_price["text"] = "Order Price"
        order_price.place(x=200,y=90,width=117,height=44)
        order_price["command"] = self.order_price_command

        total_orders=tk.Button(root)
        total_orders["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        total_orders["font"] = ft
        total_orders["fg"] = "#000000"
        total_orders["justify"] = "center"
        total_orders["text"] = "Total Orders"
        total_orders.place(x=360,y=90,width=114,height=44)
        total_orders["command"] = self.total_orders_command

        greeting=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        greeting["font"] = ft
        greeting["fg"] = "#333333"
        greeting["justify"] = "center"
        greeting["text"] = "Bread Buy & Sell"
        greeting.place(x=150,y=20,width=199,height=49)

    def add_bread_command(self):
        # add_bread_view.root.mainloop()
        add_bread_view = AddBread()
        add_bread_view.start()


    def order_price_command(self):
        order_price_view = OrderPrice()
        order_price_view.start()


    def total_orders_command(self):
        order_quantity_view = OrderQuantity()
        order_quantity_view.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
