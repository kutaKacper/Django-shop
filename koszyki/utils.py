
def calculate_total_price(koszyk_items):
    total_price = sum(item.produkt.price * item.amount for item in koszyk_items)
    return total_price