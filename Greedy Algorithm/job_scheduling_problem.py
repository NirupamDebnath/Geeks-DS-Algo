from collections import namedtuple
from operator import attrgetter
import unittest

Job = namedtuple("Job", ["id","deadline","profit"])

def get_max_profit_schedule(jobs, t):
    jobs = sorted(jobs, key= attrgetter("profit"), reverse=True)

    result = [False] * t

    res_jobs = ['-'] * t

    for i in range(len(jobs)):
        for j in range(min(t - 1, jobs[i].deadline-1), -1, -1):
            if result[j] == False:
                result[j] = True
                res_jobs[j] = jobs[i].id
                break

    return res_jobs

class Test_Max_Profit(unittest.TestCase):
    def test_1(self):
        given_jobs = [
            Job( 'a', 2, 100),
            Job( 'b', 1, 19),
            Job( 'c', 2, 27),
            Job( 'd', 1, 25),
            Job( 'e', 3, 15),
        ]

        self.assertEqual(get_max_profit_schedule(given_jobs, 3),
                                ['c', 'a', 'e'])

if __name__ == "__main__":
    unittest.main()

