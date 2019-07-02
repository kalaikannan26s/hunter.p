l = int(input())
s = list(map(int,input().split()))
r = []
for i in range(len(s)):
    if s.count(s[i]) > 1:
        if s[i] not in r:
            r.append(s[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
