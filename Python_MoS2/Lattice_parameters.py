import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_file = "/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Analytic_Data/"
# plt.style.use('classic')
graph_data = open(path_file + 'Lattice_parameters.txt', 'r').read()
path_picture = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Pictures/'
lines = graph_data.split("\n")
Number_Calc = []

a = []
c_par = []
start = time.time()
for i in range(len(lines)-1):
    if (i > 0 and i < len(lines)):
        splitted_lines = lines[i].split()
        c = list(map(float, splitted_lines))
        Number_Calc.append(c[0])
        a.append(c[1])
        c_par.append(c[2])

end = time.time()
print ("Code time:", end - start)
Ratio = []
for i in range(len(Number_Calc)):
    Ratio.append(c_par[i]/a[i])

plt.figure(1)

plt.subplot(2, 1, 1)
plt.margins(0)
plt.plot(Number_Calc, c_par, linewidth=0.8, linestyle="--", label='c-parameter')
plt.legend(loc='lower left', prop={"size": 12})
plt.ylabel('length of c [Å]', fontsize=16)
plt.title("Length of lattice parameters a and c during relaxation", fontsize=17)
plt.subplot(2, 1, 2)
plt.margins(0)
plt.plot(Number_Calc, a, linewidth=0.8, linestyle="--", color='C1',  label='a-parameter')
plt.legend(loc='upper left', prop={"size": 12})
plt.xlabel("Number of iterations", fontsize=16)
plt.ylabel('length of a [Å]', fontsize=16)
plt.tight_layout()
plt.savefig(path_picture + "c_a_plot.eps", format='eps', dpi=1200)
plt.figure(2)
plt.margins(0)
plt.plot(Number_Calc, Ratio, linewidth=0.8, linestyle="--", color="C3",  label='c/a-ratio')
plt.legend(loc='upper right', prop={"size": 12})
plt.xlabel("Number of iterations",  fontsize=16)
plt.ylabel('c/a- ratio',  fontsize=16)
plt.title("c/a-ratio as a function of computational iterations",  fontsize=16)
plt.tight_layout()
plt.savefig(path_picture + "c_a_ratio_plot.eps", format='eps', dpi=1200)
plt.show()
