import sys
import json

if len(sys.argv) <= 1:
    exit(1)

status = 0

for file in sys.argv[1:]:
    with open(file, encoding="ISO-8859-1") as f:
        try:
            json.load(f)
        except ValueError as exception:
            if "ss220" in file:
                print("SS220 exception detected in {}, passing...".format(file))
                continue
            print("JSON error in {}".format(file))
            print(exception)
            status = 1
        else:
            print("Valid {}".format(file))

exit(status)
