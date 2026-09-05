class twoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the 2D Vector is {self.i}i + {self.j}j")

class ThreeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"the 3D Vector is {self.i}i + {self.j}j + {self.k}k")

twovec = twoDVector(1,2)
twovec.show()
threevec = ThreeDVector(7,9,9)
threevec.show()