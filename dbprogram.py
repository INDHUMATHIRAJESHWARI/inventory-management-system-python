import pymysql
class Inventory_Management_System:
    def __init__(self):
        self.connection=pymysql.connect(host='localhost',user='root',password='Indhu',database='my_db')
        print("Connection to the Database sucess!")
    def add(self,p_id,pn,c,p,q):
        q="insert into inventory(product_ID,product_Name,category,price,quantity) values({0},'{1}','{2}',{3},{4})".format(p_id,pn,c,p,q)
        cursor=self.connection.cursor()
        c=cursor.execute(q)
        self.connection.commit()
        cursor.close()
        print("Data added" if c!=0 else "Failed")
    def edit(self,p_id,p,q):
        q="update inventory set price={0},quantity={1} where product_ID={2}".format(p,q,p_id)
        cursor=self.connection.cursor()
        c=cursor.execute(q)
        self.connection.commit()
        cursor.close()
        print("Data updated" if c!=0 else "Failed")
    def view(self):
        q="select * from inventory"
        cursor=self.connection.cursor()
        cursor.execute(q)
        r=cursor.fetchall()
        for i in r:
            for j in i:
                print(j,end='\t')
            print("\n")
        self.connection.commit()
        cursor.close()
    def remove(self,p_id):
        q=f"delete from inventory where product_ID={p_id}"
        cursor=self.connection.cursor()
        c=cursor.execute(q)
        self.connection.commit()
        cursor.close()
        print("Deleteion success!" if c!=0 else "Failed")
    def search(self,search_key):
        q=f"SELECT * FROM inventory WHERE product_Name LIKE '%{search_key}%'"
        cursor = self.connection.cursor()
        c=cursor.execute(q)
        if c!=0:
            results = cursor.fetchall()
            print("Search results:")
            for row in results:
             print(row)
        else:
            print("No results found.")
        self.connection.commit()
        cursor.close()
    def low_stock_alert(self,min_limit):
        q=f"SELECT * FROM inventory WHERE quantity < {min_limit}"
        cursor = self.connection.cursor()
        c=cursor.execute(q)
        if c!=0:
            results = cursor.fetchall()
            print("Low stock alert!")
            for row in results:
              print(row)
        self.connection.commit()
        cursor.close()
    def cancel(self):
        print("App closed!")
        self.connection.close()