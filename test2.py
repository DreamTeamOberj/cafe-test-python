import unittest
from machineACafe import MachineACafe

class TestPython(unittest.TestCase):
    global argent 
    argent = 40

    def test_coffee_coule(self):
        self.assertEqual(40, argent)
        self.assertTrue(MachineACafe.servirCafe())

    def test_coffee_tasse(self):

        self.assertEqual(40, argent)
        self.assertFalse(MachineACafe.donnerGobelet())

if __name__ == '__main__':
    unittest.main()
