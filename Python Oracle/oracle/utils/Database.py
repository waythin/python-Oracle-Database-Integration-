from utils.Helpers import is_number
import cx_Oracle

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