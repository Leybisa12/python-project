#Dominos clone
import random
class Dominos:
# DATA    
    menu={
        'veg':{'margerita':129,'cheese_and_corn':169,'peppi_panner':260,'veg_loaded':210,'tomato_tangi':170},
        'non-veg':{'pepper_barbeque':199,'non_veg_loaded':169,'chicken_sausage':200},
        'snacks':{'garlic_bread':120,'zingy':59,'chicken_cheese_balls':170},
        'deserts':{'choco_lava':100,'mousse cake':169},
        'drinks':{'coke':90,'pepsi':78,'sprite':50}
    }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #  TO VALIDATE LOGIN STATE
        self.cart={} # TO STORE ORDERS

        # MAIN PROGRAM

        while True:
            if not self.login_status:
               print("------ WELCOME TO DOMINOS 🍕 APP------")
               print("login")
               ch=input("Do you want to login? (y/n): ")
               if ch=='y' or 'Y':
                    self.login()
            if self.login_status:    
                print("-----------------")
                print("User👤 : ",self.name)
                print("Enter 1: order ")        
                print("Enter 2:Show Cart")
                print("Enter 3:Logout")
                choice=int(input("Enter choise: "))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice")
    @staticmethod   
    def validate_otp(value):
        while True:
            og_otp=random.randint(1000,9999)      
            print(f"An otp has been sent to {value}")
            print(f"your dominos otp is:{og_otp}")   
            otp=int(input("enter otp: "))
            if otp==og_otp:
                print("Login successful✅")
                return True
            print("Incorrect otp enter correct otp..")
            
    def login(self):
        print("Enter 1: Login with Phone")
        print("Enter 2: Login with Email")
        ch=int(input("enter choice: "))
        if ch==1:
            # PHONE NO VALIDATION
            phno=int(input("enter phno: "))
            if phno==self.phno:
                state=self.validate_otp(phno)#True
                self.login_status=state
                #print("generate OTP..")
            else:
                print("incorrect phno")

        elif ch==2:
            # EMAIL VALIDATION
            email=input("enter email: ")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
                #print("generate OTP..")
            else:
                print("incorrect email")    
        else:
            print("Invalid validation")
    def order(self):
        print("-------Dominos Menu---------")
        for category in Dominos.menu:
            print(category)
        cat=input("Enter category: ")
        if cat in Dominos.menu:
            d= Dominos.menu[cat]
            for item in d:  #Display items of respective category
                print(item,'               Rs.',d[item])
            item=input("Enter item: ")
            if item in d:  
                q=int(input("enter quantity:"))
                if item in self.cart:
                    self.cart[item]+=d[item]*q #var[key]=new value
                else:
                    self.cart[item]=d[item]*q    
                print(f"{item} added to the cart🛒")   
                
            else:
                print(f'{item} is not available❌')    

        else:
            print(f'{cat} is not available❌')        

    def show_cart(self):
        print("--------Dominos Cart🛒")
        if self.cart!={}:
            total_bill=0
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,'------------Rs.',self.cart[item])
            print("Total Bill:...Rs. ",total_bill)    
        else:
           print("Cart is Empty please order..")
        if self.cart!={}:
            ch=input("Do you want to place order? (y/n):").lower
            if ch=='y':
                print("Thank you👍 for placing the order..") 
                print("your order is on the way 🛵")
                self.cart={}   
            
        print("Thank you for placing the order...")

    def logout(self):
        ch=input("Do you want to Logout? (y/n):").lower()
        if ch=='y':
            self.login_status=False
            print("Logged out✅")
ob=Dominos('leybisa','ley@gmail.com',9932218182)
