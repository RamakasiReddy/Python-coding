class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"the square of your number is: {self.n*self.n}") 
    def cube(self):
        print(f"the cbe of a number is :{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square root of your number is :{self.n**(1/2)}")

    def greet(self):
        print("Hello there !")



s = int(input("Enter the number you want : " ))
a = calculator(s)
a.greet()
a.square()
a.cube()
a.squareroot()

