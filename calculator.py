def calculate_discount(price, is_member):
    if is_member:
        return price*0.2
    
    return price * 0.15