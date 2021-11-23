
class complex_number:
    def  __init__(self,i=0,r=0):
        self.Im=i
        self.Re=r
    
    def show(self):
        if self.Re<0:
            print(self.Im,self.Re,"i")
        else:
            print(self.Im,"+",self.Re,"i")
    
    def __add__(self,other):
        result=complex_number()
        result.Im=self.Im+other.Im
        result.Re=self.Re+other.Re
        return(result)

    def __sub__(self,other):
        result=complex_number()
        result.Im=self.Im-other.Im
        result.Re=self.Re-other.Re
        return(result)
    
    def __mul__(self,other):
        result=complex_number()
        result.Im=(self.Im*other.Im)-(self.Re*other.Re)
        result.Re=(self.Re*other.Im)+(self.Im*other.Re)
        return(result)
    

a=complex_number(5,7)
b=complex_number(2,9)

c=a+b
c.show()

c=a-b
c.show()

c=a*b
c.show()