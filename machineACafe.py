import random

from sqlalchemy import true
class MachineACafe():
    
    prix = 40
    cafe = 100
    gobelets = 100
    eau = True
    
    def payerCafe(self, argent):
        argent = self.operations(argent)
        return argent
    
    def rembourser(self, argent):
        argent = argent + self.prix
        return argent

    
    def operations(self, argent):
        if self.gobelets == 0:
            print("\nPlus de gobelets !")
            self.rembourser(argent)
        elif self.cafe == 0:
            print("\nPlus de café !")
            self.rembourser(argent)
        elif self.eau == False:
            print("\nPas d'eau !")
            self.rembourser(argent)
            
        else:         
            self.donnerGobelet()
            self.servirCafe()
        
        return argent

    def servirCafe(self):
        self.cafe = self.cafe - 1
        print("\nLe cafe est servi ! Il en reste " + str(self.cafe))
    
    def donnerGobelet(self):
        self.gobelets = self.gobelets - 1
        print("\nIl reste " + str(self.gobelets) + " gobelets")
        return True
        