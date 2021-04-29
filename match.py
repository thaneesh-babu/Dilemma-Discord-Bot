# developing an algo for matching two names

import random

# cmd format: .match <person1>, <person2>

def matchingAlgo(cmd):
    cmd = cmd[7:]
    lstofnames = cmd.split(',')
    n1, n2 = lstofnames
    n2 = n2.strip()
    lst = [len(n1), len(n2)]
    p, c = 0.0, 0

    for ch in n1:
        if ch in n2:
            c += 1
    p = round((c*100)/max(lst),2)
    if p==0.00:
        p += random.uniform(0,15)
    elif p>98.00:
        p -= random.uniform(0,10)
    else:
        p = p + random.uniform(0,10) - random.uniform(0,10)

    return(str(round(p, 2)) + "%")



