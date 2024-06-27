from timeit import default_timer as timer

def insertie(v):
    n = len(v)
    for i in range(1, n):
        p = i
        while p > 0 and v[p] < v[p - 1]:
            v[p], v[p - 1] = v[p - 1], v[p]
            p -= 1

def selectie(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]

def bule(v):
    n = len(v)
    for i in range(n - 1):
        sorted = True
        for j in range(n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                sorted = False
        if sorted:
            break
def bula_des(v):
    n = len(v)
    for i in range(n - 1):
        sorted = True
        for j in range(n - i - 1):
            if v[j] < v[j + 1]:  # Inversăm condiția de comparație
                v[j], v[j + 1] = v[j + 1], v[j]
                sorted = False
        if sorted:
            break



def rapida_partitie(v, st, dr):
    pivot = v[dr]
    i = st - 1
    for j in range(st, dr):
        if v[j] <= pivot:
            i = i + 1
            v[i], v[j] = v[j], v[i]
    v[i + 1], v[dr] = v[dr], v[i + 1]
    return i + 1

def rapida(v, st, dr):
    if st < dr:
        x = rapida_partitie(v, st, dr)
        rapida(v, st, x - 1)
        rapida(v, x + 1, dr)
    return v

def interclasare_inbina(v, st, mi, dr):
    n1 = mi - st + 1
    n2 = dr - mi
    s = [0] * n1
    d = [0] * n2
    for i in range(0, n1):
        s[i] = v[st + i]  # Corectat indexul aici
    for i in range(0, n2):
        d[i] = v[mi + 1 + i]  # Corectat indexul aici
    i, j, k = 0, 0, st
    while i < n1 and j < n2:
        if s[i] <= d[j]:
            v[k] = s[i]
            i += 1
        else:
            v[k] = d[j]
            j += 1
        k += 1
    while i < n1:
        v[k] = s[i]
        i += 1
        k += 1
    while j < n2:
        v[k] = d[j]
        j += 1
        k += 1

def interclasare(v, st, dr):
    if st < dr:
        mi = (st + dr) // 2
        interclasare(v, st, mi)
        interclasare(v, mi + 1, dr)
        interclasare_inbina(v, st, mi, dr)  

def gramezi_x(v, n, i):
    L = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and v[L] > v[l]:  # Inversăm condiția de comparare
        L = l
    if r < n and v[L] > v[r]:  # Inversăm condiția de comparare
        L = r
    if L != i:
        v[i], v[L] = v[L], v[i]
        gramezi_x(v, n, L)

def gramezi(v):
    n = len(v)
    for i in range(n // 2 - 1, - 1, -1):
        gramezi_x(v, n, i)
    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]
        gramezi_x(v, i, 0)

def radix_sort(v, x):
    n = len(v)
    a1 = [0] * n
    a2 = [0] * 10
    for i in range(0, n):
        index = v[i] // x
        a2[index % 10] += 1
    for i in range(1, 10):
        a2[i] += a2[i - 1]
    i = n - 1
    while i >= 0:
        index = v[i] // x
        a1[a2[index % 10] - 1] = v[i]
        a2[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        v[i] = a1[i]
def radix(v):
    maxi = max(v)
    x = 1
    while maxi / x >= 1:
        radix_sort(v, x)
        x *= 10

fin = open("50000.txt", "r")
f = fin.readline().split()
v = [int(i) for i in f]
fin.close()

start = timer()
interclasare(v,0, len(v) - 1)

end = timer()
print(v)
print("Execution Time:", round(end - start, 2), "seconds")