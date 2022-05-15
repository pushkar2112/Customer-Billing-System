from mcon import curs,mcon

#=========================FUNCTIONS=======================================

def tables():
    curs.execute('show tables')
    data=curs.fetchall()
    return data

def showtable():
    curs.execute('show tables')
    data=curs.fetchall()
    print('The database contains the following tables:')
    for i in data:
        print(str(data.index(i) + 1) + "." + i[0])

def showdata():
    query="select * from {}"
    curs.execute(query.format('inventory'))

    data=curs.fetchall()
    for i in data:
        print(i)

def spdata(st):
    query='select {} from {};'.format(st,'inventory')
    curs.execute(query) 
    data=curs.fetchall()
    for i in data:
        print(i)

#--------------------------------------Search Record---------------------------

def search(co):
    query="select * from inventory"
    curs.execute(query)
    data=curs.fetchall()
    for i in data:
        if i[0]==co:
            print('RECORD FOUND!!!!!')
            print(i)
            return 1
            break
    else:
        print('ENTRY NOT FOUND!!!')
        return 0

#-------------------------------------Add Record----------------------------------

def add():
    i=input("Enter ITEM ID: ")
    n=input("Enter ITEM NAME: ")
    q=int(input("Enter QUANTITY: "))
    p=int(input("Enter PRICE: "))
    query="Insert into inventory values('{}','{}',{},{})".format(i,n,q,p)
    curs.execute(query)
    mcon.commit()

#------------------------------------Update Record----------------------------------

def update(co,v1,v2):
    query='update inventory set {}={} where item_id={}'.format(v1,v2,co)
    curs.execute(query)
    print('UPDATION SUCCESFUL')
    mcon.commit()

def update_item():
    while True:
        co=input('ENTER ID WHOSE ENTRY IS TO BE UPDATED: ')
        if search(co)==1:
            ch=input('ARE YOU SURE YOU WANT TO UPDATE THIS RECORD? [Y/N]  ')
            if ch in ['n','N']:
                print('-------RECORD NOT UPDATED-------')
                break
            else:
                
                v1=input('ENTER COLUMN NAME: ')
                cnm=curs.column_names
                if v1 in cnm:
                    v2=input('ENTER NEW VALUE: ')
                    update(co,v1,v2)
                    c=input('DO YOU WANT TO UPDATE MORE? [Y/N]  ')
                    if c in ['n','N']:
                        break
                    
                else:
                    print('COLUMN NOT FOUND')
                    break
                
        else:
            c=input('DO YOU WANT TO TRY AGAIN? [Y/N]  ')
            if c in['n','N']:
                break

#----------------------------------Delete Record----------------------------------

def delete(co):
    query="delete from inventory where item_id='{}'".format(co)
    curs.execute(query)
    print('DELETION SUCCESFUL')
    mcon.commit()

def del_item():
    while True:
            co=input('ENTER ID WHOSE ENTRY IS TO BE DELETED: ')
            if search(co)==1:
                ch=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD? [Y/N]  ')
                if ch in ['n','N']:
                    print('-------RECORD NOT DELETED-------')
                    break
                else:
                
                    delete(co)
                    c=input('DO YOU WANT TO DELETE MORE? [Y/N]  ')
                    if c in ['n','N']:
                        break
            else:
                c=input('DO YOU WANT TO TRY AGAIN? [Y/N]  ')
                if c in['n','N']:
                    break