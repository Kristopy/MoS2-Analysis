#!/bin/sh -f
for Kpoints in 1 2 3 4 5 6 7 8 9
do 
mkdir $Kpoints\KPOINTS
cp INCAR POSCAR KPOINTS POTCAR jobfile $Kpoints\KPOINTS/
cd $Kpoints\KPOINTS
makekpoints -d $Kpoints
sed s/1/$Kpoints/  KPOINTS > $Kpoints\KPOINTS/KPOINTS
cd ..
done