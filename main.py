from shop.prices import total
from shop.discounts import apply_discount

bill = total(50,3)
print("Original bill:",bill)
print("After discount:",apply_discount(bill))


