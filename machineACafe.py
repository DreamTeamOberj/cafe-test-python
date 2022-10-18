class MachineACafe():
    
    prix = 40
    cafe = 100
    gobelets = 100
    eau = True
    tasseDetectee = False

    def mettrePiece(self, valeur):
        pieces = 0
        valueTot = 0
        if pieces <= 4 :
            pieces = pieces + 1
            valueTot = valueTot + valeur
        else :
            self.rembourser(valueTot)

    def payerCafe(self, argent):
        argent -= self.prix
        argent = self.operations(argent)
        return argent
    
    def rembourser(self, argent):
        return argent

    
    def operations(self, argent):
        if self.gobelets == 0:
            print("\nPlus de gobelets !")
            argent = self.rembourser(argent)
        elif self.cafe == 0:
            print("\nPlus de café !")
            argent = self.rembourser(argent)
        elif self.eau == False:
            print("\nPas d'eau !")
            argent = self.rembourser(argent) 
        else:
            if self.tasseDetectee == False:  
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
    
