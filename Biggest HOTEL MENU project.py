#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Hotel():
    def hotel(self):
        print("Welcome to hotel")

class menu():
    def mymenu(self):
        print("1-dessert")
        print("2-vegdish")
        print("3-non-vegdish")
        print("4-bevearges")
        print("5-bill")
        
class Submenu():
    def submenu(self):
        if(opt==1):
            print("1-cupcakes")
            print("2- donuts")
            print("3-custards")
        elif(opt==2):
            print("4-rajmachawal")
            print("5-kebab")
            print("6-vegbiryani")
        elif(opt==3):
            print("7-grilledchicken")
            print("8-chickentikka")
            print("9-chillichicken")
        elif(opt==4):
            print("10-bluelagoon")
            print("11-virginmojito")
            print("12-wine")
        else:
            print("Order from menu card only")
            
class Dishname():
    cupcakes="cupcakes"
    def getcupcakesname(self):
        return self.cupcakes
    donuts="donuts"
    def getdonutsname(self):    
        return self.donuts
    custards="custards"
    def getcustardsname(self):
        return self.custards
    rajmaChawal="rajmaChawal"
    def getrajmachawalname(self):
        return self.rajmaChawal
    kebab="kebab"
    def getkebabname(self):
        return self.kebab
    vegbiryani="vegbiryani"
    def getvegbiryaniname(self):
        return self.vegbiryani
    grilledchicken="grilledchicken"
    def getgrilledchickenname(self):
        return self.grilledchicken
    chickentikka="chickentikka"
    def getchickentikkaname(self):
        return self.chickentikka
    chillichicken="chillichicken"
    def getchillichickenname(self):
        return self.chillichicken
    bluelagoon="bluelagoon"   
    def getbluelagoonname(self):
        return self.bluelagoon
    virginmojito="virginmojito"   
    def getvirginmojitoname(self):
        return self.virginmojito
    wine="wine"
    def getwinename(self):
        return self.wine
    
class price():
    cupcakes=200
    def getcupcakesprice(self):
        return self.cupcakes
    donuts=150
    def getdonutsprice(self):
        return self.donuts
    custards=250
    def getcustardsprice(self):
        return self.custards
    rajmaChawal=200
    def getrajmachawalprice(self):
        return self.rajmaChawal
    kebab=250
    def getkebabprice(self):
        return self.kebab
    vegbiryani=260
    def getvegbiryaniprice(self):
        return self.vegbiryani
    grilledchicken=250
    def getgrilledchickenprice(self):
        return self.grilledchicken
    chickentikka=300
    def getchickentikkaprice(self):
        return self.chickentikka
    chillichicken=200
    def getchillichickenprice(self):
        return self.chillichicken
    bluelagoon=290
    def getbluelagoonprice(self):
        return self.bluelagoon
    virginmojito=300
    def getvirginmojitoprice(self):
        return self.virginmojito
    wine=350
    def getwineprice(self):
        return self.wine
    
class Dishcount():
    cupcakescount=0
    def setcupcakes(self,qty):
        self.cupcakescount=self.cupcakescount+qty
    donutscount=0
    def setdonuts(self,qty):
        self.donutscount=self.donutscount+qty
    custardscount=0
    def setcustards(self,qty):
        self.custardscount=self.custardscount+qty
    rajmachawalcount=0
    def setrajmachawal(self,qty):
        self.rajmachawalcount=self.rajmachawalcount+qty
    kebabcount=0
    def setkebab(self,qty):
        self.kebabcount=self.kebabcount+qty
    vegbiryanicount=0
    def setvegbiryani(self,qty):
        self.vegbiryanicount=self.vegbiryanicount+qty
    grilledchickencount=0
    def setgrilledchicken(self,qty):
        self.grilledchickencount=self.grilledchickencount+qty
    chickentikkacount=0
    def setchickentikka(self,qty):
        self.chickentikkacount=self.chickentikkacount+qty
    chillichickencount=0
    def setchillichicken(self,qty):
        self.chillichickencount=self.chillichickencount+qty
    bluelagooncount=0
    def setbluelagoon(self,qty):
        self.bluelagooncount=self.bluelagooncount+qty
    virginmojitocount=0
    def setvirginmojito(self,qty):
        self.virginmojitocount=self.virginmojitocount+qty
    winecount=0
    def setwine(self,qty):
        self.winecount=self.winecount+qty
    def getcupcakescount(self):
        return self.cupcakescount
    def getdonutscount(self):
        return self.donutscount
    def getcustardscount(self):
        return self.custardscount
    def getrajmachawalcount(self):
        return self.rajmachawalcount
    def getkebabcount(self):
        return self.kebabcount
    def getvegbiryanicount(self):
        return self.vegbiryanicount
    def getgrilledchickencount(self):
        return self.grilledchickencount
    def getchickentikkacount(self):
        return self.chickentikkacount
    def getchillichickencount(self):
        return self.chillichickencount
    def getbluelagooncount(self):
        return self.bluelagooncount
    def getvirginmojitocount(self):
        return self.virginmojitocount
    def getwinecount(self):
        return self.winecount
    
