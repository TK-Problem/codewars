import unittest


def validate(domain):
    if len(domain.split(".")) == 1 or len(domain.split(".")) > 127 or len(domain) > 253:
        return False
    if domain[0] == "." or domain[-1] == ".":
        return False
    try:
        int(domain.split(".")[-1])
        return False
    except:
        pass
    for s in domain.split("."):
        if len(s)>=1:
            if s[0] == "-" or s[-1] == "-" or s[0] == "_":
                return False
        else:
            return False
        if len(s)>=63:
            return False
        if "@" in s:
            return False
        if not all(ord(c) < 128 for c in s):
            return False
    return True


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(not validate('codewars'), True)

    def test_2(self):
        self.assertEqual(validate('g.co'), True)

    def test_3(self):
        self.assertEqual(validate('codewars.com'), True)

    def test_4(self):
        self.assertEqual(validate('CODEWARS.COM'), True)

    def test_5(self):
        self.assertEqual(validate('sub.codewars.com'), True)

    def test_6(self):
        self.assertEqual(not validate('codewars.com-'), True)

    def test_7(self):
        self.assertEqual(not validate('.codewars.com'), True)

    def test_8(self):
        self.assertEqual(not validate('example@codewars.com'), True)

    def test_9(self):
        self.assertEqual(not validate('127.0.0.1'), True)


if __name__ == '__main__':
    unittest.main()
    # print(validate('sub.codewars.com'))
