import random as r
import pickle as p
import os.path as o

def get_all_accounts():
    if o.isfile("Accounts.bat"):            
        read_file=open("Accounts.bat","rb")
        Accounts=p.load(read_file)
        read_file.close()
        return Accounts
    else:
        print("Data Not Available")
        return {}

def display_account(Act):
    print("-"*80)
    print("Holder Name:",Act[0])
    print("Phone:",Act[1])
    print("Address:",Act[2])
    print("Gender:",Act[3])
    print("Password:",Act[4])
    print("Balance:",Act[5])
    print("-"*80)

def write_accounts(Accounts):
    write_file=open("Accounts.bat","wb")
    p.dump(Accounts,write_file)
    write_file.close()

def add_account():
    Accounts=get_all_accounts()
    ac_no=input("Enter Account Number:")
    if ac_no in Accounts.keys():
        print("This Account Number already exists")
        return
    name=input("Enter Account Holder Name:")
    phone=input("Enter Phone Number:")
    address=input("Enter Address:")
    gender=input("Enter gender:")
    password=r.randint(100000,1000000)
    balance=0

    Accounts[ac_no]=[name,phone,address,gender,password,balance]

    write_accounts(Accounts)
    print("Account Has Been Created")
 

def remove_account():
    Accounts=get_all_accounts()
    ac_no=input("Enter Account Number:")
    if ac_no in Accounts.keys():
        del Accounts[ac_no]
        print("Account Has Been Deleted")
        write_accounts(Accounts)
    else:
        print("Account Doesn't Exists")
        

def edit_account():
    Accounts=get_all_accounts()
    ac_no=input("Enter Account Number:")
    if ac_no in Accounts.keys():
        display_account(Accounts[ac_no])
        print("What do you want to change:")
        print("0.Holder Name")
        print("1.Phone")
        print("2.Address")
        print("3.Gender")
        choice=int(input())
        if choice>=0 and choice<4:
            v=input("Enter New Value:")
            if v!="":
                Accounts[ac_no][choice]=v
                write_accounts(Accounts)
                print("Account Has Been Updated")
            else:
                print("Try Again..")
        else:
            print("Wrong Choice")
    else:
        print("Account Doesn't Exists")

def display_all_account():
    Accounts=get_all_accounts()
    print("-"*80)
    print("Account Table".center(80))
    print("-"*80)
    for account in Accounts:
        print(account,Accounts[account])
        


def search_account():
    Accounts=get_all_accounts()
    ac_no=input("Enter Account Number:")
    if ac_no in Accounts.keys():
        display_account(Accounts[ac_no])
    else:
        print("Account Doesn't Exists")



def admin_menu():
    print("-"*80)
    print("Admin Panel".center(80))
    print("-"*80)
    print("1.Add New Account")
    print("2.Remove Account")
    print("3.Edit Account")
    print("4.Display All Accounts")
    print("5.Search Account")
    print("0.Exit")
    
    choice=int(input("Select:"))
    if choice==1:add_account()
    elif choice==2:remove_account()
    elif choice==3:edit_account()
    elif choice==4:display_all_account()
    elif choice==5:search_account()
    elif choice==0:exit()

    input("Continue...")
    admin_menu()

def deposit_cash(act_no):
    Accounts=get_all_accounts()
    amount=int(input("Enter Amount For Deposit:"))
    Accounts[act_no][5]=int(Accounts[act_no][5])+amount
    write_accounts(Accounts)
    print("Amount Deposited")
    

def withdraw_cash(act_no):
    Accounts=get_all_accounts()
    amount=int(input("Enter Amount For Withdraw:"))
    if(Accounts[act_no][5]>amount):
        Accounts[act_no][5]=int(Accounts[act_no][5])-amount
        print("Amount Withdraw.")
        write_accounts(Accounts)
    else:
        print("Can not Withdraw.")

def check_balance(act_no):
    Accounts=get_all_accounts()
    print("Balance:Rs.",Accounts[act_no][5])



def customer_menu(act_no):
    print("-"*80)
    print("Customer Panel".center(80))
    print("-"*80)
    print("1.Deposit Cash")
    print("2.Withdraw Cash")
    print("3.Check Balance")
    print("0.Exit")
    choice=int(input("Select:"))
    if choice==1:deposit_cash(act_no)
    elif choice==2:withdraw_cash(act_no)
    elif choice==3:check_balance(act_no)
    elif choice==0:exit()
    input("Continue...")
    customer_menu(act_no)


def main_menu():
    print("-"*80)
    print("Banking System".center(80))
    print("-"*80)
    print("1.Admin Login\n2.Customer Login")
    choice=int(input("Select:"))
    if choice==1:
        admin_id=input("Enter Admin Id:")
        password=input("Enter Admin Password:")
        if admin_id=="Ishim" and password=="1234":
            admin_menu()
        else:
            print("Id/Password not mateched")
    elif choice==2:
        Accounts=get_all_accounts()
        act_no=input("Enter Account Number:")
        if act_no in Accounts.keys():
            password=int(input("Enter Account Password:"))
            if Accounts[act_no][4]==password:
                customer_menu(act_no)
            else:
                print("Password does not matched")
        else:
            print("Account not available")


main_menu()
