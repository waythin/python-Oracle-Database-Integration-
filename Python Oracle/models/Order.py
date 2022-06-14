from utils.Database import Database

class Order(Database):
    def __init__(self):
        self.columns = ["ORDERID", "ORDERMADEDATETIME", "ORDERCOMPLETIONDATETIME", "PRICEINEURO", "STOREID", "BREADID", "MENUITEMID", "CUSTOMERID", "COMPLETION_MARK"]
        self.table_name = "ORDERPLACE"
        super().__init__(self.columns, self.table_name)