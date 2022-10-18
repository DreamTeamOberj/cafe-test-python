import unittest

from machineACafe import MachineACafe

class TestMachine(unittest.TestCase):
    
    def test_coffee_coule(self):
        machine = MachineACafe()
        argentDepart = 40
        argent = argentDepart
        cafeDepart = machine.cafe
        gobeletsDepart = machine.gobelets
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(argent, (argentDepart - machine.prix))
        self.assertEqual(machine.cafe, (cafeDepart - 1))
        self.assertEqual(machine.gobelets, (gobeletsDepart - 1))
    
    def testRendreArgentNoCaf(self):
        machine = MachineACafe()
        argentDepart = 40
        argent = argentDepart
        machine.cafe = 0
        cafeDepart = machine.cafe
        gobeletsDepart = machine.gobelets
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, gobeletsDepart)
        self.assertEqual(machine.cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)


    def testRendreArgentNoGob(self):
        machine = MachineACafe()
        argentDepart = 40
        argent = argentDepart
        cafeDepart = machine.cafe
        machine.gobelets = 0
        gobeletsDepart = machine.gobelets
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, gobeletsDepart)
        self.assertEqual(machine.cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)
        
    def testRendreArgentNoEau(self):
        machine = MachineACafe()
        argentDepart = 40
        argent = argentDepart
        cafeDepart = machine.cafe
        gobeletsDepart = machine.gobelets
        machine.eau = False
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, gobeletsDepart)
        self.assertEqual(machine.cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)

    def test_quatre_piece(self):
        machine = MachineACafe()
        argentDepart = 80
        i = 0
        valueTot = 0
    
        for i in range(4) :
            valueTot = valueTot + 20
            machine.mettrePiece(20)

        self.assertEqual(valueTot, machine.rembourser(argentDepart))

    def testCafeValeur(self):
        machine = MachineACafe()
        argent = 40
        cafeDepart = machine.cafe
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.cafe, (cafeDepart - 1))
        
    def testGobValeur(self):
        machine = MachineACafe()
        argent= 40
        gobeletsDepart = machine.gobelets
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, (gobeletsDepart - 1))
        
    def testTasseDetectee(self):
        machine = MachineACafe()
        argent = 40
        cafeDepart = machine.cafe
        gobeletsDepart = machine.gobelets
        machine.tasseDetectee = True
        
        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, gobeletsDepart)
        self.assertEqual(machine.cafe, (cafeDepart - 1))
        
        
    def testRemettreGobelet(self):
        machine = MachineACafe()
        machine.gobelets = 50
        gobeletsAjout = 40
        
        gobeletApresAjout = machine.remettreGobelet(gobeletsAjout)
        
        self.assertEqual(90, gobeletApresAjout)
        
    def testRemettreCafe(self):
        machine = MachineACafe()
        machine.cafe = 50
        cafeAjout = 40
        
        cafeApresAjout = machine.remettreCafe(cafeAjout)
        
        self.assertEqual(90, cafeApresAjout)

    def testNotEnoughMoney(self):
        machine = MachineACafe()
        argentDepart = 30
        argent = argentDepart
        cafeDepart = machine.cafe
        gobeletsDepart = machine.gobelets

        argent = machine.payerCafe(argent)
        
        self.assertEqual(machine.gobelets, gobeletsDepart)
        self.assertEqual(machine.cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)

if __name__ == '__main__':
    unittest.main()