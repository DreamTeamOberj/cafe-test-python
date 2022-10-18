class MachineACafe():
    
    prix = 40
    cafe = 100
    gobelets = 100
    
    def payerCafe(self, argent):
        argent = argent - self.prix
        return argent
    
    def rendreMonnaie(self, argent):
        argent = argent + self.prix
        return argent
    
    def nombreGobelets(self):
        return self.gobelets
    
    def servirCafe(self):
        self.cafe = self.cafe - 1
        print("Le cafe est servi !")
    
    def donnerGobelet(self):
        self.gobelets = self.gobelets - 1
        print("Il reste " + str(self.gobelets) + " gobelets")
        