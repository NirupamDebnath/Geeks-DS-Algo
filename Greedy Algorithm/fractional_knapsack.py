from collections import namedtuple
import unittest

Item = namedtuple("Item", ['value', 'weight'])


def max_possible_value(items, capacity = 50):
    items = sorted(items,key= lambda x: x.value / x.weight, reverse=True)
    res = 0
    i = 0
    while capacity > 0 and i<len(items):
        print(items[i])
        if items[i].weight < capacity:
            capacity -= items[i].weight
            res += items[i].value
        else:
            res += capacity * items[i].value / items[i].weight
            return res
        i += 1
    
    return res

class FractionalKnapsack_Test(unittest.TestCase):
    def test_1(self):
        given_items = [
            Item( 60, 10),
            Item( 100, 20),   
            Item( 120, 30),   
        ]

        self.assertEqual(max_possible_value(given_items), 240)

if __name__ == "__main__":
    unittest.main()
