def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
x=int(input())
A=fact(x)
print(A)
A=str(A)
B=list(A.strip())
print(B)
C=0
for i in range(len(B)):
    C+=int(B[i])
print('Digital Sum: {}'.format(C))
