x,y=map(int,input().split())
y=str(y)
q=0
for i in range(1,x):
    q=str(i)
    p=list(q)
    if y in p:
        q=1
        print(i,end=" ")
if q==0:
    print("-1")
print(q)