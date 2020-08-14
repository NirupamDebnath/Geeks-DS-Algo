from collections import namedtuple
from operator import itemgetter

Job = namedtuple("Job", ["start","end"])

given_jobs = [  Job( 3, 8 ),
                Job( 2, 4 ),
                Job( 1, 3 ),
                Job( 10, 11 ), ]

given_jobs.sort(key=itemgetter(1))

def get_max_activities(jobs):
    res = [jobs[0]]
    for i in range(1,len(jobs)):
        if res[-1].end <= jobs[i].start:
            res.append(jobs[i])
    return res

print(*get_max_activities(given_jobs), sep="\n")
