def calculate_buyers_premium(hammer_price):
    if hammer_price <= 900000:
        premium = hammer_price * 0.26
    elif hammer_price <= 6000000:
        premium = 900000 * 0.26 + (hammer_price - 900000) * 0.21
    else:
        premium = 900000 * 0.26 + 5100000 * 0.21 + (hammer_price - 6000000) * 0.15

    total_price = hammer_price + premium

    return total_price

def convert_to_usd(chf_total):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/CHF")
    data = response.json()
    chf_rate = data["rates"]["CHF"]
    usd_rate = data["rates"]["USD"]
    usd_total = chf_total / chf_rate * usd_rate
    return usd_total

hammer_price = 1000000
total_price = calculate_buyers_premium(hammer_price)
usd_total = convert_to_usd(total_price)
print("The total price (hammer price + buyer's premium) is CHF {:.2f} (USD {:.2f})".format(total_price, usd_total))
