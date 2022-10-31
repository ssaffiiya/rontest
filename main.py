def annagramma(s, p):
    a = []
    s = s.lower()
    p = p.lower()
    for i in range(len(s) - len(p) + 1):
        k = 0
        for j in range(len(p)):
            if (s[i:i + len(p)].find(p[j])) != -1:
                k += 1
                if k == len(p):
                    k = 0
                    a.append(i)
    return a


s = (input())
p = (input())
if annagramma(s, p):
    print(annagramma(s, p))
else:
    print("there is no anogramms")
