


import sqlite3
from tracemalloc import start
from time_module import timer
base = sqlite3.connect("school.db")
c = base.cursor()
from random import randint
import pickle
import time
from datetime import datetime
from threading import Thread
from tabulate import tabulate

# c.execute("drop table service_providers")
# c.execute("""create table service_providers( 
#     code int primary key,
#     driver_name varchar(50),
#     vehicle_code int,
#    name varchar(50) ,
#     number int,
#    start_time int,
#    end_time int,
#    cost_per_hr int,
#    others varchar(100)



# )
# """)

# c.execute("""create table customers_log( 
#     customer_code int primary key,
#     customer_name varchar(100),
#     adress varchar(100),
#     code int,
#     vehicle_code int,
#     start_time int,
#     end_time int



# )
# """)



def service_providers():
    # c.execute('Delete from service_providers')
    # l = []
    # f1 = open("service_providers.dat" , 'ab')
    # f2 = open("service_providers.dat" , 'rb')
    # try: 
    #     while 1:
    #         d = pickle.load(f2) # to load all alloted codes to a list to prevent duplication
    #         l += [d]
    # except:
    #     f2.close()
    #to check if code aldready exists
    code_name_1 = input("enter name of organization/driver: ")
    code_1 = randint(1000 , 9999)
    data = c.execute("select code from service_providers")
    for x in data.fetchall():
        while (code_1 , ) in x:  #checks if the code aldready exists (to be verified)
            code_1 = randint(1000 , 9999)


    # while {code_1 , 1} in l: #dict with key as code and value as one to check if it is repeated
    #     code_1 = randint(1000 , 9999)
    # d = {code_1: 1}
    # pickle.dump(d , f1)
    # f1.close()

    types = int(input("enter number of car models: "))
    vehicle_code_1 = 0
    for x in range(types):
        vehicle_code_1 += 1
            
        name_1 = input("enter car name: ")
        number_1 = int(input("enter number of units: "))
        start_time_1 = int(input("enter start time (hour in integer format in 24 hour clock): "))
        end_time_1 = int(input("enter end time (hour in integer format in 24 hour clock): "))

        while start_time_1 not in range(0,24) or end_time_1 not in range(0 , 24):
            print("sorry that the time given wasnt valid")
            start_time_1 = int(input("enter start time (hour in integer format in 24 hour clock): "))
            end_time_1 = int(input("enter end time (hour in integer format in 24 hour clock): "))
        
        while start_time_1 > end_time_1:
            print("sorry overnight shifts not allowed")
            start_time_1 = int(input("enter start time (hour in integer format in 24 hour clock): "))
            end_time_1 = int(input("enter end time (hour in integer format in 24 hour clock): "))
            
        others_1 = input("enter any other information (less than 100 characters): ")
        # available_1 = "Yes"
        cost_per_hr_1 = int(input("enter cost per hour in rupees: "))  
        c.execute("insert into service_providers(code , driver_name ,vehicle_code, name,number, start_time ,end_time  , cost_per_hr , others) values({}, '{}',{}, '{}' , {} ,{}, {} , {} , '{}')".format(code_1 , code_name_1 ,vehicle_code_1, name_1 ,number_1, start_time_1 , end_time_1 ,  cost_per_hr_1 , others_1)) #syntax for user input insert into table
        #driver name, name(vehicle name), number(units), time are user input     code and vehicle_code are autogenerated available will depend on number
    print("thank you for registering with us")
    base.commit()

