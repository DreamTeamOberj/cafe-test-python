import random
class MachineACafe():
    
    prix = 40
    cafe = 100
    gobelets = 100
    
    def payerCafe(self, argent):
        argent = self.operations(argent)
        return argent
    
    def rendreMonnaie(self, argent):
        argent = argent + self.prix
        return argent
    
    def nombreGobelets(self):
        return self.gobelets
    
    def operations(self, argent):
        if self.gobelets == 0:
            print("Plus de gobelets")
            self.rendreMonnaie(argent)
        elif self.cafe == 0:
            print("Plus de café")
            self.rendreMonnaie(argent)
        else:         
            self.donnerGobelet()
            self.servirCafe()
        
        return argent

    def servirCafe(self):
        self.cafe = self.cafe - 1
        print("Le cafe est servi ! Il en reste " + str(self.cafe))
    
    def donnerGobelet():
        gobelets = gobelets - 1
        print("Il reste " + gobelets + " gobelets")
        return True
        