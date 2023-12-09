from cube import cube

import json #For debugging using json.dump

x = cube()
print(json.dumps(x.contents,indent=4))