class Handler():
    def operations(self,obj):
        Flag=True
        Tbill=0
        count=0
        while(Flag):
            obj.getmenu().mymenu()
            ord=int(input("Enter the no."))
            if(ord==1):
                Tag=True
                while(Tag):
                    print("1-cupcakes")
                    print("2- donuts")
                    print("3-custards")
                    print("4 Go to main Menu")
                    opt=int(input("Select dish "))
                    if(opt==1):
                        print(obj.getDishname().getcupcakesname())
                        qty=int(input("No.of plates "))
                        obj.getDishcount().setcupcakes(qty)
                        obj.getcashier().updatebill(obj.getprice().getcupcakesprice()*qty)
                    elif(opt==2):
                        print(obj.getDishname().getdonutsname())
                        qty=int(input())
                        obj.getDishcount().setdonuts(qty)
                        obj.getcashier().updatebill(obj.getprice().getdonutsprice()*qty)
                    elif(opt==3):
                        print(obj.getDishname().getcustardsname())
                        qty=int(input())
                        obj.getDishcount().setcustards(qty)
                        obj.getcashier().updatebill(obj.getprice().getcustardsprice()*qty)
                    elif(opt==4):
                        Tag=False
                        
                  
            elif(ord==2):
                Tag1=True
                while(Tag1):
                    print("5-rajmachawal")
                    print("6-kebab")
                    print("7-vegbiryani")
                    print("8-Go to main menu")
                    opt=int(input("Enter the nos. "))
                    if(opt==5):
                        print(obj.getDishname().getrajmachawalname())
                        qty=int(input("No.of plates "))
                        obj.getDishcount().setrajmachawal(qty)
                        obj.getcashier().updatebill(obj.getprice().getrajmachawalprice()*qty)
                    elif(opt==6):
                        print(obj.getDishname().getkebabname())
                        qty=int(input())
                        obj.getDishcount().setkebab(qty)
                        obj.getcashier().updatebill(obj.getprice().getkebabprice()*qty)
                    elif(opt==7):
                        print(obj.getDishname().getvegbiryaniname())
                        qty=int(input())
                        obj.getDishcount().setvegbiryani(qty)
                        obj.getcashier().updatebill(obj.getprice().getvegbiryaniprice()*qty)
                    elif(opt==8):
                        Tag1=False

            elif(ord==3):
                Tag2=True
                while(Tag2):
                    print("9-grilledchicken")
                    print("10-chickentikka")
                    print("11-chillichicken")
                    print("12-Go to main menu")
                    opt=int(input("Enter the nos. "))
                    if(opt==9):
                        print(obj.getDishname().getgrilledchickenname())
                        qty=int(input("No.of plates "))
                        obj.getDishcount().setgrilledchicken(qty)
                        obj.getcashier().updatebill(obj.getprice().getgrilledchickenprice()*qty)
                    elif(opt==10):
                        print(obj.getDishname().getchickentikkaname())
                        qty=int(input())
                        obj.getDishcount().setchickentikka(qty)
                        obj.getcashier().updatebill(obj.getprice().getchickentikkaprice()*qty)
                    elif(opt==11):
                        print(obj.getDishname().getchillichickenname())
                        qty=int(input())
                        obj.getDishcount().setchillichicken(qty)
                        obj.getcashier().updatebill(obj.getprice().getchillichickenprice()*qty)
                    elif(opt==12):
                        Tag2=False

            elif(ord==4):
                Tag3=True
                while(Tag3):
                    print("13-bluelagoon")
                    print("14-virginmojito")
                    print("15-wine")
                    print("16-Go to main menu")
                    opt=int(input("Enter the nos. "))
                    if(opt==13):
                        print(obj.getDishname().getbluelagoonname())
                        qty=int(input("No.of plates "))
                        obj.getDishcount().setbluelagoon(qty)
                        obj.getcashier().updatebill(obj.getprice().getbluelagoonprice()*qty)
                    elif(opt==14):
                        print(obj.getDishname().getvirginmojitoname())
                        qty=int(input())
                        obj.getDishcount().setvirginmojito(qty)
                        obj.getcashier().updatebill(obj.getprice().getvirginmojitoprice()*qty)
                    elif(opt==15):
                        print(obj.getDishname().getwinename())
                        qty=int(input())
                        obj.getDishcount().setwine(qty)
                        obj.getcashier().updatebill(obj.getprice().getwineprice()*qty)
                    elif(opt==16):
                        Tag3=False

            elif(ord==5):
                obj.getbill,obj.getbill().printbill(obj)
                Flag=False

