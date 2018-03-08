import unittest

def fb(i):

    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i == 100:
        return "Bam!"
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return str(i)

class fbUnit(unittest.TestCase):

    def fbUnit(self):
        self.assertEqual(fb(3), "Fizz")
        self.assertEqual(fb(5), "Buzz")
        self.assertEqual(fb(15), "FizzBuzz")
        self.assertEqual(fb(100), "Bam!")
        self.assertEqual(fb(23), 23)
        self.assertEqual(fb(91), 91)


print "\n".join(fb(n) for n in xrange(1, 101))
