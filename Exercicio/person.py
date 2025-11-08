class Person:
    name= "Alex"
    age = 0
    def toString (self) :
        return self.name+", "+str(self.age)+"a."
    def __str__(self) : 
        return self.name+" ["+str(self.age)+"]" 
    def yearsToMajority(self) :
        return 0 if self.age>17 else 18-self.age
    
    
p1 = Person ()
print(p1)
print(p1.yearsToMajority())