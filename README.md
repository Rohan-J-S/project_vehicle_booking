Topic:   Application for handling vehicle ride bookings, and vehicle registration with (tentative) carpooling feature (tentative). 

Name of students:   Rohan J S, Adarsh Raman

Project description: The application can be used by 2 types of users, service providers or customers. 
1) service providers: service providers can use the application as a platform to accept bookings, registering their vehicles to be available for rent on the application. (Assumed to be drivers who believe in bigger profit margins using organized platforms or companies supplying drivers and vehicles.
2) customers: The customers will be shown the available vehicles for booking. They are to pick a convenient time slot for the booking depending on availability. (tentative) carpooling option where customer can choose from available seats from booked rides (tentative). 

Table structure
----  ----------  -------------  ---------  ---------------  ------------------  ----------
code  name        vehilcle code  car model  units available  duration of rental  available?
9361  muthappa    1              baleno     1                2                   Yes
9361  muthappa    2              swift      1                2                   Yes
4303  revanna     1              alto       1                3                   Yes
9435  tourz cabs  1              innova     1                3                   Yes
9435  tourz cabs  2              city       3                3                   Yes
9435  tourz cabs  3              Nexon      8                3                   Yes
9435  tourz cabs  4              taigun     5                3                   Yes
9435  tourz cabs  5              kona       3                3                   Yes
----  ----------  -------------  ---------  ---------------  ------------------  ----------

User inputs:
1) service provider: driver names, vehicle name(model), number of units, start time of availability, end time of availability.
2) customer: code of preferred service provider, vehicle code, time of rental, confirmation.

Modules involved in the project:   time, datetime, threading, mysql/sqllite3, pickle, random

Time required for completion of the work: 20 hrs

Break up of work: 
Rohan J S: service provider
Adarsh Raman: customer
