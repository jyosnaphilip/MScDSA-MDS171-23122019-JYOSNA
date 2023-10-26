
class sportMart:
    def __init__(self):
        self.inventory={}
        self.customerOrders={}
  
    def createInventory(self,ItemID,Item,Quantity,UnitPrice):
        temp={"Itemid":ItemID,"product Name":Item,"Quantity":Quantity,"Price":UnitPrice}
        self.inventory[ItemID]=temp
    
    def createOrder(self,OrderId,ProductID,Quantity,price,total):
        temp={"order id":OrderId,"productid":ProductID,"quantity":Quantity,"Price":price,"total":total}
        self.customerOrders[OrderId]=temp
    
    def printOrders(self):
        print("order id\tproductid\tquantity\tprice\ttotal")
        for orderid in self.customerOrders.keys():
            for order_detail in self.customerOrders[orderid]:
                print(self.customerOrders[orderid][order_detail],end="\t\t")
            print("")

    def printInventory(self):
        print("ItemID\tItem\tQuantity\tUnitPrice")
        for productid in self.inventory.keys():
            for prod_detail in self.inventory[productid]:
                print(self.inventory[productid][prod_detail],end="\t\t")
            print("")

    def getPrice(self,itemID):
        if itemID in self.inventory.keys():
            return int(self.inventory[itemID]["Price"])
        else:
            print("item ID not found")
            return 0
        
    def addOrder(self,orderID,dict):
        self.customerOrders[orderID]=dict
        print("Order added successfully")

    def editInventory(self,itemID,quantity):
        if itemID in self.inventory.keys():
            self.inventory[itemID]["Quantity"]=str(int(self.inventory[itemID]["Quantity"])-quantity)
            print("inventory edited succesfully")
        else:
            print("item id not found")
    
    def rewriteFiles(self):
        with open("mymodules\inventory.csv","w+") as in_file:
            in_file.write("ItemID,Item,Quantity,UnitPrice\n")
            for prodID in self.inventory.keys():
                line=str(prodID)+","+str(self.inventory[prodID]["product Name"])+","+str(self.inventory[prodID]["Quantity"])+","+str(self.inventory[prodID]["Price"])
                in_file.write(line+"\n")

        with open("mymodules\orderhistory.csv","w+") as o_file:
            o_file.write("OrderId,ProductID,Quantity,price,total\n")
            for ordID in self.customerOrders.keys():
                line=str(ordID)+","+str(self.customerOrders[ordID]["productid"])+","+str(self.customerOrders[ordID]["quantity"])+","+str(self.customerOrders[ordID]["Price"])+","+str(self.customerOrders[ordID]["total"])
                o_file.write(line+"\n")

    def getOrderID(self):
        import random
        orderid="OD"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        return orderid

#object
trinity=sportMart()
with open("mymodules\orderhistory.csv","r+") as orders:
    o_header=orders.readline()
    o_data=orders.readlines()

for data in o_data:
    tmp=data.strip().split(",")
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

trinity.printOrders()

with open("mymodules\inventory.csv","r+") as inventory:
    i_header=inventory.readline()
    i_data=inventory.readlines()

for data in i_data:
    tmp=data.strip().split(",")
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printInventory()

while True:
    print("1.Add order")
    print("2.Exit")
    u_choice=input("enter your choice:")
    if u_choice=="1":
        OrderId=trinity.getOrderID()
        ProductID=input("enter prod_id:")
        price=trinity.getPrice(ProductID)
        if price==0:
            pass
        else:
            Quantity=int(input("enter quantity:"))
            total=price*Quantity
            order_dict={"order id":OrderId,"productid":ProductID,"quantity":Quantity,"Price":price,"total":total}
            trinity.addOrder(OrderId,order_dict)
            trinity.editInventory(ProductID,Quantity)

    elif u_choice=="2":
        trinity.rewriteFiles()
        break
    else:
        print("enter valid choice")










    

                


    


