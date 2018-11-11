n=4
x=1.9

vetx=[0, 0.5   , 1     , 1.5   , 2.3   ]
vety=[3, 0.4060, 0.0549, 0.0074, 0.0003]

def difdiv(n,i):
    if n==0:
        return vety[i]
    else:
        return float((difdiv(n-1,i+1) - difdiv(n-1,i)) / (vetx[i+n] - vetx[i]))

result=0
for i in range(0, n+1):
    parcela=difdiv(i,0)
    for j in range(0, i):
        parcela*=(x-vetx[j])
    result+=parcela
print(result)