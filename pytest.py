def convert_currency(amount):
  # Define conversion rates
  usd_rate = 1.0 # 1 US dollar is equal to 1 US dollar
  brl_rate = 5.82 # 1 US dollar is equal to 5.82 Brazilian Reals
  eu_rate = 0.82 # 1 US dollar is equal to 0.82 Euros

  # Convert input amount to different currencies
  usd_amount = amount * usd_rate
  brl_amount = amount * brl_rate
  eu_amount = amount * eu_rate

  # Print results
  print(f"{amount} US dollars is equivalent to {usd_amount} US dollars, {brl_amount} Brazilian Reals, and {eu_amount} Euros.")

# Test the function with different input values
convert_currency(100)
convert_currency(200)
convert_currency(300)