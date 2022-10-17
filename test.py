import unittest

from machineACafe import MachineACafe

class TestMachine(unittest.TestCase):

    def testRendreArgent(self):
        argentDepart = 40
        argent = argentDepart
        cafe = 0
        machine = MachineACafe()
        
        machine.payerCafe(argent)
        if cafe == 0:
            machine.rendreMonnaie(argent)
            print("Cafe is no more")
        else :
            machine.donnerGobelet()
            machine.servirCafe()
            print("Buvez bien")
        
        self.assertEqual(argent, argentDepart)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()