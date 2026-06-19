#region колонка слов

from itertools import *

cnt = 0
for w in product(sorted("АКЦЕНТ"),repeat = 5):
    s = "".join(w)
    cnt += 1
    if s[0] != "А" and s[0] != "Е" and s[0] != "К" and s.count("Ц") >= 2:
        print(s, cnt)

#endregion