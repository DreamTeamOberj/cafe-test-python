import unittest
from machineACafe import MachineACafe

class TestPython(unittest.TestCase):
    global argent 
    argent = 40

    global machine 
    machine = MachineACafe()

    def test_coffee_coule(self):
        self.assertEqual(40, argent)
        self.assertTrue(machine.donnerGobelet())
        self.assertTrue(machine.servirCafe())

    def test_coffee_tasse(self):
        self.assertEqual(40, argent)
        self.assertFalse(machine.donnerGobelet())
        self.assertTrue(machine.servirCafe())

    def test_coffee_sucre(self):

        self.assertTrue(machine.sucreButton())
        self.assertTrue(machine.payerCafe(self, argent))
        self.assertTrue(machine.servirCafe())
        self.assertTrue(machine.ajoutSucre())

    def test_coffee_cancel(self):
        self.assertTrue(machine.cancelButton())
        self.assertFalse(machine.servirCafe())
        self.assertTrue(machine.rendreMonnaie(self, argent))

   


if __name__ == '__main__':
    unittest.main()
