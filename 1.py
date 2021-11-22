fin = open ("height.in")
fout = open ("height.out", 'w')
n = int(fin.readline())
bst = [1] * n
for j in range (n):
    line = list(map(int, fin.readline().split()))
    if line[1] != 0:
        bst[line[1] - 1] = bst[j] + 1
    if line[2] != 0:
        bst[line[2] - 1] = bst[j] + 1
if n == 0:
    print(0, file = fout)
else:
    print (max(bst), file = fout)
fout.close()
