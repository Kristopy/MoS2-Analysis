#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import re
import os
import shutil
import sys
import numpy as np
from pylab import *
from ase import io
from ase.dft.kpoints import ibz_points, get_bandpath, special_paths, sc_special_points
from matplotlib import rc, rcParams

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Random']})
path_picture = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Pictures/'

#path_read_files = 'ABEL/Bandstructures/Slab/BAND_CALCULATIONS/'
#path_read_files2 = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/ABEL/Bandstructures/Slab/BAND_CALCULATIONS/'
path_read_files = 'Slab_altered_a_Bandstructure/BANDCALCULATIONS/'
path_read_files2 = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/Slab_altered_a_Bandstructure/BANDCALCULATIONS/'

# Read crystal structure from POSCAR
atoms = io.read(path_read_files2 + 'POSCAR')

# Read Fermi level from OUTCAR
Fermi = float(os.popen('grep fermi' + ' cd ../' +
                       path_read_files + 'OUTCAR').readlines()[1].split()[3])

print (Fermi)

# Fermi of TEST slab:
#Fermi = -3.7388
Fermi = -3.7388

# Read band energies from EIGENVAL
with open(path_read_files2 + 'EIGENVAL') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    comment = f.readline()
    unknown, npoints, nbands = [int(x) for x in f.readline().split()]
    blankline = f.readline()
    band_energies = [[] for i in range(nbands)]
    for i in range(npoints):
        x, y, z, weight = [float(x) for x in f.readline().split()]
        for j in range(nbands):
            fields = f.readline().split()
            id, energy = int(fields[0]), float(fields[1])
            band_energies[id-1].append(energy)
        blankline = f.readline()
f.close()
# Convert to numpy array
band_energies = np.array(band_energies)
# Renormalize energy to the Fermi level
band_energies = band_energies-Fermi

# Define special points
# See https://wiki.fysik.dtu.dk/ase/ase/dft/kpoints.html
# for special points in different Bravais cells
points = sc_special_points["hexagonal"]

M = points["M"]
K = points["K"]
G = points["G"]
# Define path to be plotted. Has to be the same that was
# calculated by VASP (defined in KPOINTS)
path = get_bandpath([G, M, K, G], atoms.cell, npoints=npoints)
x2, X2, labels = path.get_linear_kpoint_axis()
labels = [label.replace('G', '\Gamma') for label in labels]
labels = [label.replace('Kpt0', 'K') for label in labels]
labels = [label.replace('Z', 'M') for label in labels]

# Hardcode plots with even distance between special points:
nkpoints = int(npoints/(len(labels)-1))
x1 = list(range(npoints))
X1 = [x1[0]]+x1[nkpoints-1::nkpoints]

print (labels)
# Create plot
for iband in range(nbands):
    plot(x1, band_energies[iband, :], linewidth=0.75, color="k")

# 0.8097
# Change range:
margins(0)
ylim(-4.10 + 0.8097, 4.18 + 0.8097)
title('Band structure - $MoS_2$ [Slab]', fontsize=17)
xlabel('Irreducible Brilloiun zone [$\mathbf{k}$]', fontsize=16)
annotate("", xy=(X1[2], 0.76 + 0.8097), xytext=(X1[2], -0.8 + 0.8097),
         arrowprops={'arrowstyle': '<->', 'ls': 'dashed', 'lw': 0.5}, va='center')
ylabel('$E - E_{Fermi}$ (eV)', fontsize=16)
text(X1[2] + 0.5, -0.2 + 0.8097, "Direct Bandgap")
plot([X1[0], X1[3]], [0.0, 0.0], linestyle="--", color="k", linewidth=0.6)
plot([X1[0], X1[3]], [1.6879, 1.6879], linestyle="--", color="k", linewidth=0.6)
tight_layout()
# Print figure to file
xticks(X1, ['$%s$' % n for n in labels])
savefig(path_picture + 'bandstruct_Slab.eps', format='eps', dpi=1200)

show()
