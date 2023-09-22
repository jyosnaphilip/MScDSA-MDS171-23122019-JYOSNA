class ExpenseTracker:
    def __init__(self):
        self.transact_Dict={"expenses":[],"income":[]}
        with open("ExpenseTracker.csv","r+") as file:
            r=file.readlines()
    
    
        for row in r:
            sentence=row.strip().split(",")
        
            if "Amount" in sentence[0]:
                pass
            else:
                self.storeTransaction(int(sentence[0]),sentence[1],sentence[2],sentence[3]) 

        
   
    def storeTransaction(self,transact,type,date,remark):
        self.transact=transact
        self.type=type
        self.date=date
        self.remark=remark
        self.singleTransact={"Amount":self.transact,"Category":self.type,"Date":self.date,"Remark":self.remark}
        
        if self.transact>0:
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
    

    


