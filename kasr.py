

class kasr :
    def __init__(self,s=0,m=1):
        self.sorat=s
        self.makhraj=m
    
    def simple(self):
        resultsorat=self.sorat
        resultmakharj=self.makhraj

        for i in range(2,10):    
            if resultsorat%i==0 and resultmakharj%i==0:
                resultsorat//=i
                resultmakharj//=i
                       
        return(resultsorat,resultmakharj)

    def __add__(self ,other):
        result=(self.sorat*other.makhraj)+(self.makhraj*other.sorat)
        return (result,self.makhraj*other.makhraj)
        

    def __sub__(self ,other):
        result=(self.sorat*other.makhraj)-(self.makhraj*other.sorat)
        return (result,self.makhraj*other.makhraj)
    
    def __mul__(self , other):
        return(self.sorat * other.sorat ,self.makhraj * other.makhraj)
    
    def __truediv__(self , other):
        return(self.sorat * other.makhraj ,self.makhraj * other.sorat)


k1=kasr(3,5)
k2=kasr(5,8)
k3=kasr(6,5)
k4=kasr(8,16)


print("Add")
print(k1+k2)
print("subtract")
print(k1-k3)
print("multiply")
print(k1*k2)
print("divide")
print(k1/k2)
print("simplification")
print(k4.simple())


