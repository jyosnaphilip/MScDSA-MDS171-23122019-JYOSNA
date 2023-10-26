#create a petstore class where you have the detailes of pets available and their details 
# the class will have methods
# -store a new pet details
# -search for a pet
# -sell a Pet
#-list all the pets
#importing your petstore class ,create a petstoremain file,when you will implement a menu driven program,for admin 
#who will manage the store and user who will see the pets and buy the pets.

class petStore:
    def __init__(self):
        self.petDetails=[
            {"type":"dog","breed":"labrador","age":"2 years","price":"Rs 10,000","status":"available"},
            {"type":"cat","breed":"sphinx","age":"1 years","price":"rs 50,000","status":"available"}
            ]
    
    def newPet(self):
        petType=input("enter animal type:")
        breed=input("enter breed:")
        age=input("enter age (years/months):")
        price=input("enter price of animal(in rupees):")
        petDict={"type":petType,"breed":breed,"age":age,"price":price,"status":"available"}
        self.petDetails.append(petDict)
    
    def searchPet(self,petType):
        for pet in self.petDetails:
            if petType in pet.values():
                for item in pet.items():
                    print(item)

    def sellPet(self,type,breed,age):
        for pet in self.petDetails:
            if type and breed and age in pet.values():
                print(pet)
                confirm=input(print("change status to sold? type y for yes and n for no"))
                if confirm.strip().lower()=="y":
                    pet["status"]="sold"
                    print("pet sold")
                    break
                else:
                    break
            else:
                pass
    def listPets(self):
        for pet in self.petDetails:
            for item in pet:
                print(item,":",pet[item],end="\t")
            print("")
    










        

