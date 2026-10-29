Balance=20000
Atm_pin=9392
history={}
count=0
phone_number=9392165961
def withdraw():
    global Balance,Atm_pin,count
    pin=int(input("enter your PIN:"))
    if pin==Atm_pin:
        withdraw=int(input("enter your Amount:"))
        if withdraw%100==0:
            if withdraw<=Balance:
                Balance-=withdraw
                count+=1
                history[count]=(f"withdraw:{withdraw}|Balance:{Balance}")
                print("withdraw successfull")
                print("-------------------")
                choice()
            else:
                print("Insufficient Balance")
                print("--------------------")
                choice()
        else:
            print("it's an ATM u dont get any type of coins here")
            withdraw()
    else:
        withdraw()
def Deposite():
    global Balance,Atm_pin,count
    Deposite=int(input("enter money to be deposited:"))
    a=int(input("Enter Number Of 100rs Notes:"))
    b=int(input("Enter Number of 200rs Notes:"))
    c=int(input("Enter Number Of 500rs Notes:"))
    Total_notes=(a*100)+(b*200)+(c*500)
    if Deposite==Total_notes:
        pin=int(input("Enter The pin:"))
        if pin==Atm_pin:
            if Deposite>=1000:
                Balance+=Deposite
                count+=1
                history[count]=(f"Deposite:{Deposite}|Balance:{Balance}")
                print("Your money as been successfully deposited")
                print("-----------------------")
                choice()
            else:
                print("Add Minimum 1000")
                print("-------------------")
                Deposite()
        else:
            print("please Enter The Valid PIN")
            print("------------------------")
            Deposite()
    else:
        print("please check The Number Of Given Notes")
        print("----------------------------")
        Deposite()
def check_Balance():
    global Balance,Atm_pin
    pin=int(input("Enter Your PIN:"))
    if pin==Atm_pin:
        print(f"your Account Balance is:{Balance}")
        print("---------------------------")
        choice()
    else:
        print("please Enter The Valid PIN")
        print("------------------------")
        check_Balance()
def transaction_history():
    print("\n===================TRANSACTION HISTORY==============")
    if count==0:
        print("No Transaction Yet")
    else:
        number=1
        while number<=count:
            print(history[number])
            number+=1
            print("==============================================")
            choice()
def Pin_change():
    global Atm_pin
    old_pin=int(input("Enter your old pin:"))
    if old_pin==Atm_pin:
        new_pin=int(input("Enter you New pin:"))
        conformation_pin=int(input("conformation pin:"))
        if new_pin==conformation_pin:
            Atm_pin=new_pin
            print("your pin has been updated successfully")
            print("--------------------------------")
            choice()
        else:
            print("/n-----------------------------")
            print("please check your conformation pin")
            print("------------------------------")
            Pin_change()
    else:
        print("/n-----------------------------------")
        print("you Entered Wrong Pin")
        print("please check your Old Pin")
        print("------------------------------------")
        Pin_change()
def Card_less_deposite():
    global Balance,count,phone_number
    Card_less_deposite=int(input("Enter money to be deposited:"))
    a=int(input("Enter Number Of 100rs Notes:"))
    b=int(input("Enter Number Of 200rs Notes:"))
    c=int(input("Enter Number Of 500rs Notes:"))
    Total_notes=(a*100)+(b*200)+(c*500)
    if Card_less_deposite==Total_notes:
        pin=int(input("Enter the pin:"))
        phone_number=int(input("Enter your phone number:"))
        if phone_number==phone_number:
            if Card_less_deposite>=1000:
                Balance+=Card_less_deposite
                count+=1
                history[count]=(f"Card_less_deposite:{Card_less_deposite}|Balance:{Balance}")
                print("your money as been successfully deposited")
                print("-----------------------------------")
                choice()
            else:
                print("Add Minimum 1000")
                print("---------------------------")
                Card_less_deposite()
        else:
            print("Enter the phone number which is connected with this bank account")
            Card_less_deposite()
    else:
        print("please enter the valid PIN")
        print("------------------------------")
        Card_less_deposite()
def exit():
        print("please Remove Your Card")
        print("--------------------------------")
        print("Thankyou For Choosing Our Bank")
def choice():
        print("\n===========================ATM=======================")
        print("\nAutomated Teller Machine")
        print("Choose 1 for Withdraw")
        print("Choose 2 for Deposite")
        print("Choose 3 for check Balance")
        print("choose 4 for Transaction History")
        print("Choose 5 for pin_change")
        print("Choose 6 for Card less deposite")
        print("Choose 7 for Exit")
        print("\n--------------------------\n")
        choices=int(input("Enter your choice:"))
        if choices==1:
            withdraw()
        elif choices==2:
            Deposite()
        elif choices==3:
            check_Balance()
        elif choices==4:
            transaction_history()
        elif choices==5:
            Pin_change()
        elif choices==6:
            Card_less_deposite()
        elif choices==7:
            exit()
        else:
            print("Please Enter Valid Option")
            print("---------------------------------")
            choice()
def insert_your_atm():
    global atm 
    print("\n please insert your ATM card")
    print("-----------------------------")
    atm_Card=input("Do you inserted your ATM card:")
    if atm_Card=="yes" or atm_Card=="yes":
        print("\n=============KONE RAJU================")
        choice()
    else:
        print("Then Keep It:")
        insert_your_atm()
if __name__ =="__main__":
    insert_your_atm()





    

