a=int(input())
b=int(input())
e=0
c=a**b
print(c)
c=str(c)
d=list(c.strip())
print(d)
for i in range(len(d)):
    e+=int(d[i])
print(e)
