import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_file = "/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Analytic_Data/"
# plt.style.use('classic')
graph_data = open(path_file + 'Slab_vakuum_layer.txt', 'r').read()

lines = graph_data.split("\n")
Layer = []

MxForce = []
Pressure = []
TOTEN = []

start = time.time()
for i in range(len(lines)-1):
    if (i > 0 and i < len(lines)):
        splitted_lines = lines[i].split()
        c = list(map(float, splitted_lines))
        Layer.append(c[4])
        MxForce.append(c[0])
        Pressure.append(c[2])
        TOTEN.append(c[3])

end = time.time()
print ("Code time:", end - start)


for i in range(len(TOTEN)-1):
    Delta = TOTEN[i] - TOTEN[i+1]
    if abs(Delta) <= 0.001:
        print ("Converged")

        print (Layer[i])
        print (Delta)
    else:
        print ("Not converged")
        print (Layer[i])
        print (Delta)

plt.figure(1)
plt.plot(Layer, MxForce, linewidth=0.5, linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Approximated solution of integral', fontsize=14)
plt.title("MxForce", fontsize=15)
# plt.tight_layout()

plt.figure(2)
plt.plot(Layer, Pressure, linewidth=0.5, color="tab:orange",
         linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Approximated solution of integral', fontsize=14)
plt.title("Pressure", fontsize=15)
# plt.tight_layout()

plt.figure(3)
plt.plot(Layer, TOTEN, linewidth=0.5, linestyle="-", marker="o", markersize=0.8)
#plt.legend(loc='upper right', prop={"size": 12})
#plt.xlabel("Number of iterations [N]", fontsize=14)
#plt.ylabel('Relative error $\epsilon$', fontsize=14)
plt.title("TOTEN", fontsize=15)
# plt.tight_layout()

plt.show()
