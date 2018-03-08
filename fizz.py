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
        self.assertEqual(fizz(3), "Fizz")
        self.assertEqual(fizz(5), "Buzz")
        self.assertEqual(fizz(15), "FizzBuzz")
        self.assertEqual(fizz(100), "Bam!")
        self.assertEqual(fizz(1), 1)
        self.assertEqual(fizz(4), 4)


print "\n".join(fb(n) for n in xrange(1, 101))
