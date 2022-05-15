
from traceback import print_tb
from mcon import curs,mcon
#=========================FUNCTIONS=======================================
# Cutomer related operations

class customer:
    '''customer(name,contact,email) | name = customer name | contact = customer contact number | email = customer email (not compulsory) |'''

    def __init__(self):
        pass

    def add(self,name,contact,email):
        query="Insert into customer (name, contact, email) values('{}',{},'{}')".format(name,contact,email)
        curs.execute(query)
        mcon.commit()
        print("Customer Added Successfuly! \nPlease note Customer ID: ")
        curs.execute(f"select cid from customer where contact = {contact}")
        data = curs.fetchall()
        print(data[0][0])

    def update(self,cname,cid,new):
        '''customer.update(cname,cid,new) | cname = column name | cid = customer id | new = new value'''
        query = f"update customer set {cname} = {new} where cid = {cid}"
        curs.execute(query)
        mcon.commit()
        print("UPDATE SUCCESSFUL!!")

    def delete(self,cid):
        '''customer.update(cid) | cid = customer id '''
        check = self.search(cid)
        if check == 1:
            query = f"delete from customer where cid = {cid}"
            curs.execute(query)
            mcon.commit()
            print("DELETION SUCCESSFUL!!")


    def search(self,cid):
        query = "Select cid from customer"
        curs.execute(query)
        data=curs.fetchall()
        for i in data:
            if i[0]==cid:
                print('RECORD FOUND!!!!!')
                print(i)
                return 1
        else:
            print('CUSTOMER NOT FOUND!!!')
            return 0
