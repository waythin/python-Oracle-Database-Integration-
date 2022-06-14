import tkinter as tk
import tkinter.font as tkFont
import cx_Oracle

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
class Database:
    def __init__(self, columns, table_name):
        self.user="sys",
        self.password="oracle",
        self.dsn="localhost:1521/orcl"
        self.connection = None
        self.columns = columns
        self.table_name = table_name

        self.connection = cx_Oracle.connect(
                        user="sys",
                        password="oracle",
                        dsn="localhost:1521/orcl",
                        encoding="UTF-8",
                        mode=cx_Oracle.SYSDBA)

    def read(self):
        datas = []
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        for row in res:
            datas.append(row)
        return datas
    
    def read_orderBy(self, orderBy, order="ASC", limit="", offset=0):
        datas = []
        query = f"SELECT * FROM {self.table_name} ORDER BY {orderBy} {order} OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY"
        query.strip()
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        for row in res:
            datas.append(row)
        return datas
    def find(self, value, column=None, items="*"):
        datas = []
        if column == None:
            column = self.columns[0]
        query = f"SELECT {items} FROM {self.table_name} WHERE {column}='{value}'"
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        for row in res:
            datas.append(row)
        return datas
    def readById( self, id ):
        query = f"SELECT * FROM {self.table_name} WHERE id={id}"
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        return res
    
        
    def create(self, values):
        if len(values) != len(self.columns):
            return {"error": "No. of entry doesn't match with number of columns "}
        msg = True
        columns_str = ""
        value_str = ""

        for col in self.columns:
            columns_str += col+','

        columns_str = columns_str[:-1]
        for val in values:
            if is_number(val):
                value_str += val+","
            else:
                value_str += f"'{val}',"
        value_str = value_str[:-1]
        query = f"INSERT INTO {self.table_name} ({columns_str}) VALUES ({value_str})"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

        if cursor.rowcount == 0: 
            msg = False
            return { 'msg': msg, 'query': query }
        
        return msg

    def delete(self, ids):
        ids_str = "";
        msg = True;
        for id in ids:
            ids_str += id+","
        ids_str = ids_str[:-1]
        query = f"DELETE FROM {self.table_name} WHERE id IN ({ids_str})"
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        if not res: 
            msg = False
            return { 'msg': msg, 'query': query}        
        return msg  
class Order(Database):
    def __init__(self):
        self.columns = ["ORDERID", "ORDERMADEDATETIME", "ORDERCOMPLETIONDATETIME", "PRICEINEURO", "STOREID", "BREADID", "MENUITEMID", "CUSTOMERID", "COMPLETION_MARK"]
        self.table_name = "ORDERPLACE"
        super().__init__(self.columns, self.table_name)
class Bread(Database):
    def __init__(self):
        self.columns = ["BREADID", "BREADTYPE", "PRICEPERLOAF", "CALORIESPERBREAD"]
        self.table_name = "Bread"
        super().__init__(self.columns, self.table_name)
    
    def add(self, values):
        val = super().find(values[0], "BREADTYPE")
        if len(val) == 0:
            datas = super().read_orderBy("BREADID", "DESC", "1")
            index = str(datas[0][0]+1)
            values = [index] + values
            return super().create(values)
        else:
            return False   
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

class OrderPrice:
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

        self.order_id=tk.Entry(self.root)
        self.order_id["borderwidth"] = "1px"
        ft = tkFont.Font(self.root, family='Times',size=10)
        self.order_id["font"] = ft
        self.order_id["fg"] = "#333333"
        self.order_id["justify"] = "left"
        self.order_id.place(x=30,y=80,width=372,height=39)

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
        id = self.order_id.get()
        order = Order()
        price = order.find(value=id, items="PRICEINEURO")
        if len(price) == 0:
            self.result_view["text"] = "Incorrect order ID"
        else:
            self.result_view["text"] = "Order price: "+str(price[0][0])
    def start(self):
        self.root.mainloop()

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

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
