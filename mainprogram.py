import dbprogram
try:
    db=dbprogram.Inventory_Management_System()
    while True:
        print("\n\nDashBoard")
        print("1. Add product\n2. view products\n3. update product price & quantity\n4. delete product\n5. search\n6. stock check\n0. Exit")
        ch=int(input("\nEnter choice(0-6) : "))
        if ch==1:
            p_id=int(input("Enter product ID : "))
            pn=input("Entter product name : ")
            c=input("Enter product category : ")
            p=float(input("Enter price : "))
            q=int(input("Enter quantity : "))
            db.add(p_id,pn,c,p,q)
            
        elif ch==2:
            print("\n\n   Product list in the inventory")
            db.view()    
       
        elif ch==3:
            p_id=int(input("Enter product ID : "))
            p=float(input("Enter price :"))
            q=int(input("Enter quantity : "))
            db.edit(p_id,p,q)
            
        
        elif ch==4:
            p_id=int(input("Enter product ID : " ))
            db.remove(p_id)

        elif ch==5:
            k = input("Enter search key: ")
            db.search(k) 

        elif ch==6:
            min_limit = int(input("Enter minimum stock limit: "))
            db.low_stock_alert(min_limit)    

        elif ch==0:
            db.cancel()
            break

        else:
            print("\n Invalid Choice")
        
except Exception as e:
    print("\n Error ~ ",e)

"""
DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 1
Enter product ID : 111
Entter product name : Fenugrreek
Enter product category : Spices
Enter price : 40
Enter quantity : 20
Data added


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 2


   Product list in the inventory
101     Clove   Spices  500.00  20

102     Gram flour      Flour   200.00  10

103     Turmeric        Spices  300.00  25

104     Moong daal      Daal    75.00   50

105     Rice    staple food variety     45.00   200

106     Tomato  vegetables      10.00   30

107     Cinnamon        Spices  150.00  25

108     Mango   Fruits  120.00  20

109     Pepper  Spices  250.00  20

110     Bitter guard    vegetables      45.00   10

111     Fenugrreek      Spices  40.00   20



DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 3
Enter product ID : 110
Enter price :20
Enter quantity : 10
Data updated


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 2


   Product list in the inventory
101     Clove   Spices  500.00  20

102     Gram flour      Flour   200.00  10

103     Turmeric        Spices  300.00  25

104     Moong daal      Daal    75.00   50

105     Rice    staple food variety     45.00   200

106     Tomato  vegetables      10.00   30

107     Cinnamon        Spices  150.00  25

108     Mango   Fruits  120.00  20

109     Pepper  Spices  250.00  20

110     Bitter guard    vegetables      20.00   10

111     Fenugrreek      Spices  40.00   20


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 4
Enter product ID : 110
Deleteion success!


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 2


   Product list in the inventory
101     Clove   Spices  500.00  20

102     Gram flour      Flour   200.00  10

103     Turmeric        Spices  300.00  25

104     Moong daal      Daal    75.00   50

105     Rice    staple food variety     45.00   200

106     Tomato  vegetables      10.00   30

107     Cinnamon        Spices  150.00  25

108     Mango   Fruits  120.00  20

109     Pepper  Spices  250.00  20

111     Fenugrreek      Spices  40.00   20


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 0
App closed!

DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 5
Enter search key: pepper
Search results:
(109, 'Pepper', 'Spices', Decimal('250.00'), 20)


DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 5
Enter search key: cashew nuts
No results found.

DashBoard
1. Add product
2. view products
3. update product price & quantity
4. delete product
5. search
6. stock check
0. Exit

Enter choice(0-6) : 6
Enter minimum stock limit: 20
Low stock alert!
(102, 'Gram flour', 'Flour', Decimal('200.00'), 10)

"""
        


