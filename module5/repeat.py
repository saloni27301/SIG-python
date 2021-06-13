print("Saloni(1803010120)")

def olist(L1,n):
    for i in range(n):
        print(L1[i],end = "")
def nlist(L1,n):
    for i in range(n):
        if((i+1)%2==0):
            L1[i]= "#"
    olist(L1,n)
L1=[1,2,3,4,5]
n=len(L1)
nlist(L1,n)