import subprocess
import json

alt = 0
mach = 0.5
zxn = 1

proc = subprocess.check_output('curl -d "alt={alt}&mach={mach}&zxn={zxn}" http://192.168.1.32:3030/v1/api/perf/'.format(alt=alt, mach=mach, zxn=zxn))

dict_ = ((json.loads(proc))[0])

Thrust = dict_["Thrust (kN)"]
SFC = dict_["TSFC (g/kN.s)"]
EGT = dict_["EGT (K)"]
T2 = dict_["T2 (K)"]
T3 = dict_["T3 (K)"]
P2 = dict_["P2 (kPa)"]
P3 = dict_["P3 (kPa)"]
Wf = dict_["Wf (kg/s)"]
T8 = dict_["St8Tt (K)"]


