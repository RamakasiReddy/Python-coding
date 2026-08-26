class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name 
        self.salary= salary
        self.pincode= pincode
p = programmer("jahnavi",1200000,518165)
print(p.name,p.salary,p.pincode,p.company)
r = programmer("Rama Kasi",1200000,518165)
print(r.name,r.salary,r.pincode,r.company)
s = programmer("Gouse",1200000,516134)
print(s.name,s.salary,s.pincode,s.company)

