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

path_read_files = 'ABEL/Bandstructures/Bulk/BANDCALCULATION/'
path_read_files2 = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/ABEL/Bandstructures/Bulk/BANDCALCULATION/'
#path_read_files = 'TEST_BS/BANDCALCULATION/'
#path_read_files2 = '/Users/kristoffervarslott/Documents/MENA/Master_MENA/1.Master/FYS-MENA4111/MoS2-Analysis/TEST_BS/BANDCALCULATION/'

# Read crystal structure from POSCAR
atoms = io.read(path_read_files2 + 'POSCAR')

# Read Fermi level from OUTCAR
Fermi = float(os.popen('grep fermi' + ' cd ../' +
                       path_read_files + 'OUTCAR').readlines()[1].split()[3])

print (Fermi)
#Fermi = 6.0507
#Fermi = 4.6300
# Hard code Fermi level from SCF calculation
Fermi = 5.6000
# Fermi bulk = 5.2091
# Fermi Slab = -2.9188

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


# Hardcode plots with even distance between special points:
nkpoints = int(npoints/(len(labels)-1))
x1 = list(range(npoints))
X1 = [x1[0]]+x1[nkpoints-1::nkpoints]

xticks(X1, ['$%s$' % n for n in labels])

# Create plot
for iband in range(nbands):
    plot(x1, band_energies[iband, :], linewidth=0.75, color="k")

# 0.5731
# Change range:
margins(0)
ylim(-2.9538, 2.9)
title('Band structure - $MoS_2$ [Bulk]', fontsize=17)
xlabel('Irreducible Brilloiun zone [$\mathbf{k}$]', fontsize=16)
ylabel('$E - E_{Fermi}$ (eV)', fontsize=16)
annotate("", xy=(X1[2] + (X1[3] - X1[2])/2, 0.9), xytext=(X1[3], 0.03),
         arrowprops={'arrowstyle': '<->', 'ls': 'dashed', 'lw': 0.5}, va='center')
text(X1[3]/1.5, 0.27, "Indirect Bandgap")
tight_layout()
# Print figure to file
plot([X1[0], X1[3]], [0, 0], linestyle="--", color="k", linewidth=0.6)
plot([X1[0], X1[3]], [0.9211, 0.9211], linestyle="--", color="k", linewidth=0.6)
savefig(path_picture + 'bandstruct_bulk.eps', format='eps', dpi=1200)
show()
