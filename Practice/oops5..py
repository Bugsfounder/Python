"""
WRITE A CLASS TRAIN WHICH HAS METHODS TO BOOK A TICKET, GET STATUS (NO OF SEATS) AND
GET FARE INFORMATION OF TRAINS RUNNING
"""


class Train:
    def __init__(self, name, fare, seats):
        self.cancel = None
        self.name = name
        self.fare = fare
        self.seats = seats
        self.cancel = self.cancel

    def bookTicket(self):
        if self.seats > 0:
            print("Your Seat has been Booked")
            self.seats = self.seats - 1
        else:
            print("Sorry All Seats are Full")

    def cancelTicket(self, seatNo):
        print("Your seat has been canceled")
        self.seats = self.seats + 1


def getStatus(self):
    print("*******************")
    print(f"The Name of Train is: {self.name}")
    print(f"The Seats are available {self.seats}")
    print("*******************")


def getFareInfo(self):
    print("*******************")
    print(f"The Price of Ticket is: {self.fare}")
    print("*******************")


tc = Train("Express", 10, 1)
tc.bookTicket()
tc.bookTicket()
tc.cancelTicket(2)
tc.bookTicket()
