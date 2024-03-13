uah_usd = 0.026
usd_uah = 38.76
uah_eur = 0.024
eur_uah = 42.41

currency = input("Choose the option (UAH-USD, USD-UAH, UAH-EUR, EUR-UAH): ").strip().upper()

if currency == "UAH-USD":
    amount_uah = float(input("Enter the amount in UAH: "))
    amount_usd = amount_uah * uah_usd
    print(f"The amount in USD is: {amount_usd}")
elif currency == "USD-UAH":
    amount_usd = float(input("Enter the amount in USD: "))
    amount_uah = amount_usd * usd_uah
    print(f"The amount in UAH is: {amount_uah}")
elif currency == "UAH-EUR":
    amount_uah = float(input("Enter the amount in UAH: "))
    amount_eur = amount_uah * uah_eur
    print(f"The amount in EUR is: {amount_eur}")
elif currency == "EUR-UAH":
    amount_eur = float(input("Enter the amount in EUR: "))
    amount_uah = amount_eur * eur_uah
    print(f"The amount in UAH is: {amount_uah}")
else:
    print("Try again")
