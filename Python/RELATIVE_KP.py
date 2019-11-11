import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_file = "/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Analytic_Data/"
path_picture = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Pictures/'
# plt.style.use('classic')
graph_data_bulk = open(path_file + 'KPOINTS_bulk.txt', 'r').read()

lines_bulk = graph_data_bulk.split("\n")

graph_data_slab = open(path_file + 'KPOINTS_slab.txt', 'r').read()

lines_slab = graph_data_slab.split("\n")

KPOINTS = []


TOTEN_bulk = []
TOTEN_slab = []
start = time.time()
for i in range(len(lines_bulk)-1):
    if (i > 0 and i < len(lines_bulk)):
        splitted_lines_bulk = lines_bulk[i].split()
        splitted_lines_slab = lines_slab[i].split()
        c_bulk = list(map(float, splitted_lines_bulk))
        c_slab = list(map(float, splitted_lines_slab))
        KPOINTS.append(c_bulk[4])
        TOTEN_bulk.append(c_bulk[3])
        TOTEN_slab.append(c_slab[3])
end = time.time()
print ("Code time:", end - start)


print (TOTEN_bulk)
print("--------------------------")
print (TOTEN_slab)
print("--------------------------")
print ([x1 - x2 for (x1, x2) in zip(TOTEN_bulk, TOTEN_slab)])
RELATIVE = ([x1 - x2 for (x1, x2) in zip(TOTEN_bulk, TOTEN_slab)])

plt.figure(1)
plt.plot(KPOINTS, RELATIVE, linewidth=0.5, linestyle="-", marker="o", markersize=3.0)
#plt.legend(loc='upper right', prop={"size": 12})
plt.xlabel("KPOINTS", fontsize=14)
plt.ylabel('TOTEN [eV]', fontsize=14)
plt.title("Relative TOTEN of KPOINTS", fontsize=15)
plt.tight_layout()
plt.savefig(path_picture + "REL_KP_EN.eps", format='eps', dpi=1200)

plt.figure(2)
plt.plot(KPOINTS, RELATIVE, linewidth=0.5, linestyle="-", marker="o", markersize=3.0)
#plt.legend(loc='upper right', prop={"size": 12})
plt.xlabel("KPOINTS", fontsize=14)
plt.ylabel('Pressure [eV/Å]', fontsize=14)
plt.title("Relative Pressure of KPOINTS", fontsize=15)
plt.tight_layout()
plt.savefig(path_picture + "REL_KP_PR.eps", format='eps', dpi=1200)
plt.show()

for i in range(len(RELATIVE)-1):
    Delta = RELATIVE[i] - RELATIVE[i+1]
    if abs(Delta) <= 0.001:
        print ("Converged")
        # Set i+1 in ENCUT if it is not ex: 400-450, converges and then 400 is the number you shall use. If 450 is the case, then i+1
        print (KPOINTS[i])
        print (Delta)
    else:
        print ("Not converged")
        print (KPOINTS[i])

# According to print output, use 450eV aIs ENCUT
# According to print output, use KPOINT-density as 5.0 CORRECT
# Have now aquired desired results for ENCUT and KPOINTS.
