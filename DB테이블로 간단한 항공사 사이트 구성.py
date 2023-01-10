import time
import re
import mysql.connector 
mysql_con = mysql.connector.connect(host='localhost', port='3306', database='airline', user='root', password='dgu1234!')
cur = mysql_con.cursor()
import os
os.system('cls')
print("===============Airline homepage===============\n")
print("1. sign in\n")
print("2. log in\n")
print("==============================================\n")
x= int(input())
os.system('cls')
email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
phone_check = re.compile('\d{3}\d{3,4}\d{4}')

if(x == 1):
    print("===============Airline homepage===============\n")
    print("Please put your information!! \n")
    z= input("Member ID : ")
    a =input("Name : ")
    b =input("Address : ")
    c =input("Phone Number : ")
    c = phone_check.match(c)
    while(True):
        if(c == None):
            print("Please type in numbers!")
            c =input("Phone Number : ")
            c = phone_check.match(c)
        else:
            break
        
    d =input("Passport number : ")
    while(len(d) != 9):
        print("Please enter in 9 digits!")
        d =input("Passport Number : ")
      
    e =int(input("Age : "))
    while(e>110 or e<0):
        print("Please type in numbers!")
        e =input("age : ")
    f =input("E-mail : " )
   
    f = email_check.match(f)
    while(True):
        if(f ==None):
            print("Please type in mail!")
            f =input("E-mail : ")
            f = email_check.match(f)
        else:
            break
    x = c.group()
    y = f.group()
    sql = ("INSERT INTO member" "(member_ID, member_name, address, phone_number, age, passport_number,email)" "VALUES (%s, %s, %s,%s,%s,%s,%s)")   

    cur.execute(sql,(z,a,b,x,d,e,y))
    print("Membership success!")
    mysql_con.commit() 
    time.sleep(3)    
    os.system('cls')
    print("===============Airline homepage===============\n")
    print("Please enter your ID")
    id= int(input("▶  "))
    cur.execute('select member_ID,member_name from member')
    findid=cur.fetchall()
    for i,j in findid:
         if(id==i):
              print(j+" login success!")
    print("==============================================\n")
    time.sleep(3)    
    os.system('cls')

elif(x==2):
    print("===============Airline homepage===============\n")
    print("Please enter your ID")
    id= int(input("▶  "))
    cur.execute('select member_ID,member_name from member')
    findid=cur.fetchall()
    for i,j in findid:
         if(id==i):
              print(j+" login success!")
        
    print("\n==============================================\n")
time.sleep(3)
os.system('cls')
    
