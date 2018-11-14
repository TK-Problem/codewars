import unittest


def format_words(words):
    # remove empty strings
    if isinstance(words, list):
        words = [_ for _ in words if _ != ""]
    else:
        return ""
    if len(words) == 1:
        return "".join(words)
    elif len(words) == 2 :
        return words[0] + " and " + words[1]
    else:
        return "".join([words[_]+", " if _ != len(words)-2 else words[_]+" and "+words[_+1] for _ in range(len(words)-1)])


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(format_words(['one', 'two', 'three', 'four']), 'one, two, three and four')

    def test_2(self):
        self.assertEqual(format_words(['one']), 'one')

    def test_3(self):
        self.assertEqual(format_words(['one', '', 'three']), 'one and three')

    def test_4(self):
        self.assertEqual(format_words(['', '', 'three']), 'three')

    def test_5(self):
        self.assertEqual(format_words(['one', 'two', '']), 'one and two')

    def test_6(self):
        self.assertEqual(format_words([]), '')

    def test_7(self):
        self.assertEqual(format_words(None), '')

    def test_8(self):
        self.assertEqual(format_words(['']), '')


if __name__ == '__main__':
    unittest.main()
