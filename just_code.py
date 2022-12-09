import json
import sys


jsonf = json.load(open(sys.argv[-1]))

for cell in jsonf["cells"]:
    if cell["cell_type"] == "code":
        for line in cell["source"]:
            print(line)
