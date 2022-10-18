import unittest

from machineACafe import MachineACafe

class TestMachine(unittest.TestCase):

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
        

if __name__ == '__main__':
    unittest.main()