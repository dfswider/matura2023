s = [5, 14, 17, 25]
A = [[1, 2, 3], [1, 2, 5, 10], [13, 5, 5, 2, 7], [7, 6, 5, 4, 3, 2, 1]]


def tour(B, A, s, k):
    for i in range(s, A[k]-1, -1):
        if B[i-A[k]] == 'p' and B[i] == '.':
            B[i] = 'p'
    return B


for game in range(0, len(s)):
    n = len(A[game])
    B = []
    for i in range(s[game]+1):
        B.append('.')
    B[0] = 'p'
    for k in range(0, n):
        B = tour(B, A[game], s[game], k)

    if B[s[game]] == 'p':
        print("Success: YES!!!")
    else:
        print("Success: NO :-(")

ss = 500
AA = []
for aa in range(5, 105, 5):
    AA.append(aa)
nn = len(AA)
BB = []
for bb in range(0, ss+1):
    BB.append('.')
BB[0] = 'p'
for kk in range(0, nn):
    B = tour(BB, AA, ss, kk)

counter = 0
for b in range(len(B)):
    if B[b] == 'p':
        counter += 1

print("End with ", counter, " figures")
