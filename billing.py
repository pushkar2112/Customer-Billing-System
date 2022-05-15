from mcon import curs,mcon
from datetime import date, datetime
import inventory, os
#=========================FUNCTIONS=======================================

billed = {}
billed_amt = {}
total = 0
dpath = "bills"
#bill_id

def add_items():
    curs.execute("select item_id from inventory")
    data = curs.fetchall()

    
    iid = input("Enter Item ID: ")

    found = inventory.search(iid)

    if found == 0:
        return 0

    while True:
        qty = int(input("Enter Quantity: "))
        curs.execute(f"select quantity from inventory where item_id = {iid}")
        data = curs.fetchall()
        if data[0][0] >= qty:
            break
        else:
            print("INSUFFICIENT INVENTORY!! Available - {}".format(data[0]))


    billed[iid] = qty

    curs.execute(f"select price from inventory where item_id = {iid}")
    data = curs.fetchall()

    price = int(data[0][0]) * qty

    billed_amt[iid] = [qty,price]
    


def settle(billed, billed_amt):
    global total

    for key,value in billed.items():
        query = f"update inventory set quantity = quantity - {value} where item_id = {key}"
        curs.execute(query)
        

    for key,value in billed_amt.items():
        total = total + value[1]
    


def bill_print(bill_id, ts, dop,cid):
    name = "bill-" + str(bill_id) + '.txt'
    new_path = os.path.join(dpath,name)
    with open(new_path, 'w') as f:
        f.write(f'''
--------------Bill--------------

Bill ID - 0000{bill_id}
Customer ID - 0000{cid}
Date of purchase - {dop}

Item \tQty \tPrice
''')
        for key,value in billed_amt.items():

            f.write(f"{key} \t{value[0]} \t\t{value[1]}\n")

        f.write(f"\nTotal \t\t{total}")
        f.write("\n-------------Thank You!!-----------")


def generate(cid):
    dop = date.today()
    now = datetime.now()
    ts = datetime.isoformat(now)
    ts = ts.replace(" ","")


    while True:
        add_items()

        c = input("Add more items? [Y/N]")
        if c in ['n','N']:
            break
    
    settle(billed, billed_amt)

    curs.execute(f"insert into sales (dop, bill_value, cid, time_id) values('{dop}',{total}, {cid}, '{ts}')")
    
    curs.execute(f"select bill_id from sales where time_id = '{ts}'")
    data = curs.fetchall()
    bill_id = data[0][0]

    bill_print(bill_id,ts,dop,cid)
    mcon.commit()
    