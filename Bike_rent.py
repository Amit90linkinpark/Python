from pickle import TRUE


class Bike():
    def __init__(self):
        self.commuter_bike=["Activa","Splendor","pulsar 150"]
        self.adventure_bike=["himalayan","duke 390 adventure","yeszi adventure","triumph tiger 1200","bmw gs 1250"]
        self.race_bike=["R15","R1","RS200","RC390","panigale v4","Zx10r"]
        self.sports_naked_bike=["NS200","Duke390","Z900","MT15"]
        self.cruiser_bike=["classic 350","CB 350RS","FatBoy"]
    def show_all_bike(self):
        print("Welcome To Amit Bike Rental Service")
        print("Press 1 to show Commuter Bike")
        print("Press 2 to show Adventure Bike")
        print("Press 3 to show Raceing Bike")
        print("Press 4 to show Sport Naked Bike")
        print("Press 5 to Show Cruiser Bike")
        user_input=int(input("Please Enter your option Here= "))
        if(user_input == 1):
            print(self.commuter_bike)
            self.a=self.commuter_bike
        elif(user_input == 2):
            print(self.adventure_bike)
            self.a=self.adventure_bike
        elif(user_input == 3):
            print(self.race_bike)
            self.a=self.race_bike
        elif(user_input == 4):
            print(self.sports_naked_bike)
            self.a=self.sports_naked_bike
        elif(user_input == 5):
            print(self.cruiser_bike)
            self.a=self.cruiser_bike
        else:
            print("Invalit Options")
        
class User(Bike):
    def __init__(self,name,address,phnumber):
        super().__init__()
        self.name=name
        self.address=address
        self.phnumber=phnumber
        self.user_have_bike=0
        
    def show_bike(self):
        print(f"Hi {self.name}")
        self.show_all_bike()
    def rent_bike(self):
        if (self.user_have_bike == 0):
            print(f"Hi {self.name} what kind of bike do you want to rent")
            self.show_all_bike()
            user_want_bike=input("Enter a Bike name you want to rent : ")
            if user_want_bike in self.a:
                print("How long Do you want Bike")
                print("Press 1 to just one days")
                print("Press 2 to just one week")
                print("Press 3 to just 1 year")
                self.user_want_time=int(input("Enter you option here : "))
                if(self.user_want_time == 1 or self.user_want_time == 2 or self.user_want_time == 3):
                    self.a.remove(user_want_bike)
                    self.user_have_bike=user_want_bike
                    print("Thank you")
                else:
                    print("Please Enter valied number")
            else:
                print("Please Enter Right bike name or I don't have those bike")
        else:
            print(f"Hi {self.name} you already have {self.user_have_bike} Bike")
    
    def return_bike(self):
        print(f"Hi {self.name} you  have {self.user_have_bike} bike")
        user_input_two=int(input("Do you want to return bike press 1 to YES and Press 2 to NO= "))
        if(user_input_two == 1):
            print("Thnq for using our bike")
            if(self.user_want_time == 1):
                print("You 1 day service package is over")
                print(f"Your ammount is 800/- only")
                self.a.append(self.user_have_bike)
                self.user_have_bike=0
            elif(self.user_want_time == 2):
                print("You 1 week service package is over")
                print(f"Your ammount is 1800/- only")
                self.a.append(self.user_have_bike)
                self.user_have_bike=0
            elif(self.user_want_time == 3):
                print("You 1 year service package is over")
                print(f"Your ammount is 18000/- only")
                self.a.append(self.user_have_bike)
                self.user_have_bike=0
        elif(user_input_two == 2):
            print("Enjoy your bike ride")
        else:
            print("Please Enter valied input")

if __name__ == "__main__":
    print("Welcome To Amit Bike Rent Service (ABS)")
    amit=User("Amit","Champasari",6541254)
    while(True):
        print("#########################################")
        print("Enter 1 to show All Bike")
        print("Enter 2 to rent Bike")
        print("Enter 3 to return Bike")
        print("Enter 4 to exit")
        user_input_three=int(input("Enter your option here= "))
        if(user_input_three == 1):
            amit.show_bike()
        elif(user_input_three == 2):
            amit.rent_bike()
        elif(user_input_three == 3):
            amit.return_bike()
        elif(user_input_three == 4):
            break
        else:
            print("Enter valid options please")

    

