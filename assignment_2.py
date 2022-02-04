import re
from subprocess import Popen, PIPE
import  json

def getCmdOut(cmd):
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    stdout = stdout.decode("utf-8")
    stdout = stdout.strip()

    return stdout, stderr

if __name__ == "__main__":

    cmd = ["ps", "aux"]
    OutData, Err = getCmdOut(cmd)
    AllData = []
    OutData = OutData.splitlines()
    for item in OutData[1:]:
        EachLine = re.split(r"\s",item)
        EachLine = " ".join(EachLine).split()
        EachLine[10] = " ".join(EachLine[10:])

        USER = EachLine[0]
        PID = int(EachLine[1])
        CPU = float(EachLine[2])
        MEM = float(EachLine[3])
        VSZ = int(EachLine[4])
        RSS = int(EachLine[5])
        TTY = EachLine[6]
        STAT = EachLine[7]
        START = EachLine[8]
        TIME = EachLine[9]
        COMMAND = EachLine[10]

        EachData = {PID:{"USER":USER, "%CPU":CPU, "%MEM":MEM, "VSZ":VSZ, "RSS":RSS, "TTY":TTY, "STAT":STAT, "START":START, "TIME":TIME, "COMMAND":COMMAND}}

        print(EachData)
        AllData.append(EachData)

