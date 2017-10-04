n=int(input('Enter the range from 0 to where the sum to be calculated: '))
A=[i for i in range(n) if i%3==0 or i%5==0]
print(A)
B=0
for i in range(len(A)):
    B+=A[i]
print('There are {} numbers which sums to {}'.format(len(A),B))
