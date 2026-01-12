from datetime import datetime

t = int(input())
fmt = "%a %d %b %Y %H:%M:%S %z"

for _ in range(t):
    t1 = datetime.strptime(input(), fmt)
    t2 = datetime.strptime(input(), fmt)
    print(abs(int((t1 - t2).total_seconds())))
