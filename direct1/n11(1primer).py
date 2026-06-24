#region нахождение букв

from math import *

for bykvi in range(1,10000):
     i = ceil(log2(bykvi))
     sernum = ceil(172 * i / 8) # 172 - кол-во символов
     if 187564 * sernum <= 39 * 2 ** 20:
         print(bykvi)
          
#endregion
