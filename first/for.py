__author__ = 'Mohamed_Ramadan_PC'
def array_muliply(a,b):
    sum=0
    i=0

    for x in range(0,len(a),1):
        for y in range(0,len(a[x]),1):
            sum+=a[x][y]*b[x][y]

    print(sum)


a=[[1,2,3,4],[1,2,3,4]]
b=[[10,20,30,40],[1,2,3,4]]

array_muliply(a,b)