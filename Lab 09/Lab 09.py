class ExpenseTracker:
    def __init__(self):
        self.transact_Dict={"expenses":[],"income":[]}  #initialise dictionary
        with open("expenseTracker.csv","r+") as file:   #open file 
            r=file.readlines()     #r is a list with each line as elemnt
    
    
        for row in r:
            sentence=row.strip().split(",")  #iterate through r, sentence has ech item in a row
        
            if "Amount" in sentence[0]: #to avoid first line
                pass
            else:
                self.storeTransaction(int(sentence[0]),sentence[1],sentence[2],sentence[3]) 

        
   
    def storeTransaction(self,transact,type,date,remark):
        self.transact=transact
        self.type=type
        self.date=date
        self.remark=remark
        self.singleTransact={"Amount":self.transact,"Category":self.type,"Date":self.date,"Remark":self.remark}
        
        if self.transact>0:     #differentiation of expense and income
            (self.transact_Dict["income"]).append(self.singleTransact)
        else:
            (self.transact_Dict["expenses"]).append(self.singleTransact)
        return True
    def viewTransaction(self):   
        print("INCOME")
        for income in self.transact_Dict["income"]:
            print(income)
        print("EXPENSE")
        for expense in self.transact_Dict["expenses"]:
            print(expense)
        
        
    def calcTransaction(self):
        totalExpense=0
        totalIncome=0
        for i in self.transact_Dict["expenses"]:
            totalExpense+=i["Amount"]
        for i in self.transact_Dict["income"]:
            totalIncome+=i["Amount"]
        print("total income:",totalIncome)
        print("total expense:",totalExpense)
        print("savings:",totalIncome+totalExpense)

sendFile=ExpenseTracker()  #object
    

while True:
    print("1.add income/expense")
    print("2.view Transaction")
    print("3.find total income and expense")
    print("4.exit")
    choice=int(input("enter your option:"))  #menu
    if choice ==1:
        trans=int(input("enter transaction, positive if income and negative if expense:"))
        transactType=input("enter the type of transaction:")
        transactDate=input("enter Date:")
        transactRemark=input("enter Remarks, if any. If none, enter '-':")
        sendFile.storeTransaction(trans,transactType,transactDate,transactRemark)

    elif choice==2:
        sendFile.viewTransaction()
    elif choice==3:
        sendFile.calcTransaction()
    elif choice==4:
        exit()
    else:
        print("enter a valid option!")







