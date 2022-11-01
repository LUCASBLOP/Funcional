def Fib(x):
    return Fib(x-1)+Fib(x-2) if x>=2 else 1 if x==1 else 0
def Fact(x):
    return x*Fact(x-1) if x>1 else 1
List=[[1,2],[3,4],[5,6]]
Lista2=[]
for elem in List:
    b=Fib(elem[0])
    c=Fact(elem[1])
    Lista2.append([b,c])
print(Lista2)    
