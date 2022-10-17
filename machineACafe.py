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
    
    def donnerGobelet():
        gobelets = gobelets - 1
        print("Il reste " + gobelets + " gobelets")
        