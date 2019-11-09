#!/bin/sh -f
for Layer in 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
do
mkdir $Layer\_C_Vakuum
cp INCAR POSCAR KPOINTS POTCAR jobfile $Layer\_C_Vakuum/
cd $Layer\_C_Vakuum
#Declearing variables:
num1=14.8790043000000001
num2=11.15925323
num3=12.72413762
num4=9.59436883
#Summation of variables with layer thickness
sum1=$(echo "$num1+$Layer" | bc)
sum2=$(echo "$num2+$Layer" | bc)
sum3=$(echo "$num3+$Layer" | bc)
sum4=$(echo "$num4+$Layer" | bc)
#Changing the POSCAR-file:
sed -i '' -e s/$num1/$sum1/  POSCAR
sed -i '' -e s/$num2/$sum2/  POSCAR
sed -i '' -e s/$num3/$sum3/  POSCAR
sed -i '' -e s/$num4/$sum4/  POSCAR
cd ..
done
