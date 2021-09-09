import sqlite3
base = sqlite3.connect("school.db")
c = base.cursor()
from random import randint
import pickle

c.execute("drop table service_providers")
c.execute("""create table service_providers( 
    code int,
    driver_name varchar(50),
    vehicle_code int,
   name varchar(50) ,
    number int,
   start_time int,
   end_time int

)
""")

def service_providers():
    l = []
    f1 = open("service_providers.dat" , 'ab')
    f2 = open("service_providers.dat" , 'rb')
    try:
        while 1:
            d = pickle.load(f2)
            l += [d]
    except:
        f2.close()
    #to check if code aldready exists
    code_name_1 = input("enter name of organization/driver: ")
    code_1 = randint(1000 , 9999)
        
    while {code_1 , 1} in l: #dict with key as code and value as one to check if it is repeated
        code_1 = randint(1000 , 9999)
    d = {code_1: 1}
    pickle.dump(d , f1)
    f1.close()

    types = int(input("enter number of car models: "))
    vehicle_code_1 = 0
    for x in range(types):
        vehicle_code_1 += 1
            
        name_1 = input("enter car name: ")
        number_1 = int(input("enter number of units: "))
        start_time_1 = int(input("enter start time: "))
        end_time_1 = int(input("enter end time: "))
        others_1 = input("enter any other information: ")
        c.execute("insert into service_providers(code , driver_name ,vehicle_code, name,number, start_time , end_time) values({}, '{}', '{}' , {} , {} , {})".format(code_1 , code_name_1 ,vehicle_code_1 name_1 ,number_1, start_time_1 , end_time_1)) #syntax for user input insert into table

    base.commit()

def customers():
    print("code                 name                   vehicle code                   car model        units available   start time        end time")
    data = c.execute("select * from service_providers")
    for x in data.fetchall():
        for y in x:
            print(y , end = "                 ")
        print()
    
    code = int(input("enter preffered service provider code from the table (0 to abort booking): "))
    data = c.execute("select code from service_providers")
    for x in data.fetchall():
        
        while code not in x:
            print("code doesnt exist")
            code = int(input("enter preffered service provider code from the table (0 to abort booking): "))
        
        print(".....")
        vehicle_code = int(input("enter vehicle code: "))

    




choice = input('enter c for customer and s for service provider: ') 
if choice == 's':
    service_providers()
elif choice == 'c':
    customers()




