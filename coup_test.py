import unittest
import action
from player import Player


class CoupTests(unittest.TestCase):

    def capt_test(self):
        capt = action.Captain()
        p1 = Player(1)
        p2 = Player(2)
        capt.effect(p1, p2)
        self.failif(p1.coins != 4)
        self.failif(p2.coins != 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()



