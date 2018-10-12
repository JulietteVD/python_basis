# --------- buspass.py -------------------------------
# -- This programm prints the eligibility for each person ------
# -- to have access to the bus pass ----------------
# -- By Juliette Vintrou ---------------------------
# -- 26/09/2018 ------------------------------------

age = int(input("Enter your age in years: "))
decision = " Not qualify for bus pass"
if age >= 65:
    decision="Qualify for bus pass"
print(decision)

