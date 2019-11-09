#!/bin/sh -f
for Layer in 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
do
mkdir $Layer\_C_Vakuum
cp INCAR POSCAR KPOINTS POTCAR jobfile $Layer\_C_Vakuum/
cd $Layer\_C_Vakuum
#Declearing variables:
num1=14.8790043000000001
#Summation of variables with layer thickness
sum1=$(echo "$num1+$Layer" | bc)
#Changing the POSCAR-file:
sed -i s/$num1/$sum1/  POSCAR
cd ..
done