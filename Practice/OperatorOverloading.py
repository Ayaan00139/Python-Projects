class Vault:
    def __init__ (self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
        
    def __str__(self):
        return f"{self.galleons} {self.knuts} {self.sickles}"
    
    def __add__ (self,other):
        galleons=self.galleons+other.galleons
        knuts=self.knuts+other.knuts
        sickles=self.sickles+other.sickles
        return Vault(galleons,sickles,knuts)

potter=Vault(100,50,25)
print(potter)
wesly=Vault(25,50,100)
print(wesly)
total = potter + wesly
print(total)