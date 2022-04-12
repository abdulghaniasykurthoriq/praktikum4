from bad_ocp import Discount as BadDiscount
from good_ocp import Discount as GoodDiscount 
from good_ocp import VIPDiscount
from good_ocp import SuperVIPDiscount


print("="*3, 'BAD OCP', "="*3)
bad = BadDiscount('normal', 2000)
print(bad.get_discount())

print("="*3, 'GOOD OCP', "="*3)
good = GoodDiscount(2000)
print(good.get_discount())

print("="*3, 'GOOD OCP', "="*3)
good = VIPDiscount(2000)
print(good.get_discount())

print("="*3, 'GOOD OCP', "="*3)
good = SuperVIPDiscount(2000)
print(good.get_discount())

print("="*40)

pelanggans = [
    BadDiscount('normal', 2000),
    GoodDiscount(2000),
    VIPDiscount(2000),
    SuperVIPDiscount(2000)
]
for plg in pelanggans:
    print('Diskon : ', plg.get_discount())