class Train:
    def __init__(self,tno=0,tname="null",seat=0):
        self.tname=tname
        self.tno=tno
        self.seats=seat
    def display(self):
        print("%d:%s has %d seats"%(self.tno,self.tname,self.seats))
    def reserv(self):
        print(self.tname)
        self.b=int(input("Enter the seat count for booking:"))
        self.seats-=self.b
        print("%d seats of %s is reserved"%(self.b,self.tname))
    def cancel(self):
        print(self.tname)
        self.c=int(input("Enter the seat count for cancel:"))
        self.seats+=self.c
        print("%d seats of %s cancelled"%(self.c,self.tname))


print("Available Trains and Seats")
print("--------------------------")
t1=Train(1,"Duronto Express",10)
t2=Train(2,"Jan Shatabdi Express",12)
t3=Train(3,"Rajadhani Express",3)
t1.display()
t2.display()
t3.display()
print("---------------------------")
for i in range(1,10):
    print("1.Ticket Booking  2.Cancel booking  3.Display Train Details ")
    a=int(input("Enter choice:"))
    if a==1:
        b=int(input("Enter the Train No:"))
        if b==
        1:
              t1.reserv()
              print("---------------------------")
        elif b==2:
              t2.reserv()
              print("---------------------------")
        else:
              t3.reserv()
              print("---------------------------")

    elif a==2:
        b=int(input("Enter the Train No:"))
        if b==1:
              t1.cancel()
              print("---------------------------")

        elif b==2:
              t2.cancel()
              print("---------------------------")

        else:
              t3.cancel()
              print("---------------------------")

    else:
        print("Available Trains and Seats")
        print("--------------------------")
        t1.display()
        t2.display()
        t3.display()
        print("---------------------------")



    
