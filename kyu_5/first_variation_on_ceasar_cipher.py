import unittest


def moving_shift(s, shift):
    if len(s.split(" ")) % 5 == 0:
        tick = len(s.split(" "))//5
        return [" ".join(s.split(" ")[_*tick:(_+1)*tick]) for _ in range(5)]
    elif len(s.split(" ")) % 4 == 0:
        tick = len(s.split(" "))//4
        return [" ".join(s.split(" ")[_*tick:(_+1)*tick]) for _ in range(5)]
        # return [(_*tick,(_+1)*tick) for _ in range(5)]

def demoving_shift(s, shift):
    pass


# Testsing
class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(moving_shift("I should have known that you would have a perfect answer for me!!!", 1),
                         ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"])

if __name__ == '__main__':
    # print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1))
    # unittest.main()

    for _ in range(1,20):
        if _%5==0:
            print("{}: five".format(_))
        elif _%4==0:
            print("{}: four".format(_))
        else:
            print("{}: {}".format(_, _/4))