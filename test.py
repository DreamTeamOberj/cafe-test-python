import unittest

from machineACafe import MachineACafe

class TestMachine(unittest.TestCase):

    def testRendreArgentNoCaf(self):
        machine = MachineACafe()
        argentDepart = 40
        cafeDepart = 0
        gobeletsDepart = machine.gobelets
        argent = argentDepart
        cafe = cafeDepart
        gobelets = gobeletsDepart
        
        machine.payerCafe(argent)
        if cafe == 0:
            machine.rendreMonnaie(argent)
        
        self.assertEqual(gobelets, gobeletsDepart)
        self.assertEqual(cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)

    def testRendreArgentNoGob(self):
        machine = MachineACafe()
        argentDepart = 40
        cafeDepart = machine.cafe
        gobeletsDepart = 0
        argent = argentDepart
        cafe = cafeDepart
        gobelets = gobeletsDepart
        
        machine.payerCafe(argent)
        if gobelets == 0:
            machine.rendreMonnaie(argent)
        
        self.assertEqual(gobelets, gobeletsDepart)
        self.assertEqual(cafe, cafeDepart)
        self.assertEqual(argent, argentDepart)
        

if __name__ == '__main__':
    unittest.main()