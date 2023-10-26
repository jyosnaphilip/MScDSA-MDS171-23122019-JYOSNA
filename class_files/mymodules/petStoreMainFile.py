import mypetStore
file=mypetStore.petStore()
def menu(file):
    while True:
        print("1.user")
        print("2.admin")
        print("3.exit)")
        choice=input("enter option:")
        if choice=="1":
            print("1.search pet")
            print("2.see all pets")
            print("3.buy pet")
            choice=input("enter option:")
            if choice=="1":
                search=input("enter animal type or breed:")
                file.searchPet(search.strip().lower())
            elif choice=="2":
                file.listPets()
            elif choice=="3":
                print("contact admin")
            else:
                print("enter a valid option")
        elif choice=="2":
            print("1.add new pet")
            print("2.sell pet")
            adminChoice=input("enter your choice:")
            if adminChoice=="1":
                file.newPet()
            elif adminChoice=="2":
                petType=input("enter type:")
                breed=input("enter breed:")
                age=input("enter age:")
                file.sellPet(petType,breed,age)
            else:
                print("enter valid choice")
        elif choice=="3":
            break
        else: 
            print("invalid choice")


menu(file)

        


