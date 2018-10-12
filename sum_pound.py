# --------- sum_pound.py -------------------------------
# -- This programm sums two amount from 6 individual numbers ------
# -- and prints them  ----------------
# -- By Juliette Vintrou ---------------------------
# -- 26/09/2018 ------------------------------------

PENCE_TO_SCHILLING = 12
SCHILLING_TO_POUND = 20


print("Amount number 1 :")
pound1=int(input("Pound :"))
shilling1=int(input("Schilling :"))
pence1=int(input("Pence :"))

print("Amount number 2:")
pound2=int(input("Pound :"))
shilling2=int(input("Schilling :"))
pence2=int(input("Pence :"))

sum_pound = pound1 + pound2
sum_shilling = shilling1 + shilling2
sum_pence = pence1 + pence2

if sum_pence >= PENCE_TO_SCHILLING:
    temp = int(sum_pence/PENCE_TO_SCHILLING)
    sum_shilling = int(sum_shilling + temp)
    sum_pence = int(sum_pence - temp * PENCE_TO_SCHILLING)

if sum_shilling >= SCHILLING_TO_POUND:
    temp = int(sum_shilling/SCHILLING_TO_POUND)
    sum_pound = int(sum_pound + temp)
    sum_shilling = int(sum_shilling - temp * SCHILLING_TO_POUND)

print("The sum of this two amounts is the following :",sum_pound,"£ ,",sum_shilling,"s ,",sum_pence,"d")  
