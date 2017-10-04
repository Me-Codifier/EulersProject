for a in range(1,1000):
    for b in range(1,1000):
        for c in range(334,1000):
            if a**2+b**2==c**2 and b>=a:
                print('{},{},{}'.format(a,b,c))
                if a+b+c==1000:
                    print('========>>>>>>>>>>{},{},{}'.format(a,b,c))
                 