while(True):    
    print("===============Airline homepage===============\n")
    print("※  Please choose the service you want to use  ※\n")
    print("1. Ticket Reservation\n")
    print("2. Check Reservation\n")
    print("3. Check Membership\n")
    print("4. Administrator mode\n")
    print("==============================================\n")
    menu= int(input())
    os.system('cls')
    if(menu==1):
        print("===============Ticket Reservation===============\n")
        print("Search \n")
        print("1. one way\n")
        print("2. round trip\n")
        print("==============================================\n")
        reserv=int(input())
        if(reserv == 1):
            print("===============One Way Ticket Reservation===============\n")
            print("Please put the items")
            destination = int(input("The Destination you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon  7.Busan  ▶  "))
            while(True):
                if(0< destination < 8):
                    break
                else:
                    destination = int(input("The Destination you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon  7.Busan  ▶  "))
        
            departure = int(input("The Departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon  7.Busan  ▶  "))
            while(True):
                if(0< departure < 8):
                    while(destination == departure):
                        departure = int(input("The Departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon  7.Busan  ▶  "))
                    break
                else:
                    departure = int(input("The departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon  7.Busan  ▶  "))

            person_choice = int(input("Types of passenger | 1. Adult    2. Adult, Child   3. Adult, Infant  4. Audult, Child, Infant\n (Notice) Child and Infants Always together with Adult "))
            while(True):
                if(0< person_choice < 5):
                    break
                else:
                    person_choice = int(input("Types of passenger | 1. Adult 2. Adult, Child 3. Adult, Infant 4. Audult, Child, Infant"))
            minimum = 0
            if(person_choice == 4):
                minimum =3
                person_choice ="Audult, Child, Infant"
            elif(person_choice == 2):
                minimum =2
                person_choice ="Audult, Child"
            elif(person_choice == 3):
                minimum =2
                person_choice ="Audult, Infant"
            elif(person_choice ==1):
                minimum =1
                person_choice ="Audult"
            person_number= int(input("Number of people : "))
            while(True):
                if(person_number>minimum):
                    break
                else:
                    print("The number of tickets is smaller than the minimum number of passengers")
                    answer = input("Keep going or Fix | 1. keep going 2. Fix  ▶  ")
                    if(answer == "2"):
                        person_number= int(input("Number of people : "))
                    
            seat_level=input("Choose your Seat Level | 1. Economy 2. Business Class 3.First Class  ▶  ")

            while(True):
                if(seat_level == "1" or "2" or "3"):
                    if(seat_level =="1"):
                        seat_level ="Economy Class"
                    elif(seat_level =="2"):
                        seat_level = "Business Class"
                    else:
                        seat_level ="First Class"
                    break
                else:
                    seat_level=input("Choose your Seat Level | 1. Economy 2. Business Class 3.First Class  ▶  ")
                
            Payment_classification=input("Payment right away or Post Payment  | 1.Payment right away 2.Post Payment  ▶  ")
            while(True):
                if(Payment_classification == "1" or "2"):
                    break
                else:
                    Payment_classification=input("Payment right away or Post Payment  | 1.Payment right away 2.Post Payment  ▶  ")
            
            
            sql2 = ("INSERT INTO ticket_reservation" "(flight_number, round_tripone_way, point_of_departure, destination, passengerschoice, number_of_people,seat_level,Payment_classification)" "VALUES (%s, %s, %s,%s,%s,%s,%s,%s)")   
            number = "aa123456789" + str(departure) + str(destination)
            if(departure == 1):
                departure = "NewYork"
            elif(departure ==2):
                departure ="Paris"
            elif(departure ==3):
                departure ="London"
            elif(departure ==4):
                departure ="Beijing"
            elif(destination ==5):
                destination ="seoul"
            elif(destination ==6):
                destination ="Incheon"
            elif(destination ==7):
                destination ="busan"
            if(destination == 1):
                destination = "NewYork"
            elif(destination ==2):
                destination ="Paris"
            elif(destination ==3):
                destination ="London"
            elif(destination ==4):
                destination ="Beijing"
            elif(destination ==5):
                destination ="seoul"
            elif(destination ==6):
                destination ="Incheon"
            elif(destination ==7):
                destination ="busan"
            if(Payment_classification=="1"):
                Payment_classification ="Payment right away"
            else:
                Payment_classification ="Post Payment"
            cur.execute(sql2,(number,"one way",departure,destination,person_choice,person_number,seat_level,Payment_classification))
            print("Ticket purchase success!")
            final = int(input("return menu or exit? | 1. menu   2. exit  ▶  "))
            if(final ==2):
                break
            time.sleep(3)
            os.system('cls')
        elif(reserv == 2):
            print("===============Round trip Ticket Reservation===============\n")
            print("Please put the items")
            destination = int(input("The Destination you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul  ▶  "))
            while(True):
                if(0< destination < 8):
                    break
                else:
                    destination = int(input("The Destination you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon   7.Busan  ▶  "))
        
            departure = int(input("The Departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon   7.Busan  ▶  "))
            while(True):
                if(0< departure < 8):
                    while(destination == departure):
                        departure = int(input("The Departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon   7.Busan  ▶  "))
                    break
                else:
                    departure = int(input("The departure you can choose | 1. New york   2. Paris    3. London   4.Beijing   5. Seoul    6. Incheon   7.Busan  ▶  "))

            person_choice = int(input("Types of passenger | 1. Adult    2. Adult, Child   3. Adult, Infant  4. Audult, Child, Infant\n (Notice) Child and Infants Always together with Adult "))
            while(True):
                if(0< person_choice < 5):
                    break
                else:
                    person_choice = int(input("Types of passenger | 1. Adult 2. Adult, Child 3. Adult, Infant 4. Audult, Child, Infant"))
            minimum = 0
            if(person_choice == 4):
                minimum =3
                person_choice ="Audult, Child, Infant"
            elif(person_choice == 2):
                minimum =2
                person_choice ="Audult, Child"
            elif(person_choice == 3):
                minimum =2
                person_choice ="Audult, Infant"
            elif(person_choice ==1):
                minimum =1
                person_choice ="Audult"
            person_number= int(input("Number of people : "))
            while(True):
                if(person_number>minimum):
                    break
                else:
                    print("The number of tickets is smaller than the minimum number of passengers chosen by the customer.")
                    answer = input("Keep going or Fix | 1. keep going 2. Fix  ▶  ")
                    if(answer == "2"):
                        person_number= int(input("Number of people : "))
                    
            seat_level=input("Choose your Seat Level | 1. Economy 2. Business Class 3.First Class  ▶  ")

            while(True):
                if(seat_level == "1" or "2" or "3"):
                    if(seat_level =="1"):
                        seat_level ="Economy Class"
                    elif(seat_level =="2"):
                        seat_level = "Business Class"
                    else:
                        seat_level ="First Class"
                    break
                else:
                    seat_level=input("Choose your Seat Level | 1. Economy 2. Business Class 3.First Class  ▶  ")
                
            Payment_classification=input("Payment right away or Post Payment  | 1.Payment right away 2.Post Payment  ▶  ")
            while(True):
                if(Payment_classification == "1" or "2"):
                    break
                else:
                    Payment_classification=input("Payment right away or Post Payment  | 1.Payment right away 2.Post Payment  ▶  ")
            
            
            sql2 = ("INSERT INTO ticket_reservation" "(flight_number, round_tripone_way, point_of_departure, destination, passengerschoice, number_of_people,seat_level,Payment_classification)" "VALUES (%s, %s, %s,%s,%s,%s,%s,%s)")   
            number = "aa123456789" + str(departure) + str(destination)
            if(departure == 1):
                departure = "New York"
            elif(departure ==2):
                departure ="Paris"
            elif(departure ==3):
                departure ="London"
            elif(departure ==4):
                departure ="Beijing"
            elif(destination ==5):
                destination ="seoul"
            elif(destination ==6):
                destination ="Incheon"
            elif(destination ==7):
                destination ="busan"
            if(destination == 1):
                destination = "New York"
            elif(destination ==2):
                destination ="Paris"
            elif(destination ==3):
                destination ="London"   
            elif(destination ==4):
                destination ="Beijing"
            elif(destination ==5):
                destination ="seoul"
            elif(destination ==6):
                destination ="Incheon"
            elif(destination ==7):
                destination ="busan"
            
            if(Payment_classification=="1"):
                Payment_classification ="Payment right away"
            else:
                Payment_classification ="Post Payment"
            cur.execute(sql2,(number,"Round trip",departure,destination,person_choice,person_number,seat_level,Payment_classification))
            print("Ticket purchase success!")
            final = int(input("return menu or exit? | 1. menu   2. exit"))
            if(final ==2):
                break
            time.sleep(3)
            os.system('cls')
    elif(menu==2):
        print("===============Airline homepage===============\n")
        print("Please enter your flight number")
        flight_n= str(input("▶  "))
        while(len(flight_n)!=13):
            print("Please enter in 13 digits again!")
        cur.execute('select flight_number,round_tripone_way,point_of_departure,destination,passengerschoice,number_of_people,seat_level,Payment_classification from ticket_reservation')
        findticket=cur.fetchall()
        for (a,b,c,d,e,f,g,h) in findticket:
            if(flight_n==a):
                print("\n※ Reservation info. ※")
                print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
        print("==============================================\n")
        final = int(input("return menu or exit? | 1. menu   2. exit  ▶  "))
        if(final ==2):
            break
        time.sleep(3)
        os.system('cls')
    elif(menu==3):
        print("===============Airline homepage===============\n")
        print("Please enter your ID: ")
        member=int(input("▶  "))
        while(len(str(member))!=8):
            print("Please enter it again in 8 digits!")
        cur.execute('select member_ID,member_name,address,phone_number,age,passport_number,email from member')
        findmember=cur.fetchall()
        for (a,b,c,d,e,f,g) in findmember:
            if(member==a):
                print("\n※ Member info. ※")
                print("name: "+str(b)+"\n"+"address: "+str(c)+"\n"+"phone number: "+str(d)+"\n"+"age: "+str(e)+"\n"+"passport number: "+str(f)+"\n"+"email: "+str(g))
        print("\n==============================================\n")
        final = int(input("return menu or exit? | 1. menu   2. exit  ▶  "))
        if(final ==2):
            break
        time.sleep(3)
        os.system('cls')
    elif(menu==4):
        print("===============Airline Administer page===============\n")
        print("1. Ticket purchase trend \n")
        print("2. Search\n")
        print("==============================================\n")
        admin=int(input())
        os.system('cls')
        if(admin==1):
            print("===============Airline Administer page===============\n")
            print("▷  Person with more than 10,000 miles.\n")
            cur.execute('select flight_number,mileage from payment where mileage>10000') ##use database airline(table:payment)
            f1=cur.fetchall()
            print(f1)
            print("\n▷  Paid in cash, and the number of adults on board is more than two.\n")
            cur.execute('select distinct adult,payment_way from payment,passenger where adult>2 and payment_way="cash"') ##use database airline(table:payment,passenger)
            f2=cur.fetchall()
            print(f2)
            print("\n▷  Person who are over 24 years old and boarding date is November 7th. \n")
            cur.execute('select member_name,boarding_date from member,oneway where age>24 and boarding_date=1107 group by boarding_date') ##use database airline(table member,oneway)
            f3=cur.fetchall()
            print(f3)
            print("\n▷  Person information whose boarding date is January 13th and going one way \n")
            cur.execute('select distinct flight_number, round_tripone_way, point_of_departure, destination,passengerschoice,number_of_people,seat_level from ticket_reservation where exists(select boarding_date from oneway where boarding_date=0113) ')
            ##use database airline(table: ticket_reservation)
            f4=cur.fetchall()
            print(f4)
        

            print("==============================================\n")
        elif(admin==2):
            print("===============Airline Administer page===============\n")
            while(True):
                print("Search by\n")
                print("1.seat level    2.round trip/one way    3.point of departure    4.destination")
                search=int(input("▶  "))
                print("==============================================\n")
                os.system('cls')
                if(search==1):
                    print("Find who are")
                    print("1. economy class\n")
                    print("2. business class\n")
                    print("3. first class\n")
                    n=int(input("▶  "))
                    if(n==1):
                        cur.execute('select * from ticket_reservation where seat_level="economy_class"')
                        fa=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fa:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==2):
                        cur.execute('select * from ticket_reservation where seat_level="business_class"')
                        fb=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fb:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))

                    elif(n==3):
                        cur.execute('select * from ticket_reservation where seat_level="first_class"')
                        fc=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fc:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    print("==============================================\n")
                    final = int(input("return administer page or exit? | 1. administer page   2. exit  ▶  "))
                    if(final ==2):
                        break
                    os.system('cls')
                elif(search==2):
                    print("===============Airline Administer page===============\n")
                    print("Find who are")
                    print("1. round trip\n")
                    print("2. one way\n")
                    n=int(input("▶  "))
                    if(n==1):
                        cur.execute('select * from ticket_reservation where round_tripone_way="roundtrip"')
                        fd=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fd:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==2):
                        cur.execute('select * from ticket_reservation where round_tripone_way="oneway"')
                        fe=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fe:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    print("==============================================\n")
                    final = int(input("return administer page or exit? | 1. administer page   2. exit  ▶  "))
                    if(final ==2):
                        break
                    os.system('cls')
                elif(search==3):
                    print("===============Airline Administer page===============\n")
                    print("Find whose point of departure is")
                    print("1. New york\n")
                    print("2. Paris\n")
                    print("3. London\n")
                    print("4. Beijing\n")
                    print("5. Seoul\n")
                    print("6. Incheon\n")
                    print("7. Busan\n")
                    n=int(input("▶  "))
                    if(n==1):
                        cur.execute('select * from ticket_reservation where point_of_departure="NewYork"')
                        ff=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in ff:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==2):
                        cur.execute('select * from ticket_reservation where point_of_departure="Paris"')
                        fg=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fg:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==3):
                        cur.execute('select * from ticket_reservation where point_of_departure="London"')
                        fh=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fh:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==4):
                        cur.execute('select * from ticket_reservation where point_of_departure="Beijing"')
                        fi=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fi:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==5):
                        cur.execute('select * from ticket_reservation where point_of_departure="seoul"')
                        fj=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fj:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==6):
                        cur.execute('select * from ticket_reservation where point_of_departure="Incheon"')
                        fk=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fk:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==7):
                        cur.execute('select * from ticket_reservation where point_of_departure="busan"')
                        fl=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fl:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    print("==============================================\n")
                    final = int(input("return administer page or exit? | 1. administer page   2. exit  ▶  "))
                    if(final ==2):
                        break
                    os.system('cls')
                elif(search==4):
                    print("===============Airline Administer page===============\n")
                    print("Find whose destination is")
                    print("1. New york\n")
                    print("2. Paris\n")
                    print("3. London\n")
                    print("4. Beijing\n")
                    print("5. Seoul\n")
                    print("6. Incheon\n")
                    print("7. Busan\n")
                    n=int(input("▶  "))
                    if(n==1):
                        cur.execute('select * from ticket_reservation where point_of_departure="NewYork"')
                        ff=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in ff:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==2):
                        cur.execute('select * from ticket_reservation where point_of_departure="Paris"')
                        fg=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fg:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==3):
                        cur.execute('select * from ticket_reservation where point_of_departure="London"')
                        fh=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fh:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==4):
                        cur.execute('select * from ticket_reservation where point_of_departure="Beijing"')
                        fi=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fi:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==5):
                        cur.execute('select * from ticket_reservation where point_of_departure="seoul"')
                        fj=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fj:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==6):
                        cur.execute('select * from ticket_reservation where point_of_departure="Incheon"')
                        fk=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fk:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    elif(n==7):
                        cur.execute('select * from ticket_reservation where point_of_departure="busan"')
                        fl=cur.fetchall()
                        for (a,b,c,d,e,f,g,h) in fl:
                            print("flight_number: "+str(a)+"\n"+"round trip/one way: "+str(b)+"\n"+"start: "+str(c)+"\n"+"end: "+str(d)+"\n"+"passengers: "+str(e)+"\n"+"number of passengers: "+str(f)+"\n"+"seat level: " +str(g)+"\n"+"now/later : "+str(h))
                    print("==============================================\n")
                final = int(input("return administer page or exit? | 1. administer page   2. exit  ▶  "))
                if(final ==2):
                    break
                os.system('cls')
        final = int(input("return menu or exit? | 1. menu   2. exit  ▶  "))
        if(final ==2):
             break
        time.sleep(3)
        os.system('cls')    
    