import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_file = "/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Analytic_Data/"
path_picture = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Pictures/'

graph_data_bulk = open(path_file + 'CPU_time_ENCUT_bulk.txt', 'r').read()
lines_bulk = graph_data_bulk.split("\n")

graph_data_slab = open(path_file + 'CPU_time_ENCUT_slab.txt', 'r').read()
lines_slab = graph_data_slab.split("\n")

graph_data_bulk_KPOINTS = open(path_file + 'CPU_time_KPOINTS_bulk.txt', 'r').read()
lines_bulk_KPOINTS = graph_data_bulk_KPOINTS.split("\n")

graph_data_slab_KPOINTS = open(path_file + 'CPU_time_KPOINTS_slab.txt', 'r').read()
lines_slab_KPOINTS = graph_data_slab_KPOINTS.split("\n")


ENCUT = []
KPOINST = []

CPU_bulk_CutOff = []
CPU_slab_Cutoff = []

CPU_bulk_KPOINTS = []
CPU_slab_KPOINTS = []

# For CutOff energies
for i in range(len(lines_bulk)-1):
    if (i > 0 and i < len(lines_bulk)):
        splitted_lines_bulk = lines_bulk[i].split()
        splitted_lines_slab = lines_slab[i].split()
        c_bulk = list(map(float, splitted_lines_bulk))
        c_slab = list(map(float, splitted_lines_slab))
        ENCUT.append(c_bulk[0])
        CPU_bulk_CutOff.append(c_bulk[1])
        CPU_slab_Cutoff.append(c_slab[1])
end = time.time()

# For KPOINTS densities
for i in range(len(lines_bulk_KPOINTS)-1):
    if (i > 0 and i < len(lines_bulk_KPOINTS)):
        splitted_lines_bulk_KPOINTS = lines_bulk_KPOINTS[i].split()
        splitted_lines_slab_KPOINTS = lines_slab_KPOINTS[i].split()
        c_bulk_KPOINTS = list(map(float, splitted_lines_bulk_KPOINTS))
        c_slab_KPOINTS = list(map(float, splitted_lines_slab_KPOINTS))
        KPOINST.append(c_bulk_KPOINTS[0])
        CPU_bulk_KPOINTS.append(c_bulk_KPOINTS[1])
        CPU_slab_KPOINTS.append(c_slab_KPOINTS[1])

# Figure Containing ENCUT
plt.figure(1)
plt.plot(ENCUT, CPU_bulk_CutOff, linewidth=0.5, linestyle="-",
         marker="o", markersize=3.0, label="$MoS_2-bulk$")
plt.plot(ENCUT, CPU_slab_Cutoff, linewidth=0.5, linestyle="-",
         marker="o", markersize=3.0, label="$MoS_2-slab$")
plt.legend(loc='upper left', prop={"size": 12})
plt.xlabel("ENCUT [eV]", fontsize=14)
plt.ylabel('CPU-time [s]', fontsize=14)
plt.title("CPU-time for bulk $\\&$ slab", fontsize=15)
plt.tight_layout()
plt.savefig(path_picture + "CPU_EN.eps", format='eps', dpi=1200)

# Figure Containing KPOINTS
plt.figure(2)
plt.plot(KPOINST, CPU_bulk_KPOINTS, linewidth=0.5, linestyle="-",
         marker="o", markersize=3.0, label="$MoS_2-bulk$")
plt.plot(KPOINST, CPU_slab_KPOINTS, linewidth=0.5, linestyle="-",
         marker="o", markersize=3.0, label="$MoS_2-slab$")
plt.legend(loc='upper left', prop={"size": 12})
plt.xlabel("KPOINTS", fontsize=14)
plt.ylabel('CPU-time [s]', fontsize=14)
plt.title("CPU-time for bulk $\\&$ slab", fontsize=15)
plt.tight_layout()
plt.savefig(path_picture+"CPU_KP.eps", format='eps', dpi=1200)

plt.show()
