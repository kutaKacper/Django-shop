

def calculate_discount(total_cost, discount_percentage):
    discount_amount = (float(total_cost) * float(discount_percentage)) / 100
    discounted_cost = round((total_cost - discount_amount), 2)
    return discounted_cost