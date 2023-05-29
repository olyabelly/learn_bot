stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

def discounted(price, discount, max_discount=30, phone_name=''):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except (ValueError, TypeError):
        print("Неккоректные данные")


    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)


    
for phone in stock:
    phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name = phone['name'])
print (stock)