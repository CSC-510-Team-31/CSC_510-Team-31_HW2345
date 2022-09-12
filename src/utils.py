# all util functions

import math
import re


def copy(t):
    if not isinstance(t, dict):
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return dict(u)


def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    if p > len(t)-1:
        p=len(t)-1
    return t[max(1, min(len(t), p))]


# optional, we can just use round() function instead.
def rnd(x, places):
    mult = 10 ** (places or 2)
    return math.floor(x * mult + 0.5) / mult


def coerce(s: str):
    def fun(sl:str):
        if sl.strip().lower() == "true":
            return True
        if sl.strip().lower() == "false":
            return False
        return sl
    strToCheck = s.strip()
    if strToCheck.isnumeric():
        return int(strToCheck)
    else:
        try:
            return float(strToCheck)
        except ValueError:
            return fun(re.match("\s*(.*)\s*", strToCheck).string)


if __name__ == "__main__":
    print(rnd(1.23445, 2))
