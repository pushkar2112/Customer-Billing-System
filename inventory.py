from mcon import curs

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