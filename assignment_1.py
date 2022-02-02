import re
import pprint

ss = "Software version : v2.3.0\nMainline Version: V2.3\nRelease Date: 12.11.2021\nBuild info:\nBuild Number: 121123"

parentKey = ""
dd = {}
for substring in re.split("\n", ss):
    item = re.split(":",substring)
    item[0] = item[0].strip()
    item[1] = item[1].strip()
    if re.findall("^[0-9]*$", item[1]) != [] and item[1] != "":
        item[1] = int(item[1])
    if item[1] == "":
        parentKey = item[0]
    else:
        if parentKey != "":
            dd[parentKey] = {item[0]:item[1]}
            parentKey = ""
        else:
            dd[item[0]] = item[1]

pprint.pprint(dd)
