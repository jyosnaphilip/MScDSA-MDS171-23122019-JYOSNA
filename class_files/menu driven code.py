
#get details of student name, reg no, phone , email,check if reg no already exists,if exists replace all the details with the new one
#search using reg no and print all the details
studentDetails=[]
keys=["Name","Reg.No","Phone","Email"]

def addDetails():
    x={}
    
    for key in keys:
        
        x[key]=(input("enter "+key)).strip().title()
    for i in studentDetails:
        if i["Reg.No"]==x["Reg.No"]:
            place=studentDetails.index(i)
            studentDetails[place]=x
        else:
            studentDetails.append(x)

def searchDetails(search):
    for detail in studentDetails:
        
        if search in detail.values():
            print("Name:",detail["Name"])
            print("Reg No.",detail["Reg.No"])
            print("Phone:",detail["Phone"])
            print("Email:",detail["Email"])
    else:
        print("reg no not found")

while True:
    print("*"*30)
    print("student details")
    print("*"*30)
    print("1.add a detail")
    print("2.search a detail")
    print("3.exit")
    choice=int(input(("enter your choice:")))
    if choice==1:
        addDetails()
    elif choice==2:
        regNo=input("enter reg no to search:")
        searchDetails(regNo)
    elif choice==3:
        exit()
    else:
       print("invalid entry")

