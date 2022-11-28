filename = "/home/wiercik/szkola/Przedmioty/Informatyka/Matura2023/Dane_2203/liczby.txt"
file = open(filename)
lines = file.readlines()
n = len(lines)
print(n, " numbers read")


def is_prime(m):
    if (m & 1) == 1:
        for i in range(3, m//2, 2):
            if m % i == 0:
                return False
    return True


def euclides(a, b):

    r = 0
    if b > a:
        c = b
        b = a
        a = c
    r = a % b
    while r != 0:
        if b > a:
            c = b
            b = a
            a = c
        a = a - b
        r = a % b
    return b

M = []
a = []
b = []
nwd = []
isPrime = []
countPrimes = 0
countVsPrimes = 0
for i in range(n):
    lineNumbers = lines[i].split()
    M.append(lineNumbers[0])
    a.append(lineNumbers[1])
    b.append(lineNumbers[2])
    nwd.append(euclides(int(M[i]), a[i]))
    if nwd[i] == 1:
        countVsPrimes += 1
    if is_prime(int(M[i])):
        isPrime.append(True)
        countPrimes += 1
    else:
        isPrime.append(False)

    print(M[i], " is prime? ", isPrime[i], "is vs prime?", M[i], a[i])

print(countPrimes)
