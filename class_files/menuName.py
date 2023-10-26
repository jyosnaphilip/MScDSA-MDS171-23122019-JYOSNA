nameList=[]
def storeName():
    name=input("enter the name to be saved:")
    name=name.strip().title()
    nameList.append(name)
    return name
def listName():
    print("*"*30)
    print("names in the list")
    print("*"*30)
    for name in nameList:
        if len(nameList)==0:
            print("no data available")               #validation
        else:
            print(name)

def searchName(search):
    search=search.strip().title()
    if search in nameList:
        print("name exists in list")
    else:
        print("name not found")

while True:
    print("*"*30)
    print("1.enter a name")
    print("2.list the names")
    print("3.search for a name")
    print("4.exit")
    print("*"*30)
    
    choice=input("your choice?")
    print("you chave entered choice:",choice)

    if int(choice)==1:
        name=storeName()
        print("name {} added succesfully".format(name))
    elif int(choice)==2:
        listName()
    elif int(choice)==3:
        name=input("enter name to be searched:")
        searchName(name)
    elif int(choice)==4:
        exit()
    else:
        print("invalid option...!")  
    