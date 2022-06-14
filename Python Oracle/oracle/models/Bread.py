from utils.Database import Database
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
        