class bill():
        def printbill(self,obj):
                print("Name",   "price",   "Total")
                if(obj.getDishcount().getcupcakescount()>0):
                    print(obj.().getcupcakesname(),obj.getprice().getcupcakesprice(),obj.getprice().getcupcakesprice()*obj.getDishcount().getcupcakescount())
                if(obj.getDishcount().getdonutscount()>0):
                    print(obj.getDishname().getdonutsname(),obj.getprice().getdonutsprice(),obj.getprice().getdonutsprice()*obj.getDishcount().getdonutscount())
                if(obj.getDishcount().getcustardscount()>0):
                    print(obj.getDishname().getcustardsname(),obj.getprice().getcustardsprice(),obj.getprice().getcustardsprice()*obj.getDishcount().getcustardscount())
                if(obj.getDishcount().getrajmachawalcount()>0):
                    print(obj.getDishname().getrajmachawalname(),obj.getprice().getrajmachawalprice(),obj.getprice().getrajmachawalprice()*obj.getDishcount().getrajmachawalcount())
                if(obj.getDishcount().getkebabcount()>0):
                    print(obj.getDishname().getkebabname(),obj.getprice().getkebabprice(),obj.getprice().getkebabprice()*obj.getDishcount().getkebabcount())
                if(obj.getDishcount().getvegbiryanicount()>0):
                    print(obj.getDishname().getvegbiryaniname(),obj.getprice().getvegbiryaniprice(),obj.getprice().getvegbiryaniprice()*obj.getDishcount().getvegbiryanicount())
                if(obj.getDishcount().getgrilledchickencount()>0):
                    print(obj.getDishname().getgrilledchickenname(),obj.getprice().getgrilledchickenprice(),obj.getprice().getgrilledchickenprice()*obj.getDishcount().getgrilledchickencount())
                if(obj.getDishcount().getchickentikkacount()>0):
                    print(obj.getDishname().getchickentikkaname(),obj.getprice().getchickentikkaprice(),obj.getprice().getchickentikkaprice()*obj.getDishcount().getchickentikkacount())
                if(obj.getDishcount().getchillichickencount()>0):
                    print(obj.getDishname().getchillichickenname(),obj.getprice().getchillichickenprice(),obj.getprice().getchillichickenprice()*obj.getDishcount().getchillichickencount())
                if(obj.getDishcount().getbluelagooncount()>0):
                    print(obj.getDishname().getbluelagoonname(),obj.getprice().getbluelagoonprice(),obj.getprice().getbluelagoonprice()*obj.getDishcount().getbluelagooncount())
                if(obj.getDishcount().getvirginmojitocount()>0):
                    print(obj.getDishname().getvirginmojitoname(),obj.getprice().getvirginmojitoprice(),obj.getprice().getvirginmojitoprice()*obj.getDishcount().getvirginmojitocount())
                if(obj.getDishcount().getwinecount()>0):
                    print(obj.getDishname().getwinename(),obj.getprice().getwineprice(),obj.getprice().getwineprice()*obj.getDishcount().getwinecount())
                print("Your current bill is ",obj.getcashier().getTotalBill())
                print("After discount is ",obj.getdiscount().discount(obj.getcashier().getTotalBill()))
                
                
class cashier():
    current_bill=0
    def updatebill(self,amt):
        self.current_bill=self.current_bill+amt
    def getTotalBill(self):
        return self.current_bill
        
class discount():
    def discount(self,amount):
        discount=amount/100*50
        Tbill=amount-discount
        print(Tbill)
        return Tbill
                
class objectfactory():
    h=Hotel()
    m=menu()
    s=Submenu()
    d=Dishname()
    p=price()
    dc=Dishcount()
    h=Handler()
    dis=discount()
    b=bill()
    c=cashier()
    def getHotel(self):
        return self.h
    def getmenu(self):
        return self.m
    def getSubmenu(self):
        return self.s
    def getDishname(self):
        return self.d
    def getprice(self):
        return self.p
    def getDishcount(self):
        return self.dc
    def getHandler(self):
        return self.h
    def getdiscount(self):
        return self.dis
    def getbill(self):
        return self.b
    def getcashier(self):
        return self.c
    
    
obj=objectfactory()
obj.getHandler().operations(obj)


# In[ ]:




