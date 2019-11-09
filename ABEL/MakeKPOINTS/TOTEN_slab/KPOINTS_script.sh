#!/bin/sh -f
for Kpoints in 1 2 3 4 5 6 7 8 9
do
mkdir $Kpoints\KPOINTS
cp INCAR POSCAR KPOINTS POTCAR jobfile $Kpoints\KPOINTS/
cd $Kpoints\KPOINTS
echo "Current KPOINTS after makekpoints:"
makekpoints -d $Kpoints
echo "Changing KPOINTS for slab:"
sed -i '4s/..$/ 1/'  KPOINTS
sed -n 4p KPOINTS
cd ..
done