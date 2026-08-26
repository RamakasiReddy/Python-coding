from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def book(self, fro ,to):
        print(f"your ticket booked successfully in train no{self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"your train is rrunning on time {self.trainNo}")
    def getfare(self, fro , to ):
        print(f"your ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train(12)
t.book("san","kanala")
t.getStatus()
t.getfare("san","kanala")
