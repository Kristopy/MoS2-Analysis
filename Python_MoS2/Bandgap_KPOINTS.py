import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_file = "/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Analytic_Data/"
path_picture = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Pictures/'

graph_data_bulk = open(path_file + 'Bandgap_KPOINTS_bulk.txt', 'r').read()

lines_bulk = graph_data_bulk.split("\n")

graph_data_slab = open(path_file + 'Bandgap_KPOINTS_slab.txt', 'r').read()

lines_slab = graph_data_slab.split("\n")

#KPOINTS = []
Cutoff = []

Gap_bulk = []
Band_bulk = []
Vbm_bulk = []
Cbm_bulk = []

Gap_slab = []
Band_slab = []
Vbm_slab = []
Cbm_slab = []

start = time.time()
for i in range(len(lines_bulk)-1):
    if (i > 0 and i < len(lines_bulk)-1):
        splitted_lines = lines_bulk[i].split()
        c = list(map(float, splitted_lines))
        Gap_bulk.append(c[0])  # First element x-values
        Band_bulk.append(c[1])  # second element u(x)
        Vbm_bulk.append(c[2])  # third element v(x))
        Cbm_bulk.append(c[3])  # fourth element relative error
        Cutoff.append(c[4])


for i in range(len(lines_slab)-1):
    if (i > 0 and i < len(lines_slab)-1):
        splitted_lines = lines_slab[i].split()
        c = list(map(float, splitted_lines))
        Gap_slab.append(c[0])  # First element x-values
        Band_slab.append(c[1])  # second element u(x)
        Vbm_slab.append(c[2])  # third element v(x))
        Cbm_slab.append(c[3])  # fourth element relative error
end = time.time()

print ("Code time:", end - start)

"""
List_conv = [y - x for x, y in zip(Gap, Gap[1:-1])]
List_pos = np.abs(List_conv)
print (List_pos)

For KPOINTS:

plt.figure(1)
plt.plot(k_points, List_pos[:6], "--o", linewidth=1)
# plt.plot(x, v, linewidth=1, linestyle="--", label='Numerical solution')
# plt.legend(loc='right', prop={"size": 10})
plt.xlabel("k-point density")
plt.ylabel('Bandgap convergence [eV]')
plt.title("Bandgap convergence as a function of the k-point density")
"""
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(Cutoff, Gap_bulk, "--o", linewidth=1, markersize=2, label="Bulk")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("KPOINTS")
plt.ylabel('Band gap [eV]')
plt.title("Bandgap vs KPOINTS [BULK]")
plt.subplot(2, 1, 2)
plt.plot(Cutoff, Gap_slab, "--o", color="orange", linewidth=1, markersize=2, label="Slab")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("KPOINTS")
plt.ylabel('Band gap [eV]')
plt.title("Bandgap vs KPOINTS [SLAB]")
plt.tight_layout()
plt.savefig(path_picture + "Bandgap_KP.eps", format='eps', dpi=1200)

"""
plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(Cutoff, Vbm_bulk, "--o", linewidth=1, label="Bulk")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("Energy Cutoff [eV]")
plt.ylabel('VBM')
plt.title("Energy cutoff vs total energy [BULK]")
plt.subplot(2, 1, 2)
plt.plot(Cutoff, Vbm_slab, "--o", color="orange", linewidth=1, label="Slab")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("Energy Cutoff [eV]")
plt.ylabel('VBM')
plt.title("Energy cutoff vs total energy [SLAB]")
plt.tight_layout()

plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(Cutoff, Cbm_bulk, "--o", linewidth=1, label="Bulk")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("Energy Cutoff [eV]")
plt.ylabel("CBM")
plt.title("Energy cutoff vs maximum force [BULK]")
plt.subplot(2, 1, 2)
plt.plot(Cutoff, Cbm_slab, "--o", color="orange",  linewidth=1, label="Slab")
plt.legend(loc='upper right', prop={"size": 10})
plt.xlabel("Energy Cutoff [eV]")
plt.ylabel("CBM")
plt.title("Energy cutoff vs maximum force [SLAB]")
plt.tight_layout()
"""
plt.show()
