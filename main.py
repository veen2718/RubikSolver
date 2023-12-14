from cube import cube
from display import doMainLoop
import numpy as np

import json #For debugging using json.dump
def dump(x,n=4):
    print(json.dumps(x,indent=n))



x = cube()
dump(x.contents)
print("\n\n\n")
#x.F()
#x.F()
dump(x.contents)
x.draw()



doMainLoop()
