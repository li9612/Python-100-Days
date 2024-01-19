num=input()
num=int(num)
list1=list()
x=0
dic = {}
list_s={}

dic1 ={"asd":1}


#按照/拆分字符串，去掉无用元素
for x in range(num):

    a=input()
    b=a.split("/")
    b.pop(0)
    c=b
    list1.append(c)
    dep = 0
    l_list1=len(list1)
    for y in range(l_list1+1):
        k=list1[x][y]+str(dep)
        if k in dic:
            dic[k]=dic[k]+1
        else:
            dic[k]=0
        dep=dep+1
# print(list1)
print(dic)
answer=input()

list_a=answer.split(" ")

print(list_a)

a1=int(list_a[0])-1
a2=list_a[1]+str(a1)
if a2 in  dic:

    print(dic.get(a2)+1)
else:
    print(0)
