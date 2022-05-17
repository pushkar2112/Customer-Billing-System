#-------------------------IMPORTING MODULES-------------------------------
from billing import generate
from customer import customer
from mcon import mcon,curs
import time
import inventory, mysql.connector
    

#-------------------------MAIN MENU---------------------------------------

admin_ch=None
while True:
    print('''
------------------ADMIN MENU--------------

1) Customer Management
2) Inventory Management
3) Billing
''')

    admin_ch=int(input('ENTER YOUR CHOICE: '))
    if admin_ch == 1:
        ch = None
        while True:
            print('''
----------------------Customer Management-----------------

1) Add Customer
2) Update Customer Record
3) Search Customer
4) Delete Customer Record
''')
            cust = customer()
            ch=int(input('ENTER YOUR CHOICE: '))
            
            if ch == 1:
                n = input("Enter Name: ")
                c = int(input("Enter Contact Number: "))
                e = input("Enter E-mail: ")

                cust.add(n,c,e)

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

            elif ch == 2:
                cname = input("Enter Atribute Name: ")
                cid = input("Enter Customer ID: ")
                new = input("Enter New Value: ")

                cust.update(cname,cid,new)

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

            elif ch == 3:
                cid = input("Enter Customer ID: ")
                cust.search(cid)

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

            elif ch == 4:
                cid = input("Enter Customer ID: ")
                print("ARE YOU SURE YOU WANT TO DELETE RECORD ? [Y/N]")
                choice = input().lower()
                if choice == "y":
                    cust.delete()

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

            #----------------------------------INVALID CHOICE-----------------------------
            else:
                print('SELECT A VALID OPTION!!!')

            

    elif admin_ch == 2:
        ch = None
        while True:
            print('''---------------------------------------------------
                    MAIN MENU
---------------------------------------------------
1)SHOW ALL RECORDS
2)SHOW ALL RECORDS(SPECIFIC COLUMNS)
3)SEARCH RECORD
4)ADD ENTRY
5)DELETE ENTRY
6)UPDATE ENTRY
---------------------------------------------------''')
            ch=int(input('ENTER YOUR CHOICE: '))

        #----------------------------------SHOW ALL RECORDS-------------------------

            if ch==1:        
                inventory.showdata()
                
                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

        #-----------------------------SHOW SPECIFIC COLUMNS--------------------------

            if ch==2:                                   
                print('COLUMN NAMES: ')
                curs.execute("select * from inventory")
                cnm=curs.column_names
                for i in cnm:
                    print(i)
                cno=int(input('HOW MANY COLUMNS DO YOU WANT TO SELECT: '))
                sample=[]
                for i in range(cno):
                    nm=input('ENTER COLUMN NAME: ')
                    sample.append(nm)
                
                st=''
                for i in sample:
                    st+=i
                    st+=','
                inventory.spdata(st[:-1])
                
                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

        #-----------------------------SEARCH RECORD----------------------------------

            if ch==3:
                co=input("Enter the item id which you want to search: ")
                inventory.search(co)

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break
        #----------------------------NEW ENTRY----------------------------------------
            if ch==4:
                inventory.add()

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

        #------------------------------------DELETE ENTRY----------------------------------------
            if ch==5:
                inventory.del_item()

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break

        #----------------------------UPDATE ENTRY---------------------------------------

            if ch==6:
                try:
                    inventory.update_item()
                except mysql.connector.errors.ProgrammingError:
                    print("\nAn error occured while processing that request! Please try again!")

                inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
                if inc in ['n','N']:
                    break
        #----------------------------------INVALID CHOICE-----------------------------
            else:
                print('SELECT A VALID OPTION!!!')

    elif admin_ch == 3:
        #------------Billing------------
        cid = input("Enter Customer ID: ")
        generate(cid)

#-----------------------------INVALID CHOICE-----------------------------------------
        
    else:
        print('SELECT A VALID OPTION!!!')
        
#-----------------------------------------------END---------------------------------------------------------

time.sleep(200)    
        
         























        
        
