# --------- currency.py -------------------------------
# -- This programm prints the equivalent amount in dollars ------
# -- from an amount inputs in euro  ----------------
# -- By Juliette Vintrou ---------------------------
# -- 26/09/2018 ------------------------------------

EUROS_RATE_DOLLAR = 1.177
euro = float(input("What is the amount in euros :"))
dollar = euro * EUROS_RATE_DOLLAR
print("The amount in US Dollar is:",dollar)
