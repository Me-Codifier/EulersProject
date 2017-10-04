
A=[]
for i in range(100,1000):
    for j in range(100,1000):
        b=i*j
        b=str(b)
        c=b[::-1]
        c=int(c)
        b=int(b)
        if b==c:
            A.append(b)
        
A.sort()            
print('The highest Palindrome number by multiplying 3 digit number is ==>> {}'.format(A[len(A)-1]))
