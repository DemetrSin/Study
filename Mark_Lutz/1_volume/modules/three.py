import two
import changer, one

print(one.lst)

n = 10

print(n)  # 10
print(one.n)  # 77
print(two.n)  # 77
print(one.n)  # 77

print(one.change)  # 1001

print(one.for_from)  # 1

z = 10000
print(z, two.z, one.z)  # 10000 1000 100


changer.printer()  # First version
from imp import reload
reload(changer)
changer.printer()  # Changed version

