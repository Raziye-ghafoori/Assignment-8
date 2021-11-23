class time:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
        while self.second>60:
            self.second-=60
            self.minute+=1

        while self.minute>60:
            self.minute-=60
            self.hour+=1
            
    def show(self):
        print(self.hour,":",self.minute,":",self.second)

    def __add__(self,other):
        result=time()
        result.hour=self.hour+other.hour
        result.minute=self.minute+other.minute
        result.second=self.second+other.second
        while result.second>60:
            result.second-=60
            result.minute+=1

        while result.minute>60:
            result.minute-=60
            result.hour+=1

        return(result)

    def __sub__(self,other):
        result=time()
        result.hour=self.hour-other.hour
        result.minute=self.minute-other.minute
        result.second=self.second-other.second
        
        if result.hour<0 :
            result.hour*=-1
        if result.minute<0:
            result.minute*=-1
        if result.second<0:
            result.second*=-1
        return(result)
    
    def s2h(self,s):
        self.hour=s//3600
        s%=3600
        self.minute=s//60
        s%=60
        self.second=s

        self.show()
    
    def h2s(self):
        print((self.hour*3600)+(self.minute*60)+self.second)

h1=time(2,50,7)
h2=time(5,70,55)
h3=time()

print("hour to second:")
h1.h2s()
print("second to hour:")
h3.s2h(5800)
print("h1+h2:")
h4=h1+h2
h4.show()
print("h1-h2:")
h4=h1-h2
h4.show()