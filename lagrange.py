x=2.3 #ponto à ser interpolado
n=1   #nº de pontos -1

vetx=[1, 3]
vety=[4, 2]

def prod(x, i, j):
    print('({} - {})/({} - {})'.format(x, vetx[j], vetx[i], vetx[j]),end=' *')
    return float((x - vetx[j]) / (vetx[i] - vetx[j]))

result=0
for i in range(0, n+1):
    parcela=vety[i]
    for j in range(0, n+1):
        if j!=i:
            parcela *= prod(x,i,j)
    result += parcela
    print(vety[i])
print(result)