def customers():
    address = input('enter your address: ')
    customer_name_1 = input('please enter your name: ')
    temp_list = [('code' , 'name' , 'vehicle code' , 'car model' , 'units available' , 'start time' , "end time" , 'cost per hour' , 'other information')]

    #print("code                 name                   vehicle code                car model        units available        duration of rental") #display of service provider details
    data = c.execute("select * from service_providers")
    temp_list += data.fetchall()
    print("""
    1. pick up asap
    2. pick up at scheduled time
    """)
    choice_1 = int(input("enter your choice(1 or 2): "))
    while choice_1 not in [1,2]:
        print('sorry that input was not valid')
        choice_1 = int(input("enter your choice(1 or 2): "))
    if choice_1 == 1:
        current_time = datetime.now().hour
    else:
        current_time = int(input("enter pickup time (in 24 hour clock): "))
        while current_time not in range(0 , 24):
            print('sorry that input was not valid')
            current_time = int(input("enter pickup time (in 24 hour clock): "))


    for x in range(1 , len(temp_list)):
        if current_time not in range(temp_list[x][5] , temp_list[x][6]):
            a,b,d,e,f,g,h,j,k= temp_list[x] #unpack and repack
            f = 0
            temp_list[x] = (a,b,d,e,f,g,h,j,k)
        """to compare with customers log table and reduce the units for the cars that are currently being used"""
        data = c.execute("select code , vehicle_code , start_time , end_time from customers_log")
        data = c.execute("select start_time , end_time from customers_log where code = {} and vehicle_code = {}".format(temp_list[x][0] , temp_list[x][2]))
        for y in data.fetchall():
        
                
            if current_time in range(y[0] , y[1] + 1):      
                a,b,d,e,f,g,h,j,k= temp_list[x] #unpack and repack
                if f != 0:
                    f -= 1
                temp_list[x] = (a,b,d,e,f,g,h,j,k)
            
                  



 
    print(tabulate(temp_list))
    # for x in data.fetchall():
    #     for y in x:
    #         print(y , end = "                 ")
    #     print()
    
    code = int(input("enter preffered service provider code from the table (0 to abort booking): ")) #user to input one of the service provider codes
    if code == 0:
        return None
    data = c.execute("select code from service_providers")
    li = []
    for x in data.fetchall():
        
        li += [x[0]]
    print(li)
    while code not in li:
        print("code doesnt exist")
        code = int(input("enter preffered service provider code from the table (0 to abort booking): "))
        if code == 0:
            return None
            break
        
    print(".....")
    vehicle_code = int(input("enter vehicle code: "))

    data = c.execute("SELECT code , vehicle_code FROM service_providers")
    temp_l = []
    for x in c.fetchall():
        temp_l += [x]
    while (code , vehicle_code) not in temp_l:
        print("sorry that vehicle code doesnt exist please try again")
        vehicle_code = int(input("enter vehicle code: "))



    data = c.execute("select code , vehicle_code , number from service_providers")  # to check if vehicle is available

    for x in c.fetchall():
        if x[0] == code and x[1] == vehicle_code:
            
            if x[2] > 0:
                time = int(input("enter number of hours of rental: ")) #vehicle number to be reduces by one for the specified time period
                if current_time + time > 24:
                    print("sorry overnight bookings not available")
                    time = int(input("enter number of hours of rental: "))

                # current_time = datetime.now().hour #current hour is stored
            
                # data = c.execute("select * from service_providers")
            
                l = []
                # for i in data.fetchall():
                #     print(i)
                #     l += [i]
                # data = l
                data = temp_list[1::] # to leave out the headers

                for y in range(len(data)):

                    if (code , vehicle_code) == (data[y][0] , data[y][2]):
                        units = data[y][4]
                        print(units)
                        def reduce(code , vehicle_code, units , start_time , end_time):
                            # print(current_time , time)
                            if units == 0 or not(start_time <= current_time < current_time + time <= end_time ):  #to check if time is within valid time limit 
                                if units == 0:   
                                    print("unsuccesful booking no units available")
                                else:
                                    print("sorry units not available for that time slot")
                                return None
                               
                            else:
                                
                                    print('booking succesful! Driver will pick you up at the provided adress shortly')
                                    c.execute("insert into customers_log(customer_code , customer_name ,adress, code ,vehicle_code, start_time ,end_time ) values({}, '{}','{}', {} , {} ,{}, {})".format(randint(1000,9999)  ,customer_name_1, address ,code,vehicle_code, current_time , current_time + 1 + time )) #syntax for user input insert into table
                                    base.commit()
                                    return True
                        reduce(data[y][0] , data[y][2] , units , data[y][5] , data[y][6])



            else:
                print("booking unsuccesful no units available")
                customers()
                #recursive call if units unavailable


def increase_units(code , vehicle_code , units , time):
    data = c.execute("select * from service_providers")
    l = []
    for i in data.fetchall():
        print(i)
        l += [i]
    data = l
                  
    for y in range(len(data)):

        if (code , vehicle_code) == (data[y][0] , data[y][2]):
            units += 1
            data[y] = (data[y][0] , data[y][1] , data[y][2] , data[y][3] ,units ,data[y][5]  ,  data[y][6])

            c.execute('Delete from service_providers')
            for z in data:
                code_1 , code_name_1 ,vehicle_code_1, name_1 ,number_1, time_1 , available_1 = z

                c.execute("insert into service_providers(code , driver_name ,vehicle_code, name,number, time , available) values({}, '{}',{}, '{}' , {} , {},'{}')".format(code_1 , code_name_1 ,vehicle_code_1, name_1 ,number_1, time_1 , available_1))
                base.commit()

 

# the_func = Thread(target = customers.func)
# the_func.start()


#main

choice = input('enter c for customer and s for service provider: ') 
while choice not in ['c' , 's']:
    print("sorry that was an invalid input please input ('c' or 's') ")
    choice = input('enter c for customer and s for service provider: ')



if choice == 's':
    try: #exception handler to catch wrong input data type
        service_providers()
        data = c.execute("select * from  service_providers")
        for x in data.fetchall():
            print(x)
    except:
        print("sorry an error was raised please adhere to the input instructions")
        print("redirecting.....")
        service_providers()

elif choice == 'c':
    try:  #exception handler to catch wrong input data type
        customers()
    except:
        print("sorry an error was raised please adhere to the input instructions")
        print("redirecting.....")
        customers()


#function that checks if times in start and end time
# 3 parameters: start time , end time, duration of rental
# checks if current time , and current time + duration of rental is within start and end time
   






































