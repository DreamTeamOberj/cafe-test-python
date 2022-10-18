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
        

if __name__ == '__main__':
    unittest.main()