import currency

amount = 500000
converted = currency.mmk_to_usd(amount)

print(f"{amount} MMK = {converted:.2f} USD")
