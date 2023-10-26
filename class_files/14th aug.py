
Contact={}
def addContact(n,p):
    
    if n in Contact.keys():
        print("contact already exists")
    elif p in Contact.values():
        print("phone no already assigned to a contact")
    else:
        Contact.update({n:p})
        print("Contact added successfully!")

def editContact(n):
    
    if n in Contact.keys():
        print("a. edit name")
        print("b. edit number")
        o=input("enter your choice:")
        if o=="a":
            new_N=input("enter the updated name:")
            new_N=new_N.strip().title()
            Contact.update({new_N:Contact[n]})
            Contact.pop(n)
            print("Contact edited successfully!")
        
        elif o=="b":
            new_P=input("enter updated number:")
            new_P=new_P.strip()
            Contact[n]=new_P
            print("phone number edited successfully")
        else:
            print("invalid entry")
    else:
        print("name doesn't exist!")

def delContact():
    c=input("enter contact name to be deleted:")
    c=c.strip().title()
    print(Contact.keys())
    if c in Contact.keys():
        Contact.pop("n")
        print("contact deleted successfully!")
    else:
        print("name doesnt exist!")

def searchContact():
    print("a.search by name")
    print("b.search by number")
    o=input("enter your choice:")
    if o=="a":
        name=input("enter name:")
        name=name.strip().title()
        if name in Contact.keys():
            print(name,":",Contact[name])
        else:
            print("name doesnt exist")
    elif o=="b":
        p=input("enter phone number:")
        if p in Contact.values():
            print(Contact.get(p))
        else:
            print("number not found!")
    else:
        print("invalid option")
while True:
    print("CONTACTS")
    print("*"*30)
    print("1. add a contact")
    print("2. edit a contact")
    print("3. delete a contact")
    print("4. search a contact")
    print("5.exit")
    print("6. print all contacts")
    option=int(input("enter your option:"))
    if option==1:
        n=input("enter contact name:")
        p=input("enter phone number:")
        n=n.strip().title()
        p=p.strip()
        addContact(n,p)
    elif option==2:
        n=input("enter contact name to be edited:")
        n=n.strip().title()
        editContact(n)
    elif option==3:
        delContact()
    elif option ==4:
        searchContact() 
    elif option==6:
        print(Contact.items())    
    elif option ==5:
        exit()
    else:
        print("not a valid option !")
