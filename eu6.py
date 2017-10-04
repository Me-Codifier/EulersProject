n=int(input())
n+=1
sqr=0
smsqr=0
square=[i**2 for i in range(n)]
sumsqr=[i for i in range(n)]
for i in range(n):
    sqr+=square[i]
for i in range(n):
    smsqr+=sumsqr[i]

print('sum of {} squares is {}'.format(n,sqr))
print('Square of {} sum is {}'.format(n,smsqr**2))
dif=sqr-(smsqr**2)
ttl=sqr+(smsqr**2)
print('Difference -> {}'.format(dif))
print('total      -> {}'.format(ttl))

"""
OR
limit = 100
sum = limit(limit + 1)/2
sum sq = (2limit + 1)(limit + 1)limit/6
print sum2 − sum sq
"""
