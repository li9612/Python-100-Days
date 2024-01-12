s=input()
a=[]
op=[]

now=""

for x in  s:
    if x.isdigit():
        now+=x
    else:
        if x=="#":
            op.append(1)
        else:
            op.append(0)
        a.append(now)
        now=""
a.append(now)

a=[int(x) for x in a]

n=len(op)
i =0
b=[]
while i<n:
    if op[i]==1:
        x=a[0]
        y=a[1]
        z=4*x+3*y+2
        a.pop(0)
        a.pop(0)
        a=[z]+a
        i+=1
    else:
        b.append(a.pop(0))
        i+=1
