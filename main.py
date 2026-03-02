# 1.m
def kvadrat(c):
    return c ** 2

res = kvadrat(9)
print(res)

# 2.m
def qowiw(a, b):
    return a + b

res = qowiw(14, 34)
print(res)

3.m

# 4.m
def juft_toq(son):
    if son % 2 == 0:
        return "Juft son"

    else:
        return "Toq son"
print(juf_toq)

# 6.m
def eng_katta(a, b, c):
    return max(a, b, c)
print(eng_katta(3, 7, 5))
print(eng_katta(10, 4, 8))

# 7.m
def teskari(matn):
    return matn[::-1]

print(teskari("salom"))

# 8.m
def unli(matn):
    unlilar = "aeiouAEIOUo‘O‘"
    sanoq = 0
    for harf in matn:
        if harf in unlilar:
            sanoq += 1
    return sanoq

print(unli("Salom Dunyo"))

# 9.m
def palindrommi(soz):
    soz = soz.lower()
    return soz == soz[::-1]

print(palindrommi("alla"))
print(palindrommi("salom"))

# 10.m
def qiymat(a,b):
    
