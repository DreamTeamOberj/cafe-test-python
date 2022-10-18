import random
class MachineACafe():
    
    prix = 40
    
    def payerCafe(self, argent):
        argent = argent - self.prix
        return argent
    
    def rendreMonnaie(self, argent):
        argent = argent + self.prix
        return argent
    
    def nombreGobelets(gobelets):
        return gobelets
    
    def servirCafe():
        print("Le cafe est servi !")
        return True

    def donnerGobelet():
        gobelets = random.randint(1,10)
        gobelets = gobelets - 1
        print("Il reste " + str(gobelets) + " gobelets")
        return True

    def sucreButton():
        pass

    def ajoutSucre():
        pass
        
    def cancelButton():
        pass