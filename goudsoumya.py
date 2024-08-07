
from datetime import datetime

name=input("Enter your name =")
# for list of items
list='''
sugar     rs 40/kg
oil       rs 240/k
honey     rs 200/kg
parachute rs 220/bottle
goodnight rs 70/liquid
dal       rs 200/kg
salt      rs 35/packet
turmaric   rs 20/packet
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
items={'sugar':40,'oil':240,'honey':200,'parachute':220,'goodnight':70,'dal':200,'salt':35,'turmaric':20}
option=int(input("for list of items press 1="))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit="))
    if inp1==2:
     break
    if inp1==1:
        item=input("Enter your items =")
        quantity=int(input("Enter your quantity ="))
        if item in items.keys():
          price=(quantity*(items[item]))
          pricelist.append((items,quantity,item,price))
          totalprice+=price
          ilist.append(items)
          qlist.append(quantity)
          plist.append(price)
          gst=(totalprice*5)/100
          finalamount=gst+totalprice
        else:
           print("sorry you entered item is not available")
    else:
       print("you entered wrong number")
    inp=input("can i bill the item yes or no=")
    if inp=="yes":
       pass
       if finalamount!=0:
        print(28*"-","SOUMYA SUPERMARKET",28*"-")
        print(25*"=","RAICHUR",25*"-")
        print("Name:",name,30*" ","Date",datetime.now())
        print(75*"-")
        print(("sno",8*"-",'items',8*"-",'quantity',3*"-",'price'))
        for i in range(len(pricelist)):
            print(i,8*"-",8*"-",ilist[i],3*"-",qlist[i],plist[i])
            print(75*"=")
            print(50*"-",'Totalamount','Rs',totalprice)
            print("gst amount",50*"-",'Rs',gst)
            print(75*"=")
            print(50*"-",'finalamount','rs',finalamount)
















   
           
          





















          
       

















