from shop.prices import total
from shop.discounts import apply_discount
from shop.delivery import delivery_fee
bill = total(50,3)
print("Original bill:",bill)
print("After discount:",apply_discount(bill))
print("with delivery",delivery_fee(apply_discount(bill)))


