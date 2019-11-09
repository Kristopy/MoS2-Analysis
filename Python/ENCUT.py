import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})

# plt.style.use('classic')
graph_data = open(
    '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Analytic_Data/ENCUT_bulk.txt', 'r').read()

lines = graph_data.split("\n")
ENCUT = []

MxForce = []
Pressure = []
TOTEN = []

start = time.time()
for i in range(len(lines)-1):
    if (i > 0 and i < len(lines)):
        splitted_lines = lines[i].split()
        c = list(map(float, splitted_lines))
        ENCUT.append(c[4])
        MxForce.append(c[0])
        Pressure.append(c[2])
        TOTEN.append(c[3])

end = time.time()
print ("Code time:", end - start)

plt.figure(1)
plt.plot(ENCUT, MxForce, linewidth=0.5, linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Approximated solution of integral', fontsize=14)
plt.title("MxForce", fontsize=15)
# plt.tight_layout()

plt.figure(2)
plt.plot(ENCUT, Pressure, linewidth=0.5, color="tab:orange",
         linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Approximated solution of integral', fontsize=14)
plt.title("Pressure", fontsize=15)
# plt.tight_layout()

plt.figure(3)
plt.plot(ENCUT, TOTEN, linewidth=0.5, linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Relative error $\epsilon$', fontsize=14)
plt.title("TOTEN", fontsize=15)
# plt.tight_layout()

plt.show()
