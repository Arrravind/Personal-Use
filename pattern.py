
n = int(input())
half =n//2
print(half)
r, c = n, n + 1
n = 1
num = 97
k = c-1
o = c//2
l = o + 1
for i in range( r):
    if i<=half:
        for j in range(c):
            if j<=i:
                print(n, end=' ')
                n += 1
            elif j>=k:
                print(chr(num), end=' ')
                num += 1
            else:
                print('*', end=' ')
        k -= 1
    else:
        for j in range(c):
            if j<o-1:
                print(n, end=' ')
                n += 1
                
            elif j>=l:
                print(chr(num), end=' ')
                num += 1
            else:
                print('*', end=' ')
        o -= 1
        l += 1
    print()
