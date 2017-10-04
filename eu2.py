fibb=[]
EvenFib=[]
a=0
b=1
add=0
for i in range(100):
    c=a+b
    a=b
    b=c
    fibb.append(c)
    if c>=4000000:
        break
print(fibb)
for i in range(len(fibb)):
    if fibb[i]%2==0:
        EvenFib.append(fibb[i])
print(EvenFib)

for i in range(len(EvenFib)):
    add+=EvenFib[i]

print('The sum of even fabbonice series within 4000000 is {}.'.format(add))
