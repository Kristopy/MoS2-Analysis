import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})

# plt.style.use('classic')
graph_data_bulk = open(
    '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Analytic_Data/CORRECT/ENCUT_bulk.txt', 'r').read()

lines_bulk = graph_data_bulk.split("\n")

graph_data_slab = open(
    '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Analytic_Data/CORRECT/ENCUT_slab_5_C_Vakuum.txt', 'r').read()

lines_slab = graph_data_slab.split("\n")

ENCUT = []


TOTEN_bulk = []
TOTEN_slab = []

MxForce_bulk = []
MxForce_slab = []

Pressure_bulk = []
Pressure_slab = []

start = time.time()
for i in range(len(lines_bulk)-1):
    if (i > 0 and i < len(lines_bulk)):
        splitted_lines_bulk = lines_bulk[i].split()
        splitted_lines_slab = lines_slab[i].split()
        c_bulk = list(map(float, splitted_lines_bulk))
        c_slab = list(map(float, splitted_lines_slab))
        ENCUT.append(c_bulk[4])
        TOTEN_bulk.append(c_bulk[3])
        TOTEN_slab.append(c_slab[3])
        MxForce_bulk.append(c_bulk[0])
        MxForce_slab.append(c_slab[0])
        Pressure_bulk.append(c_bulk[2])
        Pressure_slab.append(c_slab[2])
end = time.time()
print ("Code time:", end - start)

print("----------------------------------------------------")
print ("Total energy bulk")
print("----------------------------------------------------")
print (TOTEN_bulk)
print("----------------------------------------------------")
print ("Total energy slab")
print("----------------------------------------------------")
print (TOTEN_slab)
print("----------------------------------------------------")
print ("Total Relative energy for bulk and slab")
print("----------------------------------------------------")
print ([x1 - x2 for (x1, x2) in zip(TOTEN_bulk, TOTEN_slab)])
print("----------------------------------------------------")
RELATIVE_EN = ([x1 - x2 for (x1, x2) in zip(TOTEN_bulk, TOTEN_slab)])
RELATIVE_MX = ([x1 - x2 for (x1, x2) in zip(MxForce_bulk, MxForce_slab)])
RELATIVE_PR = ([x1 - x2 for (x1, x2) in zip(Pressure_bulk, Pressure_slab)])


for i in range(len(RELATIVE_EN)-1):
    Delta_EN = RELATIVE_EN[i] - RELATIVE_EN[i+1]
    Delta_MX = RELATIVE_MX[i] - RELATIVE_MX[i+1]
    Delta_PR = RELATIVE_PR[i] - RELATIVE_PR[i+1]
    if (abs(Delta_EN) <= 0.001 and (abs(Delta_MX) <= 0.5) and (abs(Delta_PR)) <= 0.5):
        print ("Converged")
        # Set i+1 in ENCUT if it is not ex: 400-450, converges and then 400 is the number you shall use. If 450 is the case, then i+1
        print (ENCUT[i])
        print ("       Relative EN                Relative MX                Relative PR")
        print (Delta_EN, "     ", Delta_MX, "    ", Delta_PR)
    else:
        print ("Not converged")
        print (ENCUT[i])
# According to print output, use 650eV as ENCUT

plt.figure(1)
plt.plot(ENCUT, RELATIVE_EN, linewidth=0.5, linestyle="-", marker="o", markersize=3.0)
plt.xlabel("ENCUT [eV]", fontsize=14)
plt.ylabel('TOTEN [eV]', fontsize=14)
plt.title("Relative TOTEN", fontsize=15)
plt.tight_layout()
plt.savefig("/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Pictures/REL_EN.png")

plt.figure(2)
plt.plot(ENCUT, RELATIVE_PR, linewidth=0.5, color="tab:orange")
plt.xlabel("ENCUT [eV]", fontsize=14)
plt.ylabel('Pressure [eV/Å]', fontsize=14)
plt.title("Relative Pressure", fontsize=15)
plt.savefig("/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Pictures/REL_PR.png")

plt.figure(3)
plt.plot(ENCUT, RELATIVE_MX, linewidth=0.5, linestyle="-", marker="o", markersize=0.8)
plt.xlabel("ENCUT [eV]", fontsize=14)
plt.ylabel('Force [eV]', fontsize=14)
plt.title("Relative MxForce", fontsize=15)
plt.savefig("/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/Lab_Project/Pictures/REL_MX.png")

plt.show()
