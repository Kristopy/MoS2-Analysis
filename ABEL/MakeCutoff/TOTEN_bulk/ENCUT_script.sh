#!/bin/sh -f
for Energy in 200 250 300 350 400 450 500 550 600 650 700 750 800 850 900 950 1000
do 
mkdir $Energy\eV
sed s/400/$Energy/  INCAR > $Energy\eV/INCAR
cp POSCAR KPOINTS POTCAR jobfile $Energy\eV/
done