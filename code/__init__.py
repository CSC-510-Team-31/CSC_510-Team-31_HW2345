
import sys
print(sys.argv)
the={}
if len(sys.argv)>1:
    param=sys.argv[1]
    if param=="-e":
        the["e"]="nothing"
    elif param=="-d":
        the["d"]=False
    elif param=="-f":
        the["f"]=sys.argv[2]
    elif param=="-h":
        the["h"]=False
    elif param=="-n":
        the["n"]=512
        if len(sys.argv)>2:
            the["n"]=sys.argv[2]
    elif param=="-s":
        the["s"]=10019
    elif param=="-S":
        the["S"]=","
        if len(sys.argv)>2:
            the["n"]=sys.argv[2]


